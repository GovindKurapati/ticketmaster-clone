import { Flex } from "@chakra-ui/react";
import React from "react";

import { useLocation } from "react-router-dom";
import Footer from "./footer";
import Header from "./header";

const Layout = ({ children }) => {
  const location = useLocation();

  // Define paths where you don't want to show the header and footer
  const hideHeaderFooterPaths = ["/login", "/signup"];

  // Check if current path matches any of these paths
  const shouldHideHeaderFooter = hideHeaderFooterPaths.includes(
    location.pathname
  );
  return (
    <Flex margin="0" transition="0.5s ease-out">
      <Flex wrap="wrap" w="100%">
        {!shouldHideHeaderFooter && <Header />}
        <Flex width="full" as="main">
          {children}
        </Flex>
        {!shouldHideHeaderFooter && <Footer />}
      </Flex>
    </Flex>
  );
};

export default Layout;
