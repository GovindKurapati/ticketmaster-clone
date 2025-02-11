// src/api/api.js
import axios from "axios";

// Create an Axios instance with default settings (base URL, headers, etc.)
const api = axios.create({
  baseURL: "http://localhost:8080/", // Replace with your backend URL
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
