
from ast import And
from ..AutoWorld import LogicMixin
# state._Zroth_can_(player)


class ZrothLogic(LogicMixin):
    def _Zroth_has_Dkey(self, player: int, dungeon: int, amount: int = 1):
        return self.has("SmallKeyD"+str(dungeon), player, amount)

    def _Zroth_has_Bkey(self, player: int, dungeon: int):
        return self.has("BossKeyD"+str(dungeon), player)

    def _Zroth_has_crystals(self, player: int, amount: int = 7):
        return self.has_group("Crystals", player, amount)

    def _Zroth_can_damage(self, player: int):
        frod = self._Zroth_can_firerod(player)
        bow = self._Zroth_can_bow(player)
        bomb = self._Zroth_can_bomb(player)
        sword = self.has_group("Swords", player)
        hammer = self.has("Hammer", player)
        hook = self.has("HookShot", player)
        return frod or bow or bomb or sword or hammer or hook

    def _Zroth_can_advDamage(self, player: int):
        fbow = self.has("bow", player, 2)
        msword = self.has("MasterSword", player)
        return fbow or msword

    def _Zroth_can_reflect(self, player: int):
        sword = self.has("ProgressiveSword", player, 2)
        msword = self.has("MasterSword", player)
        return sword or msword

    def _Zroth_can_rock(self, player: int, level: int):
        return self.has("Gloves", player, level)

    def _Zroth_can_amunition(self, player: int):
        pot = self._Zroth_can_rock(player, 1)
        sword = self.has_group("Swords", player)
        hook = self.has("HookShot", player)
        return pot or sword or hook

    def _Zroth_can_fire(self, player: int):
        fire = self.has_group("FireSources", player)
        magic = self._Zroth_can_amunition(player)
        return fire and magic

    def _Zroth_can_bush(self, player: int):
        sword = self.has_group("Swords", player)
        fire = self._Zroth_can_fire(player)
        return sword or fire

    def _Zroth_can_firerod(self, player: int):
        rod = self.has("FireRod", player)
        magic = self._Zroth_can_amunition(player)
        return rod and magic

    def _Zroth_can_icerod(self, player: int):
        rod = self.has("IceRod", player)
        magic = self._Zroth_can_amunition(player)
        return rod and magic

    def _Zroth_can_bow(self, player: int):
        bow = self.has("Bow", player)
        arrow = self._Zroth_can_amunition(player)
        return bow and arrow

    def _Zroth_can_bomb(self, player: int):
        bomb = True
        refil = self._Zroth_can_amunition(player)
        return bomb and refil

    def _Zroth_can_water(self, player: int):
        flipper = self.has("Flipper", player)
        rod = self._Zroth_can_icerod(player)
        return flipper or rod

    def _Zroth_can_swim(self, player: int):
        flipper = self.has("Flipper", player)
        rod = self._Zroth_can_icerod(player)
        fakeflipper = rod and True
        return flipper or fakeflipper

    def _Zroth_can_remote(self, player: int):
        irod = self._Zroth_can_icerod(player)
        frod = self._Zroth_can_firerod(player)
        bow = self._Zroth_can_bow(player)
        hook = self.has("HookShot", player)
        return irod or frod or bow or hook

    def _Zroth_can_bushHook(self, player: int):
        bush = self._Zroth_can_bush(player)
        hook = self.has("HookShot", player)
        return bush and hook

    def _Zroth_can_rodHook(self, player: int):
        frod = self._Zroth_can_firerod(player)
        hook = self.has("HookShot", player)
        return frod and hook

    def _Zroth_can_sphere(self, player: int):
        irod = self._Zroth_can_icerod(player)
        frod = self._Zroth_can_firerod(player)
        bow = self._Zroth_can_bow(player)
        bomb = self._Zroth_can_bomb(player)
        sword = self.has_group("Swords", player)
        hammer = self.has("Hammer", player)
        hook = self.has("HookShot", player)
        return irod or frod or bow or bomb or sword or hammer or hook

    def _Zroth_enemy_001(self, player: int):
        area = self.can_reach("D1", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_002(self, player: int):
        area = self.can_reach("D7", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and damage

    def _Zroth_enemy_003(self, player: int):
        area = self.can_reach("Wood", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_004(self, player: int):
        area = (self.can_reach("Wood", "Region", player)
                or self.can_reach("D1", "Region", player)
                or self.can_reach("D1E2", "Region", player))
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_005(self, player: int):
        area1 = self.can_reach("MntRight", "Region", player)
        area2 = self.can_reach("MntBack", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return (area1 or area2) and (damage or rock)

    def _Zroth_enemy_006(self, player: int):
        area = (self.can_reach("Mountain", "Region", player)
                or self.can_reach("MntRight", "Region", player)
                or self.can_reach("MntBack", "Region", player))
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_008(self, player: int):
        area = self.can_reach("Field", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_009(self, player: int):
        area = (self.can_reach("LakeUp", "Region", player)
                or self.can_reach("D2Island", "Region", player)
                or self.can_reach("D2", "Region", player))
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_010(self, player: int):
        area = (self.can_reach("LakeUp", "Region", player)
                or self.can_reach("D2Island", "Region", player))
        damage = self._Zroth_can_remote(player)
        reflect = self._Zroth_can_reflect(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or reflect or rock)

    def _Zroth_enemy_011(self, player: int):
        area = (self.can_reach("Shadow", "Region", player)
                or self.can_reach("D5Area", "Region", player))
        hammer = self.has("Hammer", player)
        return area and hammer

    def _Zroth_enemy_012(self, player: int):
        area = (self.can_reach("Shadow", "Region", player)
                or self.can_reach("D5Area", "Region", player)
                or self.can_reach("D5", "Region", player)
                or self.can_reach("D5P2", "Region", player)
                or self.can_reach("BookCave", "Region", player))
        damage = self._Zroth_can_advDamage(player)
        return area and damage

    def _Zroth_enemy_013(self, player: int):
        area = self.can_reach("Desert", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_014(self, player: int):
        area = self.can_reach("Desert", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_015(self, player: int):
        area = self.can_reach("Land", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 2)
        return area and (damage or rock)

    def _Zroth_enemy_016(self, player: int):
        area = self.can_reach("SecretPath", "Region", player)
        reflect = self._Zroth_can_reflect(player)
        return area and (reflect)

    def _Zroth_enemy_018(self, player: int):
        area1 = self.can_reach("D1", "Region", player)
        area2 = (self.can_reach("D2Cave", "Region", player)
                 or self.can_reach("D2CaveD2Side", "Region", player))
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return (area1 and (damage or rock)) or (area2 and damage)

    def _Zroth_enemy_019(self, player: int):
        area = self.can_reach("D1Crystal", "Location", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_021(self, player: int):
        area = self.can_reach("D4Boss", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_022(self, player: int):
        area = self.can_reach("D2", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_enemy_023(self, player: int):
        area1 = self.can_reach("D2", "Region", player)
        area2 = self.can_reach("D2Cave", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return (area1 and (damage or rock)) or (area2 and damage)

    def _Zroth_enemy_024(self, player: int):
        area = self.can_reach("D2Crystal", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_025(self, player: int):
        area = self.can_reach("D3", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_026(self, player: int):
        area = self.can_reach("D3", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_027(self, player: int):
        area = self.can_reach("D3", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_028(self, player: int):
        area = self.can_reach("D3Crystal", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_029(self, player: int):
        area = self.can_reach("D4", "Region", player)
        fire = self._Zroth_can_fire(player)
        return area and (fire)

    def _Zroth_enemy_030(self, player: int):
        area = self.can_reach("D4", "Region", player)
        reflect = self._Zroth_can_reflect(player)
        return area and (reflect)

    def _Zroth_enemy_031(self, player: int):
        area = self.can_reach("D4Crystal", "Location", player)
        reflect = self._Zroth_can_reflect(player)
        return area and (reflect)

    def _Zroth_enemy_032(self, player: int):
        area = (self.can_reach("D5", "Region", player)
                or self.can_reach("D5P2", "Region", player))
        damage = self._Zroth_can_damage(player)
        return area and damage

    def _Zroth_enemy_033(self, player: int):
        area = (self.can_reach("D5", "Region", player)
                or self.can_reach("D5P2", "Region", player))
        damage = self._Zroth_can_damage(player)
        return area and damage

    def _Zroth_enemy_034(self, player: int):
        area = (self.can_reach("D5", "Region", player)
                or self.can_reach("D5P2", "Region", player))
        bow = self._Zroth_can_bow(player)
        return area and bow

    def _Zroth_enemy_035(self, player: int):
        area = self.can_reach("D5Crystal", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_037(self, player: int):
        area = self.can_reach("D6", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_038(self, player: int):
        area = (self.can_reach("D6", "Region", player)
                or self.can_reach("D6Ent", "Region", player))
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_039(self, player: int):
        area = self.can_reach("D6", "Region", player)
        bow = self._Zroth_can_bow(player)
        return area and bow

    def _Zroth_enemy_040(self, player: int):
        area = self.can_reach("D6Crystal", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_041(self, player: int):
        area = self.can_reach("D7", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_042(self, player: int):
        area = self.can_reach("D7", "Region", player)
        fire = self._Zroth_can_fire(player)
        return area and (fire)

    def _Zroth_enemy_043(self, player: int):
        area = self.can_reach("D7Crystal", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_044(self, player: int):
        area = self.can_reach("D8", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_045(self, player: int):
        area = self.can_reach("MSword", "Location", player)
        damage = self._Zroth_can_damage(player)
        hammer = self.has("Hammer", player)
        return area and (damage and hammer)

    def _Zroth_enemy_046(self, player: int):
        area = self.can_reach("D9", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_047(self, player: int):
        area = self.can_reach("D9", "Region", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_048(self, player: int):
        area = self.can_reach("D9K3", "Location", player)
        damage = self._Zroth_can_damage(player)
        return area and (damage)

    def _Zroth_enemy_050(self, player: int):
        area = self.can_reach("Triforce", "Location", player)
        damage = self._Zroth_can_advDamage(player)
        return area and (damage)

    def _Zroth_enemy_053(self, player: int):
        area = self.can_reach("Field", "Region", player)
        damage = self._Zroth_can_damage(player)
        rock = self._Zroth_can_rock(player, 1)
        return area and (damage or rock)

    def _Zroth_has_monster(self, player: int, count: int):
        return (
            self._Zroth_enemy_001(player)
            + self._Zroth_enemy_002(player)
            + self._Zroth_enemy_003(player)
            + self._Zroth_enemy_004(player)
            + self._Zroth_enemy_005(player)
            + self._Zroth_enemy_006(player)
            + self._Zroth_enemy_008(player)
            + self._Zroth_enemy_009(player)
            + self._Zroth_enemy_010(player)
            + self._Zroth_enemy_011(player)
            + self._Zroth_enemy_012(player)
            + self._Zroth_enemy_013(player)
            + self._Zroth_enemy_014(player)
            + self._Zroth_enemy_015(player)
            + self._Zroth_enemy_016(player)
            + self._Zroth_enemy_018(player)
            + self._Zroth_enemy_019(player)
            + self._Zroth_enemy_021(player)
            + self._Zroth_enemy_022(player)
            + self._Zroth_enemy_023(player)
            + self._Zroth_enemy_024(player)
            + self._Zroth_enemy_025(player)
            + self._Zroth_enemy_026(player)
            + self._Zroth_enemy_027(player)
            + self._Zroth_enemy_028(player)
            + self._Zroth_enemy_029(player)
            + self._Zroth_enemy_030(player)
            + self._Zroth_enemy_031(player)
            + self._Zroth_enemy_032(player)
            + self._Zroth_enemy_033(player)
            + self._Zroth_enemy_034(player)
            + self._Zroth_enemy_035(player)
            + self._Zroth_enemy_037(player)
            + self._Zroth_enemy_038(player)
            + self._Zroth_enemy_039(player)
            + self._Zroth_enemy_040(player)
            + self._Zroth_enemy_041(player)
            + self._Zroth_enemy_042(player)
            + self._Zroth_enemy_043(player)
            + self._Zroth_enemy_044(player)
            + self._Zroth_enemy_045(player)
            + self._Zroth_enemy_046(player)
            + self._Zroth_enemy_047(player)
            + self._Zroth_enemy_048(player)
            + self._Zroth_enemy_050(player)
            + self._Zroth_enemy_053(player)
        ) >= count
