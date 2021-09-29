"""This module is related to item_helper_class"""
# pylint: disable=import-error,invalid-name,too-many-instance-attributes
import math
import secrets
import numpy as np
import configparams as cfg


class Item:
    """This class has the structure for each solution with all required parameters"""
    max_features = -math.inf
    min_features = math.inf
    max_totalcost = -math.inf
    min_totalcost = math.inf
    max_known = -math.inf
    min_known = math.inf
    max_featuresused = -math.inf
    min_featuresused = math.inf
    costs = [secrets.randbelow(10) for _ in range(cfg.whunparams["NUM_FEATURES"])]
    defective = [bool(secrets.randbelow(2)) for _ in range(cfg.whunparams["NUM_FEATURES"])]
    used = [bool(secrets.randbelow(2)) for _ in range(cfg.whunparams["NUM_FEATURES"])]

    def __init__(self, item, eval):
        """This is the constructor for item_helper_class class"""
        self.r = -1
        self.d = -1
        self.theta = -1
        self.item = item
        self.score = 0
        self.features = sum(item)
        self.selectedpoints = 0
        self.totalcost = sum(np.multiply(item, self.costs))
        self.knowndefects = sum(np.multiply(item, self.defective))
        self.featuresused = sum(np.multiply(item, self.used))
        self.risk = eval[0]
        self.effort = eval[1]
        self.defects = eval[2]
        self.months = eval[3]
        self.zitler_rank = eval[4]

    @staticmethod
    def calc_staticfeatures(items):
        """This function updates the parameters related to static features"""
        for x in items:
            if x.features > Item.max_features:
                Item.max_features = x.features
            if x.features < Item.min_features:
                Item.min_features = x.features
            if x.totalcost > Item.max_totalcost:
                Item.max_totalcost = x.totalcost
            if x.totalcost < Item.min_totalcost:
                Item.min_totalcost = x.totalcost
            if x.knowndefects > Item.max_known:
                Item.max_known = x.knowndefects
            if x.knowndefects < Item.min_known:
                Item.min_known = x.knowndefects
            if x.featuresused > Item.max_featuresused:
                Item.max_featuresused = x.featuresused
            if x.featuresused < Item.min_featuresused:
                Item.min_featuresused = x.featuresused

    @staticmethod
    def rank_features(items, names):
        """This function is used to update the ranking parameters of all the features"""
        count = np.zeros(len(items[0].item))
        for item in items:
            count = np.add(count, item.item)
        rank = np.zeros(len(count))
        for i, v in enumerate(count):
            if v == 0:
                rank[i] = -1
                print("No", names[i])
            if v == (len(items)):
                rank[i] = -1
                print("All", names[i])
        return count, rank