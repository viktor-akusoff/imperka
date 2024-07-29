from pymongo import MongoClient
from app.core.config import settings
        
db = MongoClient(settings.mongodb_url)[settings.mongodb_db]