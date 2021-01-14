import numpy as np
import pandas as pd
import plotly.offline as pyo


data = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
pyo.plot([{
    'x':data.index,
    'y': data[col],
    'name':col
}for col in data.columns])