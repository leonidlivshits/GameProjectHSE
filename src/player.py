from typing import Dict


class Player:
    # Класс, представляющий состояние игрока.

    # Атрибуты:
    #   name (str): имя игрока
    #   health (int): здоровье
    #   karma (int): карма
    #   luck (int): удача
    #   p (int): опыт


    def __init__(self, name: str = "Игрок"):
        self.name: str = name
        self.health: int = 20
        self.karma: int = 0
        self.luck: int = 0
        self.xp: int = 0

    def apply_effects(self, effects: Dict[str, int]):
        if not effects:
            return
        if "health" in effects:
            self.health += int(effects["health"])
        if "karma" in effects:
            self.karma += int(effects["karma"])
        if "luck" in effects:
            self.luck += int(effects["luck"])
        if "xp" in effects:
            self.xp += int(effects["xp"])

    def is_alive(self) -> bool:
        return self.health > 0

    def summary(self) -> Dict[str, int]:
        return {
            "name": self.name,
            "health": self.health,
            "karma": self.karma,
            "luck": self.luck,
            "xp": self.xp,
        }

    def __repr__(self) -> str:
        return (
            f"Player(name={self.name!r}, health={self.health}, karma={self.karma}, "
            f"luck={self.luck}, xp={self.xp})"
        )
