class Character(object):

    def __init__(self, name, desc, coins=100):
        self.name = name
        self.desc = desc
        self.items = []
        self.coins = coins
        self.is_alive = True
        self.current_location = None

    def add_item(self, item):
        self.items.append(item)
        return item

    def get_inventory(self):
        result = []
        for item in self.items:
            result.append(item.name)
        return result

    def set_location(self, location):
        self.current_location = location
        return self.current_location

    def move(self, location):
        self.set_location(location)
        return

    def death(self):
        self.is_alive = False
        return


class Player(Character):
    def __init__(self, name=None, desc=None, coins=100):
        super(Player, self).__init__(name, desc, coins)
        self.player = True
        self.is_victorious = False

    def set_player_name(self, name, game_name):
        self.name = name
        print "Welcome to " + game_name + ", " + self.name
        return name


class Npc(Character):

    def __init__(self, name=None, desc=None, coins=100):
        super(Npc, self).__init__(name, desc, coins)

    def dialogue(self):
        pass


class Enemy(Character):

    def __init__(self, name, desc, coins):
        super(Enemy, self).__init__(name, desc, coins)
        self.can_fight = True


