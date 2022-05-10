Zroth_regions: dict[str, dict[str, tuple[str, any]]] = {
    "Menu": {"NewGame": ("LinksHouse", None)},
    "LinksHouse": {"LinksExit": ("Wood", None)},
    "Wood": {
        "WoodExit": (
            "Field",
            lambda state, player: state._Zroth_can_rock(player, 1)
        ),
        "D1Ent1": (
            "D1",
            lambda state, player: state._Zroth_can_bush(player)
        )
    },
    "WoodUp": {
        "D1Ent2": ("D1E2", None),
        "FromUpToWood": (
            "Wood",
            lambda state, player: state.has("HookShot", player)
        )
    },
    "WoodBottom": {"FromBotToWood": (
        "Wood",
        lambda state, player: state.has("HookShot", player)
    )},
    "WoodD5": {
        "D5Ent2": ("D5P2", lambda state, player: state._Zroth_can_damage(player)),
        "D5E2toWood": ("WoodUp", lambda state, player: state._Zroth_can_rodHook(player)),
        "GutterAccess": ("Gutter", lambda state, player: state._Zroth_can_rock(player, 2))
    },

    "Gutter": {
        "GutterBackWood": ("WoodD5", lambda state, player: state._Zroth_can_rock(player, 2)),
        "SecretPathAccess": ("SecretPath", lambda state, player: state._Zroth_can_rodHook(player))
    },
    "SecretPath": {
        "D8Ent1": ("D8", None),  # can hookrod
        # can hookrod
        "SecretBack": ("BookCave", lambda state, player: state._Zroth_can_bomb(player))
    },

    "Field": {
        "ToWood": ("Wood", lambda state, player: state._Zroth_can_rock(player, 1)),
        "ToMonsterHouse": ("MonsterHouse", None),
        "FieldToLake": ("LakeUp", None),
        "FieldToCem":  ("Cemetery", None),
        "FieldToKak": ("Kak", lambda state, player: state.has("Hammer", player)),
        "FieldToLedge": ("KakLedge", lambda state, player: state.has("HookShot", player)),
        "FieldToMnt": ("Mountain", lambda state, player: state.has("HookShot", player))
    },
    "MonsterHouse": {},

    "Mountain": {
        "ToMntBack": ("MntBack", lambda state, player: state._Zroth_can_rock(player, 2)),
        "ToMntRight": ("MntRight", lambda state, player: state._Zroth_can_bushHook(player)),
        "MntToField": ("Field", lambda state, player: state.has("HookShot", player))
    },
    "MntRight": {
        "RightToMntBack": ("MntBack", lambda state, player: state.has("HookShot", player))
    },
    "MntBack": {
        "ToGerudo": ("Desert", None),
        "ToGerLedge": ("GerLedge", lambda state, player: state.has("HookShot", player)),
        "BackToMnt": ("Mountain", lambda state, player: state._Zroth_can_rock(player, 2))
    },
    "GerLedge": {
        "LedgeToBack": ("MntBack", lambda state, player: state.has("HookShot", player)),
        "D3Ent1": ("D3", lambda state, player: state.has("HookShot", player))
    },
    "FieldLedge": {"BackFromLedge": ("MntBack", lambda state, player: state.has("HookShot", player))},

    "Desert": {
        "ToSmith": ("Smith", None),
        "GerToKakBack": ("KakBack", None),
        "D4Ent1": ("D4", None)
    },
    "Smith": {},

    "Kak": {
        "KakToLege": ("KakLedge", None),
        "ToCastleground": ("Castleground", None),
        "KakToBack": ("KakBack", lambda state, player: state._Zroth_can_rodHook(player)),
        "KakToField": ("Field", lambda state, player: state.has("Hammer", player)),
        "KakToLake": ("LakeUp", None)
    },
    "KakLedge": {
        "LedgeToField": ("Field", lambda state, player: state.has("HookShot", player)),
        "LedgeToKak": ("Kak", None)
    },
    "KakBack": {
        "BackToKak": ("Kak", lambda state, player: state._Zroth_can_bushHook(player)),
        "KakToDesert": ("Desert", None)
    },

    "Castleground": {
        "D9Ent1": ("D9", lambda state, player: state._Zroth_has_crystals(player)),
        "CastleToLand": ("Land", lambda state, player: state._Zroth_can_rodHook(player)),
        "CastleToKak": ("Kak", None)
    },
    "Castletop": {
        "D9Ent2": ("D9", None),
        "D9Ent3": ("D9Top", None)
    },

    "LakeUp": {
        "UpToLake": ("Lake", lambda state, player: state._Zroth_can_water(player)),
        "UpToD2Cave": ("D2Cave", lambda state, player: state._Zroth_can_bomb(player)),
        "UpToKak": ("Kak", None),
        "UpToField": ("Field", None)
    },
    "Lake": {
        "LakeToUp": ("LakeUp", None),
        "LakeToLand": ("Land", lambda state, player: state.has("Hammer", player)),
        "LakeToShadow": ("Shadow", None),
        "LakeToD2": ("D2Island", None)
    },
    "D2Cave": {
        "D2CaveExit": ("LakeUp", None),
        "ToD2Side": ("D2CaveD2Side", lambda state, player: state._Zroth_can_remote(player))
    },
    "D2CaveD2Side": {
        "ToD2Cave": ("D2Cave", lambda state, player: state._Zroth_can_sphere(player)),
        "ToIsland": ("D2Island", None)
    },
    "D2Island": {
        "IslandToCave": ("D2CaveD2Side", None),
        "IslandToLake": ("Lake", lambda state, player: state._Zroth_can_water(player)),
        "D2Ent1": ("D2", None)
    },

    "Shadow": {
        "ToBookCave": ("BookCave", lambda state, player: state._Zroth_can_bush(player)),
        "ShadToD5": (
            "D5Area",
            lambda state, player: (
                # talking to mayor
                state.has("Book", player)
                and
                state._Zroth_has_crystals(player, 4)
            )
        ),
        "ToCemetery": ("Cemetery", lambda state, player: state.has("Hammer", player)),
        "ShadToLake": ("Lake", lambda state, player: state._Zroth_can_water(player))
    },
    "BookCave": {"BookToShadow": ("Shadow", lambda state, player: state._Zroth_can_bush(player))},
    "D5Area": {
        "D5Ent1": ("D5", lambda state, player: state._Zroth_can_damage(player)),
        "ToWoodBottom": ("WoodBottom", lambda state, player: state.has("Hammer", player))
    },
    "Cemetery": {
        "ToShadow": ("Shadow", lambda state, player: state.has("Hammer", player)),
        "CemToField": ("Field", None)
    },

    "Land": {
        "LandToLake": ("Lake", lambda state, player: state._Zroth_can_water(player)),
        "D6Ent1": ("D6Ent", lambda state, player: state.has("Hammer", player)),
        "ToD7": ("D7Area", lambda state, player: state._Zroth_can_rodHook(player)),
        "LansToCastle": ("Castleground", lambda state, player: state._Zroth_can_bushHook(player))
    },
    "TurtleTop": {"D6Ent2": ("D6", None)},

    "D7Area": {
        "D7Ent1": ("D7", None),
        "BackToLand": ("Land", lambda state, player: state._Zroth_can_bushHook(player)),
        "D7ToLake": (
            "Lake",
            lambda state, player: (
                state.has("HookShot", player)
                and
                state._Zroth_can_water(player)
            )
        )
    },

    "D1": {
        "D1Ext1": ("Wood", lambda state, player: state._Zroth_can_bush(player)),
        "D1ToE2": ("D1E2", lambda state, player: state._Zroth_can_bomb(player))
    },
    "D1E2": {
        "D1ToE1": ("D1", lambda state, player: state._Zroth_can_bomb(player)),
        "D1Ext2": ("WoodUp", None)
    },

    "D2": {},

    "D3": {
        "D3Ext1": ("GerLedge", lambda state, player: state.has("HookShot", player)),
        "D3Ext2": ("FieldLedge", lambda state, player: state.has("HookShot", player))
    },

    "D4": {},

    "D5": {
        "D5Ext1": ("D5Area", None),
        "ToD5E2": (
            "D5P2",
            lambda state, player: (
                state._Zroth_can_damage(player)
                and (
                    state._Zroth_can_remote(player)
                    or
                    state.has("Hammer", player)
                )
            )
        )
    },
    "D5P2": {
        "DExt2": ("WoodD5", None),
        "ToD5E1": (
            "D5",
            lambda state, player: (
                state._Zroth_can_damage(player)
                and (
                    state._Zroth_can_remote(player)
                    or
                    state.has("Hammer", player)
                )
            )
        )
    },

    "D6Ent": {"ToD6E2": ("D6", lambda state, player: state._Zroth_can_fire(player))},
    "D6": {"D6Ext2": ("TurtleTop", None)},

    "D7": {},

    "D8": {},

    "D9": {
        "D9Ext2": (
            "Castletop",
            lambda state, player: (
                state._Zroth_can_fire(player)
                or
                state.has_group("Swords", player)
            )
        )
    },

    "D9Top": {}
}
