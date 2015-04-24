class Vector:

    @staticmethod
    def vectorSum(vectors):
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
    
if __name__ == "__main__":
    
    assert repr(Vector([1,1,2,2]))==repr([1,1,2,2])
    assert Vector([1,1,3,5]) + Vector([3,2,5,0]) == Vector([4,3,8,5])
    assert Vector([1,1,3,5]) + Vector([3,2,5,1]) != Vector([4,3,8,5])
    assert Vector([1,1,3,5]) - Vector([3,2,5,0]) == Vector([-2,-1,-2,5])
    assert Vector([1,1,3,5]) - Vector([3,2,5,1]) != Vector([-2,-1,-2,5])
    assert Vector([1,1,3,5])*2  == Vector([2,2,6,10])
    assert Vector([1,1,3,6])*2  != Vector([2,2,6,10])
    assert Vector([1,1,3,5])/2  == Vector([.5, .5, 1.5, 2.5])
    assert Vector([1,1,3,6])/2  != Vector([.5, .5, 1.5, 2.5])
    assert Vector([11,12,13,14])[1] ==12
    v = Vector([11,12,13,14])
    v[3] = 2
    assert v==Vector([11,12,13,2])
    assert len(v)==4
    assert Vector.vectorSum([Vector([1,1,2]), Vector([3,3,2]), Vector([8,7,-1])])==Vector([12,11,3])
    print 'Passed tests!'
