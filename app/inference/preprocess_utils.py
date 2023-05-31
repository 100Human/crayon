import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def encode_categorical_col(df, col, categories='auto', encoder=None):
    if encoder is None:
        encoder = OneHotEncoder(categories=categories, handle_unknown='ignore', dtype=bool, sparse_output=False)
        ecoded_data = encoder.fit_transform(df[[col]])
    else:
        ecoded_data = encoder.transform(df[[col]])
    encoded_feature_names = encoder.get_feature_names_out()
    encoded_df = pd.DataFrame(ecoded_data, columns=encoded_feature_names)

    return pd.concat([df.drop(columns=[col]), encoded_df], axis=1), encoder
