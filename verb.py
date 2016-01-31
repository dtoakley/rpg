
class Verb(object):

    def __init__(self, subj, obj):
        self.subj = subj
        self.obj = obj

    def action(self, func):
        func(self.obj)


class PickUp(Verb):

    def __init__(self, subj, obj):
        super(PickUp, self).__init__(subj, obj)
        try:
            self.action(self.subj.add_item)
        except AttributeError:
            print "you can't pick that up!"


class LookAt(Verb):

    def __init__(self, subj, obj):
        super(LookAt, self).__init__(subj, obj)
        try:
            print self.obj.desc
        except AttributeError:
            print "no description!"


class Use(Verb):

    def __init__(self, subj, obj):
        super(Use, self).__init__(subj, obj)


class Move(Verb):

    def __init__(self, subj, obj):
        super(Move, self).__init__(subj, obj)
        try:
            self.action(self.subj.move)
        except AttributeError:
            print "There is nothing in that direction!"








