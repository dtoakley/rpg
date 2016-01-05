class Character(object):

    def __init__(self, name, desc, hp, coins):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.coins = coins
        self.items = []
        self.is_alive = True

    def add_item(self, item):
        self.items.append(item)
        return item

    def get_inventory(self):
        result = []
        for item in self.items:
            result.append(item.name)
        return result


class Player(Character):
    def __init__(self, name, desc, hp, coins):
        super(Player, self).__init__(name, desc, hp, coins)
        self.player = True


class Enemy(Character):

    def __init__(self, name, desc, hp, coins):
        super(Enemy, self).__init__(name, desc, hp, coins)
        self.can_fight = True


class Npc(Character):

    def __init__(self, name, desc, hp, coins, dialogues):
        super(Npc, self).__init__(name, desc, hp, coins)
        self.dialogues = dialogues
