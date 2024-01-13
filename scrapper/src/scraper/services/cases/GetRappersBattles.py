import requests
import isodate
import time

from isodate import Duration
from src.rapper.services import RapperServices
from src.battle.services import BattleServices
from src.battle.dto import CreateBattleDTO, UpdateOldBattle


class RapperBattles:
    def __init__(self, rapper_name: str):
        self.battles = []
        self.rapper_name = rapper_name


class GetRappersBattles:
    LIMIT_PAGES = 5

    SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
    FIND_URL = 'https://www.googleapis.com/youtube/v3/videos'
    API_KEYS = ['AIzaSyAcBR9mdhaOjh_R2j5cwNyjXP0ZtzvBIPM', 'AIzaSyA_UYCizEB-1hdtN_rVrTxLLT2uNfAvWA4']
    ACTUAL_KEY = 0

    def __init__(self, rapper_services: RapperServices, battle_services: BattleServices):
        self.rapper_services = rapper_services
        self.battle_services = battle_services

    def _change_api_key(self) -> bool:
        if self.ACTUAL_KEY == len(self.API_KEYS) - 1:
            return True
        else:
            self.ACTUAL_KEY += 1
            return False

    def _make_search_battle_name(self, name: str) -> str:
        return f'Freestyle {name} vs'

    def _check_exists_battle(self, all_rappers_battles: list[RapperBattles], battle_id: str):
        exists = False

        it = 0
        while not exists and it < len(all_rappers_battles):
            for b_id in all_rappers_battles[it].battles:
                if b_id == battle_id:
                    exists = True
                    break

            it += 1

        return exists

    async def execute(self):
        all_rappers_battles: list[RapperBattles] = []
        rappers = self.rapper_services.get_rappers_names()

        for rapper in rappers:
            new_rapper_date = RapperBattles(rapper_name=rapper)
            rapper_battle_count = 0

            keys = ['id', 'snippet']

            it = 1
            next_page = None
            stop = False

            while it <= self.LIMIT_PAGES and not stop:
                params = {
                    'key': self.API_KEYS[self.ACTUAL_KEY],
                    'q': self._make_search_battle_name(rapper),
                    'part': ','.join(keys),
                    'maxResults': 100,
                    'pageToken': next_page
                }

                try:
                    response = requests.get(self.SEARCH_URL, params=params)
                    result = response.json()

                    if response.status_code >= 400:
                        stop = self._change_api_key()
                        continue

                    for item in result['items']:
                        item_id = item['id']['videoId']
                        if not self._check_exists_battle(all_rappers_battles, item_id):
                            new_rapper_date.battles.append(item_id)
                            rapper_battle_count += 1

                    next_page = result['nextPageToken']
                    it += 1
                except:
                    it += 1

            all_rappers_battles.append(new_rapper_date)

            print(f'{rapper}: {rapper_battle_count} batallas')

        print(f'\n')

        battle_index = 1
        for rapper_data in all_rappers_battles:
            for battle_id in rapper_data.battles:
                print(f'{battle_index} Buscando batalla {battle_id}...')
                keys = ['id', 'snippet', 'contentDetails', 'statistics']

                params = {
                    'key': self.API_KEYS[self.ACTUAL_KEY],
                    'part': ','.join(keys),
                    'id': battle_id
                }

                try:
                    response = requests.get(self.FIND_URL, params=params)
                    result = response.json()

                    if response.status_code >= 400:
                        if self._change_api_key():
                            break

                    for item in result['items']:
                        battle_data = item['snippet']

                        title = battle_data['title']
                        image = battle_data['thumbnails']['default']['url']
                        date = battle_data['publishedAt']
                        channel_id = battle_data['channelId']
                        channel = battle_data['channelTitle']
                        tags = []
                        duration: Duration = isodate.parse_duration(item['contentDetails']['duration'])
                        views = item['statistics']['viewCount']

                        found = await self.battle_services.find_by_title(title)
                        if found is None:
                            new_battle_dto = CreateBattleDTO(
                                battle_id=battle_id,
                                rapper_name=rapper_data.rapper_name,
                                tags=tags,
                                duration=str(duration),
                                views=views,
                                image=image,
                                date=date,
                                title=title,
                                channel=channel,
                                channel_id=channel_id
                            )

                            await self.battle_services.create_battle(new_battle_dto)
                        else:
                            update_dto = UpdateOldBattle(
                                channel_id=channel_id,
                                tags=tags,
                                video_id=battle_id
                            )

                            await self.battle_services.update_old_battle(
                                battle_id=str(found['_id']),
                                data=update_dto
                            )

                        battle_index += 1
                        time.sleep(0.1)
                except:
                    battle_index += 1
                    continue
