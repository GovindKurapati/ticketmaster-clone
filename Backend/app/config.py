import os
from dotenv import load_dotenv

# Loading environment variables from a .env file into the program's environment
load_dotenv()


# Retrieves the database URL from an environment variable for security
class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")


# Creating an instance of Settings to access configuration variables
settings = Settings()
