import datetime


class Battle:
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    DURATION_FORMAT = "%H:%M:%S"

    def __init__(
            self,
            video_id: str,
            id: str,
            title: str,
            image: str,
            date: str,
            channel_id: str,
            channel: str,
            tags: list[str],
            duration: str,
            rapper_name: str,
            views: str,
            evaluated: bool
    ):
        self.video_id = video_id
        self.title = title
        self.image = image
        self.date = datetime.datetime.strptime(date, self.DATE_FORMAT)
        self.channel_id = channel_id
        self.channel = channel
        self.tags = tags
        self.duration = datetime.datetime.strptime(duration, self.DURATION_FORMAT)
        self.rapper_name = rapper_name
        self.views = int(views)
        self.evaluated = evaluated
        self.id = id
