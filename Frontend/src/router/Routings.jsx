/**
 * @note
 * for hook alternative of route element composition:
 * - https://reactrouter.com/docs/en/v6/upgrading/v5#use-useroutes-instead-of-react-router-config
 * - https://reactrouter.com/docs/en/v6/examples/route-objects
 *
 * might need to take notes on:
 * - https://reactrouter.com/docs/en/v6/upgrading/v5#note-on-link-to-values
 */
import React, { Suspense } from "react";
import { Routes, Route } from "react-router-dom";

import { routes } from "./routes";
import Home from "../pages/home";

const Routings = () => {
  return (
    <Suspense>
      <Routes>
        {routes.map((routeProps) => (
          <Route {...routeProps} key={routeProps.path} />
        ))}
        {/* <Route path="*" element={<Home />} /> */}
      </Routes>
    </Suspense>
  );
};

export default Routings;
