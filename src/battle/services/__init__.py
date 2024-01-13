import json

from src.battle.domain import YoutubeBattle, TrainBattle
from src.battle.infra.mongo import BattleMongoRepository
from src.battle.dto import CreateBattleDTO, UpdateOldBattle


class BattleServices:
    repository = BattleMongoRepository()

    async def find_by_title(self, title: str):
        return await self.repository.find_by_title(title)

    async def create_battle(self, data: CreateBattleDTO):
        await self.repository.create(data)

    async def update_old_battle(self, battle_id: str, data: UpdateOldBattle):
        await self.repository.update_old_battle(
            battle_id=battle_id,
            data=data
        )

    def save_train_battles(self, battles: list[YoutubeBattle]):
        all_train_battles: list[TrainBattle] = []
        for battle in battles:
            new_train_battle = TrainBattle(
                title=battle.title,
                image=battle.image,
                date=battle.date,
                channel=battle.channel,
                duration=battle.duration,
                rapper_name=battle.rapper_name,
                views=battle.views
            )

            all_train_battles.append(new_train_battle)

        with open('src/battle/infra/train.json', 'w', encoding='utf-8') as outfile:
            dict_list = list(map(lambda x: x.to_dict(), all_train_battles))
            json.dump(dict_list, outfile, indent=3)
