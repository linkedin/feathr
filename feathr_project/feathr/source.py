
from abc import ABC, abstractmethod
from typing import List, Optional
from jinja2 import Template


class Source:
    """External data source for feature. Typically a 'table'.
     Attributes:
         name: name of the source
         event_timestamp_column: column name of the event timestamp
         timestamp_format: the format of the event_timestamp_column, e.g. yyyy/MM/DD.
    """
    def __init__(self,
                 name: str,
                 event_timestamp_column: Optional[str], 
                 timestamp_format: Optional[str] = "epoch") -> None:
        self.name = name
        self.event_timestamp_column = event_timestamp_column
        self.timestamp_format = timestamp_format

    def __eq__(self, other):
        """A source is equal to another if name is equal."""
        return self.name == other.name

    def __hash__(self):
        """A source can be identified with the name"""
        return hash(self.name)

    def to_write_config(self) -> str:
        pass

class InputContext(Source):
    """A type of 'passthrough' source, a.k.a. request feature source.
    """
    SOURCE_NAME = "PASSTHROUGH"
    def __init__(self) -> None:
        super().__init__(self.SOURCE_NAME, None, None)

    def to_feature_config(self) -> str:
        return "source: " + self.name


class HdfsSource(Source):
    """A data source(table) stored on HDFS-like file system. Data can be fetch through a POSIX style path.

        Args:
            name (str): name of the source
            path (str): The location of the source data. 
            event_timestamp_column (Optional[str]): The timestamp field of your record. As sliding window aggregation feature assume each record in the source data should have a timestamp column. 
            timestamp_format (Optional[str], optional): The format of the timestamp field. Defaults to "epoch". Possible values are: 
            - `epoch` (seconds since epoch), for example `1647737463`
            - `epoch_millis` (milliseconds since epoch), for example `1647737517761`
            - Any date formats supported by [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html). 
                
        """
    def __init__(self, name: str, path: str, event_timestamp_column: Optional[str]= None, timestamp_format: Optional[str] = "epoch") -> None:
        super().__init__(name, event_timestamp_column, timestamp_format)
        self.path = path

    def to_feature_config(self) -> str:
        tm = Template("""  
            {{source.name}}: {
                location: {path: "{{source.path}}"}
                {% if source.event_timestamp_column is defined %}
                    timeWindowParameters: {
                        timestampColumn: "{{source.event_timestamp_column}}"
                        timestampColumnFormat: "{{source.timestamp_format}}"
                    }
                {% endif %}
            } 
        """)
        msg = tm.render(source=self)
        return msg

class JdbcSource(Source):
    def __init__(self, name: str, url: str = "", dbtable: Optional[str] = None, query: Optional[str] = None, auth: Optional[str] = None) -> None:
        super().__init__(name, None, None)
        self.url = url
        if dbtable is not None:
            self.dbtable = dbtable
        if query is not None:
            self.query = query
        if auth is not None:
            self.auth = auth.upper()
            if self.auth not in ["USERPASS", "TOKEN"]:
                raise ValueError("auth must be None or one of following values: ['userpass', 'token']")

    def get_required_properties(self):
        if not hasattr(self, "auth"):
            return []
        if self.auth == "USERPASS":
            return ["%s_USER" % self.name, "%s_PASSWORD" % self.name]
        elif self.auth == "TOKEN":
            return ["%s_TOKEN" % self.name]

    def to_feature_config(self) -> str:
        tm = Template("""  
            {{source.name}}: {
                location: {
                    url: "{{source.url}}"
                    {% if source.dbtable is defined %}
                    dbtable: "{{source.dbtable}}"
                    {% endif %}
                    {% if source.query is defined %}
                    query: "{{source.query}}"
                    {% endif %}
                    {% if source.auth is defined %}
                        {% if source.auth == "USERPASS" %}
                    user: "${{ "{" }}{{source.name}}_USER{{ "}" }}"
                    password: "${{ "{" }}{{source.name}}_PASSWORD{{ "}" }}"
                        {% else %}
                    useToken: true
                    token: "${{ "{" }}{{source.name}}_TOKEN{{ "}" }}"
                        {% endif %}
                    {% else %}
                    anonymous: true
                    {% endif %}
                }
            } 
        """)
        msg = tm.render(source=self)
        return msg

INPUT_CONTEXT = InputContext()