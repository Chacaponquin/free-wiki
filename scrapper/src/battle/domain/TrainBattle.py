import datetime
from isodate import Duration


class TrainBattle:
    def __init__(
            self,
            title: str,
            image: str,
            date: datetime.datetime,
            channel: str,
            duration: Duration,
            rapper_name: str,
            views: int
    ):
        self.title = title
        self.image = image
        self.date = date
        self.channel = channel
        self.is_battle = False
        self.duration = duration
        self.rapper_name = rapper_name
        self.views = views

    def to_dict(self):
        return {
            'title': self.title,
            'image': self.image,
            'date': self.date.__str__(),
            'channel': self.channel,
            'is_battle': False,
            'duration': self.duration.__str__(),
            'rapper': self.rapper_name,
            'views': self.views
        }
