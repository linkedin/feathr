import { ApplicationInsights } from '@microsoft/applicationinsights-web';
import { ReactPlugin } from '@microsoft/applicationinsights-react-js';
import { createBrowserHistory } from 'history';


const browserHistory = createBrowserHistory();
const reactPlugin = new ReactPlugin();
const appInsights = new ApplicationInsights({
  config: {
    instrumentationKey: process.env.REACT_APP_APPINSIGHTS_KEY,
    extensions: [reactPlugin],
    extensionConfig: {
      [reactPlugin.identifier]: { history: browserHistory },
    },
  },
});
appInsights.loadAppInsights();
export { reactPlugin, appInsights };
