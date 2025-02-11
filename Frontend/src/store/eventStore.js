// src/store/eventStore.js
import { create } from "zustand";
import api from "../api/api"; // Import Axios instance

const useEventStore = create((set) => ({
  event: [],
  loading: false,
  error: null,

  // Fetch all events
  fetchAllEvents: async () => {
    set({ loading: true, error: null });
    try {
      const response = await api.get("/events"); // Replace with your actual endpoint
      set({ events: response.data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  // Fetch events by category ID
  fetchEventsByCategoryId: async (categoryId) => {
    set({ loading: true, error: null });
    try {
      const response = await api.get(`/events/byCategory/${categoryId}`); // Replace with actual endpoint
      set({ events: response.data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  // Fetch events by user ID
  fetchEventsByUserId: async (userId) => {
    set({ loading: true, error: null });
    try {
      const response = await api.get(`/events/user/${userId}`); // Replace with actual endpoint
      set({ events: response.data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  // Fetch event details from the API
  fetchEventDetails: async (eventId) => {
    set({ loading: true, error: null });
    try {
      const response = await api.get(`/events/${eventId}`); // Replace with actual endpoint
      set({ event: response.data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
}));

export default useEventStore;
