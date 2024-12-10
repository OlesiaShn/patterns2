import os
from dotenv import load_dotenv

load_dotenv()

TRANSLATE_API_KEY = "f5bb25c4demsh778a9ae6ac69ae6p130307jsn9c9140450c2a"
MONGODB_HOST="localhost"
MONGODB_PORT=27017
MONGO_DATABASE="googletranslate_api"
MONGODB_USERNAME="olesia"
MONGODB_PASSWORD="olesia"
MONGODB_URL = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGO_DATABASE}" \
              f"?authSource=admin"