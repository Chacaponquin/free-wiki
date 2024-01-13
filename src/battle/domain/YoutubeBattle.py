import datetime
from isodate import Duration


class YoutubeBattle:
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def __init__(
            self,
            battle_id: str,
            title: str,
            image: str,
            date: str,
            channel_id: str,
            channel: str,
            tags: list[str],
            duration: Duration,
            rapper_name: str,
            views: int
    ):
        self.battle_id = battle_id
        self.title = title
        self.image = image
        self.date = datetime.datetime.strptime(date, self.DATE_FORMAT)
        self.channel_id = channel_id
        self.channel = channel
        self.tags = tags
        self.duration = duration
        self.rapper_name = rapper_name
        self.views = views
