# Ticketmaster Clone

This is the project for Database organisation CS-425-02, built using **FastAPI**, **SQLModel**, and **Alembic**. For now all the crud operations are developed for the project.

## Project Setup

Please follow the instructions below to set up and run the project locally.

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

Navigate to the project directory and start the server:

```bash
cd Backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
uvicorn app.main:app --reload --port 8080
```

### 7. Access the API Documentation

Once the application is running, you can access the API documentation using Swagger UI at the following URL: http://localhost:8000/docs
