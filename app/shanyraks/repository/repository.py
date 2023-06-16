from typing import Optional, Any

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult

class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database
        
    def create_shanyrak(self, user_id: str, data: dict[str, Any]):
        data["user_id"] = ObjectID[user_id]
        shanyrak = self.database["shanyraks"].insert_one(data)
        return shanyrak.inserted_id
    
    def get_shanyrak(self, shanyrak_id: str):
        return self.database["shanyraks"].find_one({"_id": ObjectID(shanyrak_id)})
    
    def update_shanyrak(self, shanyrak_id: str, user_id: str, data: dict[str, Any]):
        return self.database["users"].update_one(
            filter={"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)},
            update={
                "$set": data,
            },
        )
    
    def delete_shanyrak(self, shanyrak_id: str, user_id: str) -> DeleteResult:
        return self.database["users"].delete_one("_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id))