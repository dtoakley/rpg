class Location(object):

    def __init__(self, name, desc, paths={}, event=None):
        self.name = name
        self.desc = desc
        self.items = []
        self.characters = []
        self.event = event
        self.paths = paths
        self.first_time = True
        self.can_travel = False

    def add_item(self, item):
        self.items.append(item)
        return item

    def add_character(self, character):
        self.characters.append(character)
        return character

    def add_path(self, path):
        self.paths.update(path)
        return path

    def get_item(self, item_name):
        for item in self.items:
            if item_name == item.name or item_name == item.name.capitalize():
                return item

    def get_character(self, character_name):
        for character in self.characters:
            if character_name == character.name or character_name == character.name.capitalize():
                return character

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
        obj_check = verb.obj.name
        verb_check = verb.__class__.__name__
        pass
        # if self.event.action_obj == obj_check and self.event.verb_check == verb_check:
        #     print "event processing"

    def first_time_event(self):
        print "first time event!"




