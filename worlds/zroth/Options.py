from msilib.schema import Class
from Options import DefaultOnToggle, Option
import typing


class FakeFlipper(DefaultOnToggle):
    display_name = "Fake Flipper Glitch"


Zroth_options: typing.Dict[str, type[Option]] = {
    "FakeFlipper": FakeFlipper
}
