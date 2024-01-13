from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URL = "mongodb://localhost:27017"
mongo_client = AsyncIOMotorClient(MONGO_URL)

database = mongo_client['Free-Wiki']

battle_collection = database.get_collection('battle')
