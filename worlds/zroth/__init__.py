# from .Options import mygame_options  # the options we defined earlier
from .Items import Zroth_items  # data used below to add items to the World
from .Locations import Zroth_locations  # same as above
from ..AutoWorld import World
#from BaseClasses import Region, Location, Entrance, Item
from Utils import get_options, output_path

from .Constant import GAMENAME, STARTID
from .Logic import ZrothLogic


class ZrothWorld(World):

    game: str = GAMENAME

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
        "FireSource": {"Lamp", "FireRod"}
    }

    _entrance_rules = []

    def create_regions(self) -> None:
        return super().create_regions()
