from lib import utils
from lib.utils import weightedCosSim, weightedCorrelationSim
import math


class Kernel:
    def getSim(self, vector1, vector2):
        pass


class WeightedComponentBased:
    def getComponentsAndWeights(self, vector1, vector):
        pass


MEAN_WEIGHTED_COSINE = .6135
STD_DEV_WEIGHTED_COSINE = .0811


class WeightedCosineKernel(Kernel, WeightedComponentBased):
    def __init__(self, weights, subtractMean=False, divideByStdDev=False):
        self.weights = weights
        self.subtractMean = subtractMean
        self.divideByStdDev = divideByStdDev


    def getSim(self, vector1, vector2):
        try:
            sim = weightedCosSim(vector1.data, vector2.data, self.weights)
            if self.subtractMean:
                sim = sim - MEAN_WEIGHTED_COSINE
            if self.divideByStdDev:
                sim = sim / STD_DEV_WEIGHTED_COSINE
            return sim
        except StandardError:
            # if len(vector1) != len(vector2) or len(self.weights) != len(vector1):
            return 0
            # raise Exception("differing vector lengths")


    def getComponentsAndWeights(self, vector1, vector2):
        if len(vector1) != len(vector2) or len(self.weights) != len(vector1):
            return 0
            # raise Exception("differing vector lengths")
        return [(math.sqrt(vector1[i] * vector2[i]), self.weights[i]) for i in range(len(vector1))]


class WeightedCorrelationKernel(Kernel, WeightedComponentBased):
    def __init__(self, weights):
        self.weights = weights

    def getSim(self, vector1, vector2):
        if len(vector1) != len(vector2) or len(self.weights) != len(vector1):
            return 0
            # raise Exception("differing vector lengths")
        return weightedCorrelationSim(vector1.data, vector2.data, self.weights)

    def getComponentsAndWeights(self, vector1, vector2):
        if len(vector1) != len(vector2) or len(self.weights) != len(vector1):
            return 0
            # raise Exception("differing vector lengths")
        mean1 = utils.mean(vector1)
        mean2 = utils.mean(vector2)
        return [(math.sqrt((vector1[i] - mean1) * (vector2[i] - mean2)), self.weights[i]) for i in range(len(vector1))]
        
