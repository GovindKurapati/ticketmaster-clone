import "./App.css";
import Layout from "./layout";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Routings from "./router/Routings";
import { ChakraProvider } from "@chakra-ui/react";
import theme from "./styles/theme";

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Router>
        <Layout>
          <Routings />
        </Layout>
      </Router>
    </ChakraProvider>
  );
}

export default App;
