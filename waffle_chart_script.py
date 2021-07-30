import pandas as pd
import sys

import matplotlib.pyplot as plt
from pywaffle import Waffle

data = pd.DataFrame(
{
'labels': ['psbA-trnH', 'ITS2', 'psbA-trnH+ITS2'],
'Company 1': [44, 50, 61],
'Company 2': [37, 56, 71],
'Company 3': [26, 39, 44],
'Company 4': [59, 51, 75],
'Company 5': [63, 63, 100],
},
).set_index('labels')

print(data)

fig = plt.figure(
    FigureClass=Waffle,
    plots={
    '511': {
    'values': data['Company 1'],
    'labels': [f"{k} ({v})" for k, v in data['Company 1'].items()],
    'legend': {
    'loc': 'upper left',
    'bbox_to_anchor': (1.3, 1),
    'fontsize': 8,
    },
    'title': {
    'label': 'Company 1',
    'loc': 'left'
    }
    },
    '512': {
    'values': data['Company 2'],
    'labels': [f"{k} ({v})" for k, v in data['Company 2'].items()],
    'legend': {
    'loc': 'upper left',
    'bbox_to_anchor': (1.3, 1),
    'fontsize': 8,
    },
    'title': {
    'label': 'Company 2',
    'loc': 'left'
    }
    },
    '513': {
    'values': data['Company 3'],
    'labels': [f"{k} ({v})" for k, v in data['Company 3'].items()],
    'legend': {
    'loc': 'upper left',
    'bbox_to_anchor': (1.3, 1),
    'fontsize': 8,
    },
    'title': {
    'label': 'Company 3',
    'loc': 'left'
    }
    },
    '514': {
    'values': data['Company 4'],
    'labels': [f"{k} ({v})" for k, v in data['Company 4'].items()],
    'legend': {
    'loc': 'upper left',
    'bbox_to_anchor': (1.3, 1),
    'fontsize': 8,
    },
    'title': {
    'label': 'Company 4',
    'loc': 'left'
    }
    },
    '515': {
    'values': data['Company 5'],
    'labels': [f"{k} ({v})" for k, v in data['Company 5'].items()],
    'legend': {
    'loc': 'upper left',
    'bbox_to_anchor': (1.3, 1),
    'fontsize': 8,
    },
    'title': {
    'label': 'Company 5',
    'loc': 'left'
    }
    },
    },
    rows=5,
    #columns=25,
    icon_size=8,
    #icons='seedling',
    colors=("orange", "cornflowerblue", "navy"), # shared parameter among subplots
    figsize=(9, 5) # figsize is a parameter of plt.figure
)

#plt.show()
plt.savefig("fig1_paperone.svg")
