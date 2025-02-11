# Ticketmaster Clone

This is the project for Database organisation CS-425-02, built using **FastAPI**, **SQLModel**, and **Alembic**. For now all the crud operations are developed for the project.

![ticketmaster clone demo](./project-image.png "Project Image")

## Project Setup

Please follow the instructions below to set up and run the project locally.

## Backend

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 1. Create a Virtual Environment

To create a virtual environment, navigate to the project directory in your terminal and run:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

- On Windows:

```bash
venv\Scripts\activate
```

- On linux or macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 4. Create the .env File

Create a <code>.env</code> file in the backend directory project. This file will hold the environment variables. You can create the file using a text editor or by running:

```bash
touch .env
```

### 5. Configure the .env File

Add the following lines to the <code>.env</code> file to connect to the database:

```makefile
DATABASE_URL=<actual database url(e.g.-mysql+pymysql://username:password@host:port/database)>
```

### 6. Start the Application

To start the application, use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 7. Access the API Documentation

Once the application is running, you can access the API documentation using Swagger UI at the following URL: [http://localhost:8000/docs](http://localhost:8000/docs)

---

# Frontend

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

Loom recording - [https://www.loom.com/share/e7563e01ea334653aec65a8f1791bb3d](Loom recording - https://www.loom.com/share/e7563e01ea334653aec65a8f1791bb3d)
