import sys
import os
import unittest
import math
sys.path.insert(0, os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

from vectorlib.kernel import WeightedCosineKernel
from vectorlib.vector import Vector
from lib.utils import weightedLength, weightedCosSim


class LoadNeighborsTests(unittest.TestCase):
    def testGetSim(self):
        # The 2 constants below are as given in the kernel.py module
        MEAN_WEIGHTED_COSINE = .6135
        STD_DEV_WEIGHTED_COSINE = .0811
        kernelFunction = WeightedCosineKernel([1, 1], True, True)
        self.assertAlmostEqual(
            (kernelFunction.get_sim(Vector([1, 1]), Vector([1, 1])) * STD_DEV_WEIGHTED_COSINE)
            + MEAN_WEIGHTED_COSINE, 1)
        self.assertAlmostEqual(
            (kernelFunction.get_sim(Vector([0, 0.25]), Vector([1, 1])) * STD_DEV_WEIGHTED_COSINE)
            + MEAN_WEIGHTED_COSINE, math.sqrt(0.5))
        self.assertAlmostEqual((kernelFunction.get_sim(Vector([0, 0]), Vector([1, 1])) * STD_DEV_WEIGHTED_COSINE)
                               + MEAN_WEIGHTED_COSINE, 0)
        print '\nPassed GetSim tests!'

    def testWeightedCosSim(self):
        self.assertAlmostEqual(weightedCosSim(Vector([1, 1]).data, Vector([1, 1]).data, [1, 1]), 1)
        self.assertAlmostEqual(weightedCosSim(Vector([1, 1]).data, Vector([1, -1]).data, [1, 1]), 0)
        self.assertAlmostEqual(weightedCosSim(Vector([0, 0.25]).data, Vector([1, 1]).data, [1, 1]), math.sqrt(0.5))
        assert weightedCosSim(Vector([0, 0]).data, Vector([1, 1]).data, [0, 0]) == 0
        assert weightedCosSim(Vector([2, 12]).data, Vector([13, 15]).data, [0, 0]) == 0
        self.assertRaises(TypeError, lambda: weightedCosSim(Vector([1, 1, 1]).data, Vector([1, 1]).data, [1, 1]))
        self.assertRaises(TypeError, lambda: weightedCosSim(Vector([1, 1]).data, Vector([1, 1]).data, [1, 1, 1]))
        print '\nPassed WeightedCosSim tests!'

    def testVector(self):
        assert repr(Vector([1, 1, 2, 2])) == repr([1, 1, 2, 2])
        assert Vector([1, 1, 3, 5]) + Vector([3, 2, 5, 0]) == Vector([4, 3, 8, 5])
        assert Vector([1, 1, 3, 5]) + Vector([3, 2, 5, 1]) != Vector([4, 3, 8, 5])
        assert Vector([1, 1, 3, 5]) - Vector([3, 2, 5, 0]) == Vector([-2, -1, -2, 5])
        assert Vector([1, 1, 3, 5]) - Vector([3, 2, 5, 1]) != Vector([-2, -1, -2, 5])
        assert Vector([1, 1, 3, 5]) * 2 == Vector([2, 2, 6, 10])
        assert Vector([1, 1, 3, 6]) * 2 != Vector([2, 2, 6, 10])
        assert Vector([1, 1, 3, 5]) / 2 == Vector([.5, .5, 1.5, 2.5])
        assert Vector([1, 1, 3, 6]) / 2 != Vector([.5, .5, 1.5, 2.5])
        assert Vector([11, 12, 13, 14])[1] == 12
        v = Vector([11, 12, 13, 14])
        v[3] = 2
        assert v == Vector([11, 12, 13, 2])
        assert len(v) == 4
        assert Vector.vector_sum([Vector([1, 1, 2]), Vector([3, 3, 2]), Vector([8, 7, -1])]) == Vector([12, 11, 3])
        print '\nPassed Vector tests!'

    def testWeightedLength(self):
        assert weightedLength(Vector([1]), [1]) == math.sqrt(1)
        assert weightedLength(Vector([1, 1, 1, 1]), [1, 1, 1, 1]) == math.sqrt(4)
        assert weightedLength(Vector([1, 1, 1, 1]), [0.5, 0.5, 0.5, 0.5]) == math.sqrt(2)
        assert weightedLength(Vector([11, 12]), [0, 0]) == 0
        assert weightedLength(Vector([-2, -2.5]), [1, 1]) == math.sqrt(10.25)
        assert weightedLength(Vector([-2, 0]), [1, 1]) == math.sqrt(4)
        assert weightedLength(Vector([]), []) == 0
        self.assertRaises(TypeError, lambda: weightedLength(Vector([-2, 0]), [1, 1, 1]))
        self.assertRaises(TypeError, lambda: weightedLength(Vector([1, 1, 1]), [1, 1]))
        print '\nPassed WeightedLength tests!'


def main():
    unittest.main()


if __name__ == '__main__':
    main()
