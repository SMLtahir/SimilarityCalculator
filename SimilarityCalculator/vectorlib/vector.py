class Vector:

    @staticmethod
    def vector_sum(vectors):
        return Vector(reduce(lambda x, y: x+y, vectors))

    def __init__(self, data):
        self.data = list(data)

    def __repr__(self):
        return repr(self.data)

    # overload +
    def __add__(self, other):
        return Vector(map(lambda x, y: x+y, self, other))

    # overload -
    def __sub__(self, other):
        return Vector(map(lambda x, y: x-y, self, other))

    def __mul__(self, c):
        return Vector(map(lambda x: c*x, self))

    def __div__(self, c):
        return self * (1.0/c)

    # overload []
    def __getitem__(self, index):
        return self.data[index]

    # overload set []
    def __setitem__(self, key, item):
        self.data[key] = item

    # return size to len()
    def __len__(self):
        return len(self.data)
    
    def __eq__(self, other):
        return self.data == other.data