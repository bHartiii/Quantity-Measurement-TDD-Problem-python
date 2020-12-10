class LengthConvertor:

    def __init__(self, value, ob):
        self.value = value
        self.ob = ob

    def __eq__(self, other):
        if isinstance(other, LengthConvertor):
            if self.ob.convert_into_inch(self.value) == other.ob.convert_into_inch(other.value):
                return True
            else:
                return False
