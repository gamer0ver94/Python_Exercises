from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class of Character.
        Args:
            first_name(str): The first name
            is_alive(bool): optional, by default is alive(True)"""

    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method that should be implemented in subclasses."""
        pass


class Stark(Character):
    """Class Stark that inheritate from Character"""

    def die(self):
        """This method passes is_alive to False"""
        self.is_alive = False
