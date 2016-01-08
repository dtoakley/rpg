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
    def __init__(self, name=None, desc=None, hp=100, coins=100):
        super(Player, self).__init__(name, desc, hp, coins)
        self.player = True
        self.is_victorious = False
        self.current_location = None

    def set_player_name(self, name, game_name):
        self.name = name
        print "Welcome to " + game_name + ", " + self.name
        return name

    def death(self, end_message):
        self.is_alive = False
        print end_message

    def set_location(self, location):
        self.current_location = location
        return self.current_location

    def take_turn(self, action):

        if action["verb"] == "move":
            to_go = action["path"]
            self.set_location(self.current_location.paths[to_go])

        elif action["verb"] in ["pick", "take"]:
            item = self.current_location.get_item(action["noun"])
            self.add_item(item)
            self.current_location.items.remove(item)
            print item.name + " added to your inventory"

        elif action["verb"] == "look":
            # logic for look action
            print "seen"


class Npc(Character):

    def __init__(self, name=None, desc=None, hp=50, coins=100):
        super(Npc, self).__init__(name, desc, hp, coins)

    def dialogue(self):
        pass


class Enemy(Character):

    def __init__(self, name, desc, hp, coins):
        super(Enemy, self).__init__(name, desc, hp, coins)
        self.can_fight = True
