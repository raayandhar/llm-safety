from base_gcg.baseline import Attack
import numpy as np
import torch

class BaseGCG(Attack):

    def __init__(self, config, 
