class Location(object):

    def __init__(self, name, desc, paths={}, event=None, travelable=True):
        self.name = name
        self.desc = desc
        self.items = []
        self.characters = []
        self.paths = paths
        self.event = event
        self.player = None
        self.travelable = travelable
        self.first_time = True

    def add_item(self, item):
        self.items.append(item)
        return item

    def add_character(self, character):
        self.characters.append(character)
        return character

    def add_player(self, player):
        self.player = player
        return player

    def add_path(self, path):
        self.paths.update(path)
        return path

    def can_travel(self):
        self.travelable = True
        return True

    def get_item(self, item_name):
        for item in self.items:
            if item_name == item.name or item_name == item.name.capitalize():
                return item

    def get_path(self, path_name):
        for direction, location in self.paths.iteritems():
            if location.name == path_name:
                return location

    def get_character(self, character_name):
        for character in self.characters:
            if character_name == character.name or character_name == character.name.capitalize():
                return character

    # TODO -- refactor to include paths

    def search_objects(self, name):
        for objs in [self.characters, self.items]:
            for item in objs:
                if name == item.name or name.capitalize() == item.name:
                    return item

    def get_desc(self):
        return self.desc

    def load(self):
        print self.desc

        if self.first_time:
            self.first_time_event()
            self.first_time = False

    def process_event(self, verb):
        # takes a verb object and executes the event in that location

        object_check = verb.obj.name.lower()
        verb_check = verb.__class__.__name__.lower()

        reaction_obj = self.get_path(self.event.get('reaction_object'))
        reaction_method_name = self.event.get('reaction_verb')
        reaction_desc = self.event.get('reaction_desc')

        if object_check.capitalize() not in self.player.get_inventory():
            print "You can't use that item!"
            return
        elif self.event.get('action_verb') == verb_check and self.event.get('action_object') == object_check:
            getattr(reaction_obj, reaction_method_name)()
            print reaction_desc
            return

    @staticmethod
    def first_time_event():
        print "first time event!"




