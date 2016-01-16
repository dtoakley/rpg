class Verb(object):

    def __init__(self, subj, obj):
        self.subj = subj
        self.obj = obj

    def action(self, func):
        return func(self.obj)


class PickUp(Verb):

    def __init__(self, subj, obj):
        super(PickUp, self).__init__(subj, obj)

    def pick_up(self):
        try:
            self.action(self.subj.add_item)
        except AttributeError:
            print self.subj.name + "can't pick that up!"


class LookAt(Verb):

    def __init__(self, subj, obj):
        super(LookAt, self).__init__(subj, obj)

    def look_at(self):
        try:
            print self.obj.desc
            return self.obj.desc
        except AttributeError:
            print self.subj.name + "has no description!"


class Use(Verb):

    def __init__(self, subj, obj):
        super(Use, self).__init__(subj, obj)

    def use(self):

        try:
            self.action(self.obj.use)
        except AttributeError:
            print "You can't use that object!"










