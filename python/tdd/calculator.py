class Calculator(object):

    def add(self, x, y):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x+y
        else:
            raise ValueError