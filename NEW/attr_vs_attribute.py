class GentleGuy:
    coffee_please = 'coffee'

    def __getattr__(self, name):
        if name.endswith("_please"):
            return object.__getattribute__(self, name.replace("_please", ""))
        return "And the magic word!?"


gentle = GentleGuy()

gentle.coffee = "some coffee"
print(gentle.coffee)        # AttributeError
print(gentle.coffee_please)  # "some coffee"

