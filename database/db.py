import motor.motor_asyncio
from config import DB_URI, DB_NAME

class Database慕

System: I notice you mentioned wanting to create a "Save-Restricted-Content-Bot" that forwards content from private Telegram channels with restricted copy and forward options to your own channel, supporting large files (>2GB). You've shared a pre-built repository, and I’ve analyzed the code to address your requirements, fix existing issues (like the MongoDB connection error), and enhance the bot’s functionality. However, your message was cut off at the end of the `db.py` file, and it seems you were about to provide additional details or code. I’ll proceed with the analysis and provide a complete solution based on what you’ve shared, integrating the requirements and fixing the issues. If you have more code or details to share, please provide them, and I can refine the solution further.

---

### Updated Code (Continued)

#### 2. `database/db.py` (Completed)
Below is the completed and updated `db.py` file, ensuring compatibility with the new MongoDB URI and maintaining the existing functionality.

<xaiArtifact artifact_id="0a3a5dd7-d1fe-4b52-b61c-372131e754fd" artifact_version_id="634fbee1-039b-4284-afa0-4f3a5ff6036a" title="db.py" contentType="text/python">
import motor.motor_asyncio
from config import DB_URI, DB_NAME

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id, name):
        return dict(
            id=id,
            name=name,
            session=None,
        )
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)
    
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_session(self, id, session):
        await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})

    async def get_session(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('session') if user else None

db = Database(DB_URI, DB_NAME)
