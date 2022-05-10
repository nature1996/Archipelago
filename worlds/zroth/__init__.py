from .Options import Zroth_options  # the options we defined earlier
from .Regions import Zroth_regions
# data used below to add items to the World
from .Items import ZrothItem, Zroth_progress, Zroth_other, Zroth_items
from .Locations import ZrothLocation, Zroth_locations  # same as above
from ..AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item
from Utils import get_options, output_path
from ..generic.Rules import add_rule, set_rule, forbid_item, add_item_rule

from .Constant import GAMENAME, STARTID
from . import Logic


class ZrothWorld(World):

    game: str = GAMENAME

    options = Zroth_options

    topology_peresent: bool = True
    remote_items: bool = False
    remote_start_inventory: bool = False

    date_version = 0

    base_id = STARTID

    item_name_to_id = {name: id for
                       id, name in enumerate(Zroth_items.keys(), base_id)
                       }
    location_name_to_id = {name: id for
                           id, name in enumerate(
                               Zroth_locations.keys(), base_id)
                           }

    item_name_groups = {
        "Swords": {"ProgressiveSword", "MasterSword"},
        "FireSources": {"Lamp", "FireRod"},
        "Crystals": {
            "D1Crystal",
            "D2Crystal",
            "D3Crystal",
            "D4Crystal",
            "D5Crystal",
            "D6Crystal",
            "D7Crystal"
        }
    }

    def create_item(self, name: str) -> Item:
        return ZrothItem(name, name in Zroth_progress, self.item_name_to_id[name], self.player)

    def create_regions(self) -> None:
        # Region
        exit_to_link: dict[str, tuple[str, any]] = {}
        for region, exits in Zroth_regions.items():
            r = Region(region, 0, region, self.player, self.world)
            for exit in exits.keys():
                r.exits.append(Entrance(self.player, exit, r))
            exit_to_link.update(exits)
            self.world.regions.append(r)

        for exit, data in exit_to_link.items():
            e = self.world.get_entrance(exit, self.player)
            for conection, test in data.items():
                e.connect(self.world.get_region(conection, self.player))
                if (test != None):
                    set_rule(e, lambda state: test(state, self.player))

        # Location
        for location, data in Zroth_locations.items():
            for region, test in data.items():
                r = self.world.get_region(region, self.player)
                l = ZrothLocation(self.player, location,
                                  self.location_name_to_id[location], r)
                r.locations.append(l)

                if (test != None):
                    set_rule(l, lambda state: test(state, self.player))
        return

    def create_items(self) -> None:
        for item, ammount in Zroth_items.items():
            for _ in range(ammount):
                self.world.itempool.append(self.create_item(item))
        return

    def set_rules(self) -> None:
        self.world.get_location("D1Crystal", self.player).place_locked_item(
            self.create_item("D1Crystal"))
        self.world.get_location("D2Crystal", self.player).place_locked_item(
            self.create_item("D2Crystal"))
        self.world.get_location("D3Crystal", self.player).place_locked_item(
            self.create_item("D3Crystal"))
        self.world.get_location("D4Crystal", self.player).place_locked_item(
            self.create_item("D4Crystal"))
        self.world.get_location("D5Crystal", self.player).place_locked_item(
            self.create_item("D5Crystal"))
        self.world.get_location("D6Crystal", self.player).place_locked_item(
            self.create_item("D6Crystal"))
        self.world.get_location("D7Crystal", self.player).place_locked_item(
            self.create_item("D7Crystal"))

        self.world.get_location("MSword", self.player).place_locked_item(
            self.create_item("MasterSword"))

        self.world.get_location("Triforce", self.player).place_locked_item(
            self.create_item("Triforce"))

        self.world.completion_condition[self.player] = lambda state: state.has(
            "Triforce", self.player)

        return
