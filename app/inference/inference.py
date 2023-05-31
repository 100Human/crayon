import os 
from io import StringIO
import pickle as pkl
import pandas as pd

from inference import preprocess_utils
import config


def model_fn(model_dir):
    model_file = os.path.join(model_dir, config.MODEL_FILENAME)
    if os.path.exists(model_file):
        with open(model_file, 'rb') as file:
            model = pkl.load(file)
    else:
        raise ValueError(f"{model_file} does not exist")
    
    prerocessing_conf_file = os.path.join(model_dir, config.PREPROCESS_FILENAME)
    if os.path.exists(prerocessing_conf_file):
        with open(prerocessing_conf_file, 'rb') as file:
            prerocessing_conf = pkl.load(file)
    else:
        raise ValueError(f"{prerocessing_conf_file} does not exist")

    return model, prerocessing_conf


def transform_fn(model, payload, content_type, encoders):
    output = None
    if content_type == 'text/csv':
        df = pd.read_csv(StringIO(payload))   
    else:
        raise ValueError(f'Unsupported content_type: {content_type}')
        
    for feature, encoder in encoders.items():
        df, _ = preprocess_utils.encode_categorical_col(df, feature, encoder=encoder)
     
    predictions = model.predict(df).astype(str)

    return list(predictions)

    
    