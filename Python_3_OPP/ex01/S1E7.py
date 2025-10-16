from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        """Contructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string with properties listed"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string with properties listed"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """set is_alive to False"""
        self.is_alive = False


class Lannister(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        """Contructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a string with properties listed"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string with properties listed"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """set is_alive to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name, is_alive):
        """Instatiate the class itself"""
        return cls(name, is_alive)
