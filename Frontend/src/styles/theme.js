import { extendTheme } from "@chakra-ui/react";
import { config } from "./config";

const theme = extendTheme({
  colors: {
    brand: {
      primary: "#024ddf",
      secondary: "#f6f6f6",
      text: "#121212",
    },
  },
  styles: {
    global: {
      // Set background color for the whole website
      body: {
        bg: "brand.secondary", // Use your custom color defined in the theme
        color: "brand.text", // Optional: set a default text color
      },
    },
  },
  config,
});

export default theme;
