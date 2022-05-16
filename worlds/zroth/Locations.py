
from .Constant import GAMENAME

from BaseClasses import Location


class ZrothLocation(Location):
    game: str = GAMENAME

    def __init__(self, player: int, name: str = '', address: int = None, parent=None):
        super(ZrothLocation, self).__init__(player, name, address, parent)
        self.event = address is None


# data used below to add items to the World


Zroth_locations = {
    "POH00": {"WoodD5": lambda state, player: state._Zroth_can_rodHook(player)},
    "POH01": {"WoodUp": lambda state, player: state.has("HookShot", player)},
    "POH02": {"Wood": lambda state, player: state._Zroth_can_bush(player)},
    "POH03": {"WoodBottom": None},
    "POH04": {"Gutter": None},
    "POH05": {"KakLedge": None},
    "POH06": {"KakBack": None},
    "POH07": {"Lake": lambda state, player: state._Zroth_can_swim(player)},
    "POH08": {"D2Island": lambda state, player: state.has("HookShot", player)},
    "POH09": {"Lake": None},
    "POH10": {"Desert": lambda state, player: state.has("Hammer", player)},
    "POH11": {"Gutter": None},
    "POH12": {"FieldLedge": lambda state, player: state._Zroth_can_bushHook(player)},
    "POH13": {"MntBack": None},
    "POH14": {"MntRight": lambda state, player: state.has("Hammer", player)},
    "POH15": {"Desert": None},
    "POH16": {"Desert": None},
    "POH17": {"Desert": None},
    "POH18": {"Desert": None},
    "POH19": {"GerLedge": None},
    "POH20": {"Gutter": None},
    "POH21": {"Shadow": lambda state, player: state.has("Hammer", player)},
    "POH22": {"TurtleTop": None},
    "POH23": {
        "Land":
        lambda state, player: (
            state._Zroth_can_rodHook(player)
            and
            state._Zroth_can_bush(player)
            and
            state._Zroth_can_rock(player, 2)
            and
            state.has("Hammer", player)
        )
    },
    "POH24": {
        "Lake":
        lambda state, player: (
            state._Zroth_can_swim(player)
            and
            state._Zroth_can_rock(player, 2)
        )
    },
    "POH25": {"D2Cave": lambda state, player: state.has("HookShot", player)},
    "POH26": {"MonsterHouse": lambda state, player: state._Zroth_has_monster(player, 1)},
    "POH27": {"MonsterHouse": lambda state, player: state._Zroth_has_monster(player, 2)},
    "POH28": {"MonsterHouse": lambda state, player: state._Zroth_has_monster(player, 3)},
    "POH29": {"MonsterHouse": lambda state, player: state._Zroth_has_monster(player, 4)},
    "POH30": {"MonsterHouse": lambda state, player: state._Zroth_has_monster(player, 5)},
    "POH31": {"MonsterHouse": lambda state, player: state._Zroth_has_monster(player, 6)},
    # Game
    "POH32": {"Kak": lambda state, player: state._Zroth_can_amunition(player)},
    "POH33": {"Kak": None},  # Tavern
    # Games
    "POH34": {"Desert": lambda state, player: state._Zroth_can_amunition(player)},
    "POH35": {
        "Shadow":
        lambda state, player: (
            state._Zroth_can_amunition(player)
            and
            state.has("Book", player)
        )},

    "Shield": {"LinksHouse": None},
    "Sword1": {"Wood": None},
    "Medalion2": {"WoodD5": lambda state, player: state._Zroth_can_bomb(player)},
    "Medalion1": {
        "Desert":
        lambda state, player: (
            state._Zroth_can_rock(player, 2)
            and
            state._Zroth_can_bomb(player)
        )
    },
    "Bottle2": {"Desert": lambda state, player: state._Zroth_can_amunition(player)},
    "Sword2": {
        "Smith":
        lambda state, player: (
            state._Zroth_has_crystals(player, 3)
            and
            state.has_group("Swords", player)
        )
    },
    "Glove2": {
        "Smith":
        lambda state, player: (
            state._Zroth_has_crystals(player, 7)
            and
            state.has("Gloves", player)
        )
    },
    "Bow2": {
        "Smith":
        lambda state, player: (
            state._Zroth_has_crystals(player, 3)
            and
            state.has("Bow", player)
        )
    },
    "Bottle1": {"Kak": lambda state, player: state._Zroth_can_amunition(player)},
    "Bow": {"Kak": lambda state, player: state._Zroth_can_amunition(player)},
    "Medalion3": {
        "Lake":
        lambda state, player: (
            state._Zroth_can_icerod(player)
            and
            state._Zroth_can_bomb(player)
        )
    },
    "Bottle3": {"Shadow": lambda state, player: state._Zroth_can_amunition(player)},
    "Book": {"BookCave": None},
    "DoubleMagic": {
        "Land":
        lambda state, player: (
            state._Zroth_can_bomb(player)
            and
            state._Zroth_can_rock(player, 2)
        )
    },

    "D1Map": {"D1": None},
    "D1Compass": {"D1": lambda state, player: state._Zroth_has_Dkey(player, 1, 3)},
    "D1K1": {"D1E2": lambda state, player: state._Zroth_can_bomb(player)},
    "D1K2": {"D1": None},
    "D1K3": {"D1": None},
    "D1Boss": {
        "D1":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 1, 2)
            and
            state._Zroth_can_rock(player, 1)
        )
    },
    "D1Object": {
        "D1":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 1, 3)
        )
    },
    "D1Crystal": {
        "D1":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 1)
            and
            state._Zroth_can_rock(player, 1)
        )
    },

    "D2Map": {"D2": None},
    "D2Compass": {"D2": None},
    "D2K1": {
        "D2":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 2, 4)
            and
            (
                (
                    state._Zroth_can_rock(player, 1)
                    and
                    state._Zroth_can_sphere(player)
                )
                or
                state._Zroth_can_water(player)
                or
                state.has("HookShoot", player)
            )
        )
    },
    "D2K2": {  # ToDo:Check again
        "D2":
        lambda state, player: (
            (
                state._Zroth_has_Dkey(player, 2, 4)
                and
                (
                    (
                        state._Zroth_can_rock(player, 1)
                        and
                        state._Zroth_can_sphere(player)
                    )
                    or
                    state._Zroth_can_water(player)
                    or
                    state.has("HookShot", player)
                )
            )
            or
            (
                state._Zroth_has_Dkey(player, 2, 3)
                and
                state._Zroth_can_water(player)
                and
                state._Zroth_can_sphere(player)
            )
        )
    },
    "D2K3": {
        "D2":
        lambda state, player: (
            state._Zroth_can_water(player)
            or
            state.has("HookShot", player)
        )
    },
    "D2K4": {
        "D2":
        lambda state, player: (
            state._Zroth_can_water(player)
            or
            state.has("HookShot", player)
        )
    },
    "D2K5": {
        "D2":
        lambda state, player: (
            (
                state._Zroth_has_Dkey(player, 2, 5)
                and
                state.has("HookShot", player)
            ) or (
                state._Zroth_can_rock(player, 1)
                and
                state._Zroth_can_sphere(player)
            ) or
            state._Zroth_can_water(player)
        )
    },
    "D2Boss": {
        "D2":
        lambda state, player: (
            (
                state.has("Hookshot", player)
                and
                (
                    state._Zroth_has_Dkey(player, 2, 5)
                    or
                    state._Zroth_can_rock(player, 1)
                )
            ) or
            state._Zroth_can_water(player)
        )
    },
    "D2Object": {
        "D2":
        lambda state, player: (
            (
                state._Zroth_has_Dkey(player, 2, 5)
                and
                (
                    state._Zroth_can_bomb(player)
                    or
                    (
                        state._Zroth_can_icerod(player)
                        or
                        state._Zroth_can_firerod(player)
                    )
                )
                and
                (
                    state.has("HookShoot", player)
                    or
                    (
                        state._Zroth_can_rock(player, 1)
                        and
                        state._Zroth_can_sphere(player)
                    )
                )
            ) or
            state._Zroth_can_water(player)
        )
    },
    "D2Crystal": {
        "D2":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 2)
            and
            state._Zroth_can_damage(player)
        )
    },

    "D3Map": {"D3": None},
    "D3Compass": {"D3": None},
    "D3K1": {"D3": lambda state, player: state._Zroth_can_fire(player)},
    "D3K2": {"D3": None},
    "D3K3": {"D3": None},
    "D3K4": {"D3": None},
    "D3K5": {"D3": None},
    "D3Boss": {
        "D3":
        lambda state, player: (
            state._Zroth_can_firerod(player)
            or
            (
                state._Zroth_has_Dkey(player, 3, 5)
                and
                state._Zroth_can_bomb(player)
                and
                state._Zroth_can_fire(player)
            )
        )
    },
    "D3Object": {
        "D3":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 3, 5)
            and
            state.has("HookShot", player)
        )
    },
    "D3Crystal": {
        "D3":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 3)
            and
            state._Zroth_can_damage(player)
        )
    },

    "D4Map": {"D4": lambda state, player: state._Zroth_can_fire(player)},
    "D4Compass": {"D4": lambda state, player: state._Zroth_can_fire(player)},
    "D4K1": {"D4": lambda state, player: state._Zroth_can_reflect(player)},
    "D4K2": {
        "D4":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 4, 2)
            and
            state._Zroth_can_fire(player)
        )
    },
    "D4K3": {
        "D4":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 4, 1)
            and
            state._Zroth_can_reflect(player)
        )
    },
    "D4Boss": {
        "D4":
        lambda state, player: (
            state._Zroth_can_water(player)
            and
            state._Zroth_can_damage(player)
        )
    },
    "D4Object": {
        "D4":
        lambda state, player: (
            (
                state._Zroth_has_Dkey(player, 4, 3)
                and
                state._Zroth_can_fire(player)
            )
            or
            (
                state._Zroth_can_water(player)
                and
                state._Zroth_can_reflect(player)
            )
        )
    },
    "D4Crystal": {
        "D4":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 4)
            and
            state._Zroth_can_reflect(player)
        )
    },

    "D5Map": {"D5": None},
    "D5Compass": {"D5": None},
    "D5K1": {"D5P2": None},
    "D5Boss": {
        "D5":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 5, 1)
            and
            state._Zroth_can_bow(player)
            and
            state.has("Hammer", player)
        )
    },
    "D5Object": {"D5": lambda state, player: state._Zroth_can_remote(player)},
    "D5Crystal": {
        "D5":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 5)
            and
            state._Zroth_can_damage(player)
        )
    },

    "D6Map": {"D6Ent": lambda state, player: state._Zroth_can_damage(player)},
    "D6Compass": {"D6Ent": lambda state, player: state._Zroth_can_damage(player)},
    "D6K1": {"D6": lambda state, player: state._Zroth_can_firerod(player)},
    "D6K2": {
        "D6":
        lambda state, player: (
            state._Zroth_can_firerod(player)
            and
            state.has("HookShot", player)
        )
    },
    "D6K3": {
        "D6":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 6, 1)
            and
            state._Zroth_can_firerod(player)
        )
    },
    "D6Boss": {
        "D6":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 6, 3)
            and
            state._Zroth_can_firerod(player)
        )
    },
    "D6Object": {
        "D6":
        lambda state, player: (
            state._Zroth_can_bow(player)
            and
            state._Zroth_can_reflect(player)
        )
    },
    "D6Crystal": {
        "D6":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 6)
            and
            state._Zroth_can_damage(player)
        )
    },

    "D7Map": {"D7": lambda state, player: state._Zroth_can_damage(player)},
    "D7Compass": {
        "D7":
        lambda state, player: (
            state._Zroth_can_damage(player)
            and
            state.has("HookShot", player)
        )
    },
    "D7K1": {
        "D7":
        lambda state, player: (
            state._Zroth_can_damage(player)
            and
            state._Zroth_can_bomb(player)
            and
            state.has("HookShot", player)
        )
    },
    "D7K2": {
        "D7":
        lambda state, player: (
            state._Zroth_can_damage(player)
            and
            state._Zroth_can_icerod(player)
        )
    },
    "D7Boss": {
        "D7":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 7, 2)
            and
            state._Zroth_can_damage(player)
            and
            state._Zroth_can_icerod(player)
        )
    },
    "D7Object": {
        "D7":
        lambda state, player: (
            state._Zroth_can_damage(player)
            and
            (
                state._Zroth_can_icerod(player)
                or
                state._Zroth_has_Dkey(player, 7, 1)
            )
        )
    },
    "D7Crystal": {
        "D7":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 7)
            and
            state._Zroth_can_damage(player)
        )
    },

    "D8Map": {"D8": None},
    "D8Compass": {"D8": lambda state, player: state._Zroth_has_Dkey(player, 8, 1)},
    "D8K1": {
        "D8":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 8, 1)
            and
            state._Zroth_can_damage(player)
        )
    },
    "D8K2": {"D8": lambda state, player: state._Zroth_can_damage(player)},
    "D8Boss": {
        "D8":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 8, 2)
            and
            state._Zroth_can_damage(player)
        )
    },
    "MSword": {
        "D8":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 8, 1)
            and
            state._Zroth_has_Bkey(player, 8)
            and
            state._Zroth_can_damage(player)
            and
            state.has("Hammer", player)
        )
    },

    "D9Map": {"D9": None},
    "D9Compass": {
        "D9":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 9, 2)
        )
    },
    "D9K1": {
        "D9":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 9, 1)
            and
            state._Zroth_can_damage(player)
        )
    },
    "D9K2": {"D9": lambda state, player: state._Zroth_can_damage(player)},
    "D9K3": {
        "D9":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 9, 2)
            and
            state._Zroth_can_damage(player)
        )
    },
    "D9K4": {
        "D9":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 9, 3)
            and
            state._Zroth_can_damage(player)
        )
    },
    "D9Boss": {
        "D9":
        lambda state, player: (
            state._Zroth_has_Dkey(player, 9, 4)
            and
            state._Zroth_can_sphere(player)
        )
    },
    "Triforce": {
        "D9Top":
        lambda state, player: (
            state._Zroth_has_Bkey(player, 9)
            and
            state._Zroth_can_advDamage(player)
        )
    },
}
