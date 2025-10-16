from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True):
        """Contructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """set eyes to the color passed as argument
            Args:
                color(str): Color of eyes"""
        self.eyes = color

    def set_hairs(self, color: str):
        """set hairs to the color passed as argument
            Args:
                color(str): Color of haris"""
        self.hairs = color

    def get_eyes(self):
        """Return the colors of eyes"""
        return self.eyes

    def get_hairs(self):
        """Return the Color of hairs"""
        return self.hairs
