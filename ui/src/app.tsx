import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Layout } from "antd";
import { QueryClient, QueryClientProvider } from "react-query";
import { Configuration, InteractionType, PublicClientApplication, } from "@azure/msal-browser";
import { MsalAuthenticationTemplate, MsalProvider } from "@azure/msal-react";
import Header from "./components/header/header";
import SideMenu from "./components/sidemenu/siteMenu";
import Features from "./pages/feature/features";
import NewFeature from "./pages/feature/newFeature";
import FeatureDetails from "./pages/feature/featureDetails";
import DataSources from "./pages/dataSource/dataSources";
import Jobs from "./pages/jobs/jobs";
import Monitoring from "./pages/monitoring/monitoring";
import LineageGraph from "./pages/feature/lineageGraph";

type Props = {};
const queryClient = new QueryClient();

const msalConfig: Configuration = {
  auth: {
    clientId: process.env.REACT_APP_AAD_APP_CLIENT_ID,
    authority: process.env.REACT_APP_AAD_APP_AUTHORITY,
    redirectUri: window.location.origin,
  },
};
const pca = new PublicClientApplication(msalConfig);
const App: React.FC<Props> = () => {
  return (
    <MsalProvider instance={ pca }>
      <MsalAuthenticationTemplate interactionType={ InteractionType.Redirect }>
        <QueryClientProvider client={ queryClient }>
          <BrowserRouter>
            <Layout style={ { minHeight: "100vh" } }>
              <SideMenu />
              <Layout>
                <Header />
                <Routes>
                  <Route path="/dataSources" element={ <DataSources /> } />
                  <Route path="/features" element={ <Features /> } />
                  <Route path="/new-feature" element={ <NewFeature /> } />
                  <Route path="/projects/:project/features/:qualifiedName" element={ <FeatureDetails /> } />
                  <Route path="/projects/:project/lineage" element={ <LineageGraph /> } />
                  <Route path="/jobs" element={ <Jobs /> } />
                  <Route path="/monitoring" element={ <Monitoring /> } />
                </Routes>
              </Layout>
            </Layout>
          </BrowserRouter>
        </QueryClientProvider>
      </MsalAuthenticationTemplate>
    </MsalProvider>
  );
};

export default App;
