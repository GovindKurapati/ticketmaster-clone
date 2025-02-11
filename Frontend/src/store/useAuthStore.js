// src/store/eventStore.js
import { create } from "zustand";
import api from "../api/api"; // Import Axios instance

const useAuthStore = create((set) => ({
  user: null,
  loading: false,
  error: null,

  // Signup action
  signup: async (signupData) => {
    set({ loading: true, error: null });
    try {
      const response = await api.post("/users/", signupData); // Replace with your actual signup endpoint
      set({ user: response.data, loading: false });
      return response.data; // Return data on success
    } catch (error) {
      set({
        error: error.response?.data?.message || "Signup failed",
        loading: false,
      });
      throw error;
    }
  },

  // Login action
  login: async (loginData) => {
    set({ loading: true, error: null });
    try {
      const response = await api.post("/login", null, {
        params: {
          email: loginData.email,
          password: loginData.password,
        },
      }); // Replace with your actual login endpoint
      set({ user: response.data, loading: false });
      return response.data; // Return data on success
    } catch (error) {
      set({
        error: error.response?.data?.message || "Login failed",
        loading: false,
      });
      throw error;
    }
  },

  // Logout action
  logout: () => {
    set({ user: 0 });

    // Optionally, clear tokens or session data here
  },
}));

export default useAuthStore;
