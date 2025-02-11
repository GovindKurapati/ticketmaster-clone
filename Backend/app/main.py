# Importing necessary modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from app.api import router as api_router
from contextlib import asynccontextmanager


# Defining an async context manager to manage the app's lifespan and initializing DB tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # Setting up database tables when the app starts
    yield


# Configuring FastAPI application with title and description for API documentation
app = FastAPI(
    lifespan=lifespan,
    title="Ticket Master Clone",
    description="API documentation for ticket master",
)

# Defining CORS origins for frontend communication (allows frontend to access API)
origins = ["http://localhost:3000", "http://localhost:5173"]  # for frontend origin

# Adding CORS middleware to enable cross-origin resource sharing for specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including the API router, which contains the actual API endpoints
app.include_router(api_router)
