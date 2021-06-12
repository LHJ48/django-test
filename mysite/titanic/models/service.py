import pandas as pd
import numpy as np
from mysite.titanic.models.dataset import Dataset

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

