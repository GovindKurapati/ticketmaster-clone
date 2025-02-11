# React + Vite

## Prerequisites

Before you begin, ensure you have the following installed:

1. Node.js (v14 or higher)
2. npm

## Installation

Navigate to the project directory:

```bash
cd Frontend
```

Install dependencies:
Using npm:

```bash
npm install
```

### Running the Application

To start the development server:

```bash
npm run dev
```

The application will be available at [http://localhost:5173/](http://localhost:5173/)

## Project Structure

```text
frontend/
├── public/ # Public assets (index.html, images, etc.)
├── src/
│ ├── components/            # Reusable components (EventCard, Header, etc.)
│ ├── pages/                 # Pages (Home, Login, Signup)
│ ├── store/                 # Zustand stores for state management
│ ├── api/                   # Axios instance for API calls
│ ├── App.jsx                # Main app component
│ └── main.jsx               # Entry point for React app
└── package.json             # Project configuration and dependencies
```
