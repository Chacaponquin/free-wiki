class UpdateOldBattle:
    def __init__(
            self,
            channel_id: str,
            tags: list[str],
            video_id: str
    ):
        self.channel_id = channel_id
        self.tags = tags
        self.video_id = video_id


class CreateBattleDTO:
    def __init__(
            self,
            battle_id: str,
            title: str,
            image: str,
            date: str,
            channel_id: str,
            channel: str,
            tags: list[str],
            duration: str,
            rapper_name: str,
            views: str
    ):
        self.battle_id: str = battle_id
        self.title: str = title
        self.image: str = image
        self.date: str = date
        self.channel_id: str = channel_id
        self.channel: str = channel
        self.tags: list[str] = tags
        self.duration: str = duration
        self.rapper_name: str = rapper_name
        self.views: str = views
