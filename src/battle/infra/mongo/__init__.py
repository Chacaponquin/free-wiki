from bson import ObjectId

from src.battle.domain import Battle
from src.app.infrastructure.mongo import battle_collection
from src.battle.dto import CreateBattleDTO, UpdateOldBattle


class BattleMongoRepository:
    battle_collection = battle_collection

    async def get_all(self) -> list[Battle]:
        mongo_data = await self.battle_collection.find(None)
        battles = list(map(lambda b: self._map(b), mongo_data))
        return battles

    async def update_old_battle(self, battle_id: str, data: UpdateOldBattle):
        update = await self.battle_collection.find_one_and_update(
            {
                '_id': ObjectId(battle_id)
            },
            {
                '$set': {
                    'channel_id': data.channel_id,
                    'tags': data.tags,
                    'video_id': data.video_id
                }
            }
        )

    async def create(self, data: CreateBattleDTO):
        await self.battle_collection.insert_one({
            'video_id': data.battle_id,
            'title': data.title,
            'image': data.image,
            'date': data.date,
            'channel_id': data.channel_id,
            'channel': data.channel,
            'tags': data.tags,
            'duration': data.duration,
            'rapper': data.rapper_name,
            'views': data.views,
            'evaluated': False,
            'is_battle': False
        })

    async def find_by_title(self, title: str) -> Battle | None:
        found = await self.battle_collection.find_one({'title': title})

        if found is None:
            return None
        else:
            return found

    def _map(self, document: dict) -> Battle:
        video_id: str = document['video_id']
        title: str = document['title']
        image: str = document['image']
        date: str = document['date']
        channel_id: str = document['channel_id']
        channel: str = document['channel']
        tags: list[str] = document['tags']
        duration: str = document['duration']
        rapper_name: str = document['rapper']
        views: str = document['views']
        evaluated: bool = document['evaluated']
        id: str = str(document['_id'])

        return Battle(
            video_id=video_id,
            title=title,
            image=image,
            date=date,
            channel=channel,
            channel_id=channel_id,
            tags=tags,
            duration=duration,
            rapper_name=rapper_name,
            views=views,
            evaluated=evaluated,
            id=id
        )