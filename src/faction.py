class Faction:
    def __init__(self, name: str, num: int, power: int=0, rgb=(255, 255, 255)):
        self.name = name
        self.power = power
        self.rgb = rgb

        if num <= 0:
            raise ValueError(f"Invalid numerical identifier '{num}', use 1 or higher")

        if not isinstance(num, int):
            raise TypeError(f"Numerical identifier must be int, not {type(num).__name__}")

        self.num = num


class NoFaction(Faction):
    def __init__(self):
        self.name = "No Faction"
        self.num = 0
        self.rgb = (0, 255, 255)
