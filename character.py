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

    @staticmethod
    def look_at(look_obj):
        print look_obj.desc

    @staticmethod
    def get_index_from_list_tuples(list_of_t, val):
        return [index for index, value in enumerate(list_of_t) if value[0] == val]

    def process_action(self, action):
        # takes list of tuples and return name of method to be called and object to be called on

        verb_index = self.get_index_from_list_tuples(action, "verb")
        if verb_index:
            verb = action[verb_index[0]][1]
            print verb

        path_index = self.get_index_from_list_tuples(action, "path")

        if path_index:
            path = action[path_index[0]][1]
            print path

        noun_index = self.get_index_from_list_tuples(action, "noun")

        if noun_index:
            noun = action[noun_index[0]][1]
            print noun



        # if verb in ["move"]:
        #     new_location = self.current_location.paths[path]
        #     return {"move", new_location}
        #
        # if verb in ["pick", "take"]:
        #     item = self.current_location.get_item(noun)
        #     return {"add_item", item}

        # if verb in ["look", "show"]:
        #     try:
        #         obj_looked_at = self.current_location.search_objects(noun)
        #         return {"look_at", obj_looked_at}
        #     except KeyError:
        #         obj_looked_at = self.current_location.search_objects(noun)
        #         path = action["path"]
        #         return {"look_at", obj_looked_at[path]}

        # # use action
        # elif action["verb"] in ["use"]:
        #     obj_used = self.current_location.serach_objects(action["noun"])
        #     return {"use", obj_used}

        #TODO: give action
        #TODO: open action
        #TODO: close action

    def do_action(self, action_name, action_object):
        # takes the name of an action and object and calls action on the object
        action_to_call = getattr(self, action_name)
        action_to_call(action_object)


class Npc(Character):

    def __init__(self, name=None, desc=None, coins=100):
        super(Npc, self).__init__(name, desc, coins)

    def dialogue(self):
        pass


class Enemy(Character):

    def __init__(self, name, desc, coins):
        super(Enemy, self).__init__(name, desc, coins)
        self.can_fight = True


