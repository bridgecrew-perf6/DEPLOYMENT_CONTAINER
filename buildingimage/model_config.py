import json
import numpy as np
import os



def load_model_mappings(model_name):
  return list(json.load(open(os.path.join('data',model_name+'-mapping.json'))).keys())