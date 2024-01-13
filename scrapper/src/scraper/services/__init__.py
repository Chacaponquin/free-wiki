from src.scraper.services.cases import GetRappersBattles
from src.rapper.services import RapperServices
from src.battle.services import BattleServices


class ScraperServices:
    rapper_services = RapperServices()
    battle_services = BattleServices()

    def get_rapper_battles(self, name: str) -> list:
        return []

    async def get_all_rappers_battles(self):
        case = GetRappersBattles(
            rapper_services=self.rapper_services,
            battle_services=self.battle_services
        )

        await case.execute()

        # self.battle_services.save_train_battles(battles)
