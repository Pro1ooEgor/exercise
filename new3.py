class Master(object):
    def __setattr__(self, name, val):
        print("run code in Master: %s" % val)


a = Master()
a.x = 123