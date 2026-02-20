import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    label_pattern = r'^[a-zA-Z_]+$'

    # Validation new column name
    if not re.match(label_pattern, new_column):
        return pd.DataFrame([])
    
    # Validation column names
    for col in df.columns:
        if not re.match(label_pattern, col):
            return pd.DataFrame([])
        
    # Parsing expression- role
    pattern = r'^\s*([a-zA-Z_]+)\s*([+\-*])\s*([a-zA-Z_]+)\s*$'
    match = re.match(pattern, role)
    if not match:
        return pd.DataFrame([])
    
    left_col = match.group(1)
    operator = match.group(2)
    right_col = match.group(3)

    # Verification if columns exists in df
    if left_col not in df.columns or right_col not in df.columns:
        return pd.DataFrame([])
    
    result_df = df.copy()

    if operator == '+':
        result_df[new_column] = df[left_col] + df[right_col]
    elif operator == '-':
        result_df[new_column] = df[left_col] - df[right_col]
    elif operator == '*':
        result_df[new_column] = df[left_col] * df[right_col]

    return result_df


