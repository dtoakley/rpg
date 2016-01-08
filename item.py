class Item(object):

    def __init__(self, name, desc, value=0, is_tradeable=True):
        self.name = name
        self.desc = desc
        self.value = value
        self.is_tradeable = is_tradeable


class Weapon(Item):

    def __init__(self, name, desc, value, damage):
        super(Weapon, self).__init__(name, desc, value)
        self.damage = damage


class Armor(Item):

    def __init__(self, name, desc, value, added_hp):
        super(Armor, self).__init__(name, desc, value)
        self.added_hp = added_hp


class Potion(Item):

    def __init__(self, name, desc, value, effect, time_period):
        super(Potion, self).__init__(name, desc, value)
        self.effect = effect
        self.time_period = time_period


class Food(Item):

    def __init__(self, name, desc, value, restored_hp):
        super(Food, self).__init__(name, desc, value)
        self.restored_hp = restored_hp


class StoryItem(Item):

    def __init__(self, name, desc, value, is_tradeable=False):
        super(StoryItem, self).__init__(name, desc, value)
        self.is_tradeable = is_tradeable



