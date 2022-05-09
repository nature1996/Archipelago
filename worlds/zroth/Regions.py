Zroth_Region = {
    "Menu": {"NewGame": ("LinksHouse", True)},
    "LinksHouse": {"LinksExit": ("Wood", True)},
    "Wood": {
        "WoodExit": "Field",
        "D1Ent1": "D1"
    },
    "WoodUp": {
        "D1Ent2": "D1E2",
        "FromUpToWood": "Wood"
    },
    "WoodBottom": {"FromBotToWood": "Wood"},
    "WoodD5": {
        "D5Ent2": "D5P2",
        "D5E2toWood": "WoodUp",
        "GutterAccess": "Gutter"
    },

    "Gutter": {
        "GutterBackForest": "WoodD5",
        "SecretPathAccess": "SecretPath"
    },
    "SecretPath": {
        "D8Ent1": "D8",
        "SecretBack": "BookCave"
    },

    "Field": {
        "ToWood": "Wood",
        "ToMonsterHouse": "MonsterHouse",
        "FieldToLake": "LakeUp",
        "FieldToCim":  "Cimetary",
        "FieldToKak": "Kak",
        "FieldToLedge": "KakLedge",
        "FieldToMnt": "Mountain"
    },
    "MonsterHouse": {},

    "Mountaint": {
        "ToMntBack": "MntBack",
        "MntToField": "Field"
    },
    "MntBack": {
        "ToGerudo": "Desert",
        "ToGerLedge": "GerLedge",
        "BackToMnt": "Mountain"
    },
    "GerLedge": {
        "LedgeToBack": "MntBack",
        "D3Ent1": "D3"
    },
    "FieldLedge": {"BackFromLedge": "MntBack"},

    "Desert": {
        "ToSmith": "Smith",
        "GerToKakBack": "KakBack",
        "D4Ent1": "D4"
    },
    "Smith": {},

    "Kak": {
        "KakToLege": "KakLedge",
        "ToCastleground": "Castleground",
        "KakToBack": "KakBack",
        "KakToField": "Field",
        "KakToLake": "LakeUp"
    },
    "KakLedge": {
        "LedgeToField": "Field",
        "LedgeToKak": "Kak"
    },
    "KakBack": {
        "BackToKak": "Kak",
        "KakToDesert": "Desert"
    },

    "Castleground": {
        "D9Ent1": "D9",
        "groundToLand": "Land",
        "CastleToKak": "Kak"
    },
    "Castletop": {
        "D9Ent2": "D9",
        "D9Ent3": "D9Top"
    },

    "LakeUp": {
        "UpToLake": "Lake",
        "UpToD2Cave": "D2Cave",
        "UpToKak": "Kak",
        "UpToField": "Field"
    },
    "Lake": {
        "LakeToUp": "LakeUp",
        "LakeToLand": "Land",
        "LakeToShadow": "Shadow",
        "LakeToD2": "D2Island"
    },
    "D2Cave": {
        "D2CaveExit": "LakeUp",
        "ToD2Side": "D2CaveD2Side"
    },
    "D2CaveD2Side": {
        "ToD2Cave": "D2Cave",
        "ToIsland": "D2Island"
    },
    "D2Island": {
        "IslandToCave": "D2CaveD2Side",
        "IslandToLake": "Lake",
        "D2Ent1": "D2"
    },

    "Shadow": {
        "ToBookCave": "BookCave",
        "ShadToD5": "D5Area",
        "ToCimetary": "Cimetary",
        "ShadToLake": "Lake"
    },
    "BookCave": {"BookToShadow": "Shadow"},
    "D5Area": {
        "D5Ent1": "D5",
        "ToWoodBottom": "WoodBottom"
    },
    "Cemetary": {
        "ToShadow": "Shadow",
        "CemToField": "Field"
    },

    "Land": {
        "LandToLake": "Lake",
        "D6Ent1": "D6Ent",
        "ToD7": "D7Area",
        "LansToCastle": "CastleGround"
    },
    "TurtleTop": {"D6Ent2": "D6"},

    "D7Area": {
        "D7Ent1": "D7",
        "BackToLand": "Land",
        "D7ToLake": "Lake"
    },

    "D1": {
        "D1Ext1": "Forset",
        "D1ToE2": "D1E2"
    },
    "D1E2": {
        "D1ToE1": "D1",
        "D1Ext2": "WoodUp"
    },

    "D2": {},

    "D3": {
        "D3Ext1": "GerLedge",
        "D3Ext2": "FieldLedge"
    },

    "D4": {},

    "D5": {
        "D5Ext1": "D5Area",
        "ToD5E2": "D5P2"
    },
    "D5P2": {
        "DExt2": "WoodD5",
        "ToD5E1": "D5"
    },

    "D6Ent": {"ToD6E2": "D6"},
    "D6": {"D6Ext2": "TurtleTop"},

    "D7": {},

    "D8": {},

    "D9": {"D9Ext2": "Castletop"},

    "D9Top": {}
}
