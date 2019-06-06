class Some:
    def __init__(self, value):
        self.value = value

    def __call__(self, other_value):
        return self.value * other_value


s = Some(5)
print(s(5))
