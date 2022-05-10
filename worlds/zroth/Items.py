from .Constant import GAMENAME
from BaseClasses import Item


class ZrothItem (Item):
    game: str = GAMENAME


Zroth_other = {
    "POH": 36,
    "Bottle": 3,
    "Shield": 1,
    "MagicUpgrade": 1,
    "MapD1": 1,
    "MapD2": 1,
    "MapD3": 1,
    "MapD4": 1,
    "MapD5": 1,
    "MapD6": 1,
    "MapD7": 1,
    "MapD8": 1,
    "MapD9": 1,
    "CompassD1": 1,
    "CompassD2": 1,
    "CompassD3": 1,
    "CompassD4": 1,
    "CompassD5": 1,
    "CompassD6": 1,
    "CompassD7": 1,
    "CompassD8": 1,
    "CompassD9": 1,
    "Medalion1": 1,
    "Medalion2": 1,
    "Medalion3": 1
}

Zroth_progress = {
    "ProgressiveSword": 2,
    "MasterSword": 0,
    "Gloves": 2,
    "Bow": 2,
    "Flipper": 1,
    "Hammer": 1,
    "Lamp": 1,
    "Hookshot": 1,
    "FireRod": 1,
    "IceRod": 1,
    "Book": 1,
    "BossKeyD1": 1,
    "BossKeyD2": 1,
    "BossKeyD3": 1,
    "BossKeyD4": 1,
    "BossKeyD5": 1,
    "BossKeyD6": 1,
    "BossKeyD7": 1,
    "BossKeyD8": 1,
    "BossKeyD9": 1,
    "SmallKeyD1": 3,
    "SmallKeyD2": 5,
    "SmallKeyD3": 5,
    "SmallKeyD4": 3,
    "SmallKeyD5": 1,
    "SmallKeyD6": 3,
    "SmallKeyD7": 2,
    "SmallKeyD8": 2,
    "SmallKeyD9": 4,
    "D1Crystal": 0,
    "D2Crystal": 0,
    "D3Crystal": 0,
    "D4Crystal": 0,
    "D5Crystal": 0,
    "D6Crystal": 0,
    "D7Crystal": 0,
    "Triforce": 0
}

Zroth_items = Zroth_other.copy()
Zroth_items.update(Zroth_progress)
