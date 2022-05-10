
from ..AutoWorld import LogicMixin
# state._Zroth_can_(player)


class ZrothLogic(LogicMixin):
    def _Zroth_has_Dkey(self, player: int, dungeon: int, amount: int = 1):
        return self.has("SmallKeyD"+dungeon, player, amount)

    def _Zroth_has_Bkey(self, player: int, dungeon: int):
        return self.has("BossKeyD"+dungeon, player)

    def _Zroth_has_crystals(self, player: int, amount: int = 7):
        return self.has("crystal", player, amount)

    def _Zroth_has_monster(self, player: int, amount: int):
        return self._Zroth_has_crystals(player)

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
        fire = self.has_group("FireSource", player)
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
