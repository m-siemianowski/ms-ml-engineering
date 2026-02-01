
import yaml
import pandas as pd

def load_config(path='config.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_data(path, date_col='date'):
    """
    Load raw time series data from CSV file.

    Parameters
    ----------
    path : str or Path
        Path to CSV file with time series data.
    date_col : str, default "date"
        Name of the column containing datetime information.

    Returns
    -------
    pd.DataFrame
        DataFrame sorted by date with at least:
        - 'date' column (datetime)
        - 'close' column (float)
    """
    df = pd.read_csv(path)
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).reset_index(drop=True)
    return df
