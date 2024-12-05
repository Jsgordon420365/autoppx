# ver 20241205113000.1
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch MongoDB connection string from environment variable
CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")

def test_mongo_connection():
    try:
        client = MongoClient(CONNECTION_STRING)
        db = client.test  # Test database
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

if __name__ == "__main__":
    test_mongo_connection()
