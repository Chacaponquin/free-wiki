from src.rapper.domain import Rapper


class RapperServices:
    def get_all(self) -> list[Rapper]:
        all_rappers: list[Rapper] = [
            Rapper(name='Chuty'),
            Rapper(name='Mecha'),
            Rapper(name='Azcino'),
            Rapper(name='Arkano'),
            Rapper(name='Papo'),
            Rapper(name='Wos'),
            Rapper(name='Sweet Pain'),
            Rapper(name='Trueno'),
            Rapper(name='Teorema'),
            Rapper(name='Zasko'),
            Rapper(name='Gazir'),
            Rapper(name='Dtoke'),
            Rapper(name='Stuart')
        ]

        return all_rappers

    def get_rappers_names(self) -> list[str]:
        return list(map(lambda x: x.name, self.get_all()))
