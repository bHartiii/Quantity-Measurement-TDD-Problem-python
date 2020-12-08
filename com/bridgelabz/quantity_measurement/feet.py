class Feet:

    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            if other.feet == self.feet:
                return True
        return False

