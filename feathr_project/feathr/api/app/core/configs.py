import logging
import os

API_Version = "/api/v1"
log_level = os.getenv("logLevel", "INFO")
app_insights_connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
formatter = logging.Formatter("[%(asctime)s] [%(name)s:%(lineno)s - %(funcName)5s()] %(levelname)s - %(message)s")
appServiceKey =  "mockAppServiceKey" # os.getenv("AppServiceKey")
default_purview_name = "feathrazuretest3-purview1"
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)