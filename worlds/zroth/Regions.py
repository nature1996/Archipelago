Zroth_Region = {
    "Menu": {"NewGame": "LinksHouse"},
    "LinksHouse": {"LinksExit": "Wood"},
    "Wood": {"WoodExit": "Field", "D1Ent1": "D1"},
    "WoodUp": {"D1Ent2": "D1", "FromUpToWood": "Wood"},
    "WoodBottom": {"FromBotToWood": "Wood"},
    "WoodD5": {"D5Ent2": "D5P2", "D5E2toWood": "WoodUp", "GutterAccess": "Gutter"},

    "Gutter": {"GutterBackForest": "WoodD5", "SecretPathAccess": "SecretPath"},
    "SecretPath": {"D8Ent1": "D8", "SecretBack": "BookCave"},

    "Field": {"ToMonsterHouse": "MonsterHouse",
              "FieldToLake": "LakeUp",
              "FieldToCim":  "Cimetary",
              "FieldToKak": "Kak",
              "FieldToLedge": "KakLedge",
              "FieldToMnt": "Mountain"},
    "MonsterHouse": {},

    "Mountaint": {"ToMntBack": "MntBack"},
    "MntBack": {"ToGerudo": "Desert", "ToGerLedge": "GerLedge"},
    "GerLedge": {"LedgeToBack": "MntBack", "D3Ent1": "D3"},
    "FieldLedge": {"BackFromLedge": "MntBack"},

    "Desert": {"ToSmith": "Smith", "GerToKakBack": "KakBack", "D4Ent1": "D4"},

    "Kak": {"KakToLege": "KakLedge",
            "ToCastleground": "Castleground",
            "KakToBack": "KakBack",
            "KakToField": "Field"},
    "KakLedge": {"LedgeToField": "Field", "LedgeToKak": "Kak"},
    "KakBack": {"BackToKak": "Kak", "KakToDesert": "Desert"},

    "Castleground": {"D9Ent1": "D9", "groundToLand": "Land"},
    "Castletop":   {"D9Ent2": "D9", "D9Ent3": "D9Top"},

}
