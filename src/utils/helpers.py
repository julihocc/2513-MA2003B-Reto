"""
Helper utilities and common functions.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

from src.utils.constants import (
    DEFAULT_ENCODING,
    DATE_FORMAT_INPUT,
    DECIMAL_SEPARATOR_INPUT,
    DECIMAL_SEPARATOR_OUTPUT,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_csv(
    file_path: Union[str, Path],
    encoding: str = DEFAULT_ENCODING,
    **kwargs
) -> pd.DataFrame:
    """
    Load CSV file with standard encoding and error handling.

    Args:
        file_path: Path to CSV file
        encoding: File encoding
        **kwargs: Additional arguments for pd.read_csv

    Returns:
        DataFrame

    Example:
        >>> df = load_csv('data/raw/ventas.csv')
    """
    try:
        df = pd.read_csv(file_path, encoding=encoding, **kwargs)
        logger.info(f"Loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        raise


def save_csv(
    df: pd.DataFrame,
    file_path: Union[str, Path],
    index: bool = False,
    **kwargs
) -> None:
    """
    Save DataFrame to CSV with standard settings.

    Args:
        df: DataFrame to save
        file_path: Output path
        index: Whether to include index
        **kwargs: Additional arguments for df.to_csv

    Example:
        >>> save_csv(df, 'data/processed/clean_data.csv')
    """
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(file_path, index=index, encoding=DEFAULT_ENCODING, **kwargs)
        logger.info(f"Saved {len(df)} rows to {file_path}")
    except Exception as e:
        logger.error(f"Error saving {file_path}: {e}")
        raise


def parse_spanish_decimal(value: Union[str, float, int]) -> float:
    """
    Parse decimal with comma separator (Spanish format) to float.

    Args:
        value: Value to parse (string with comma or numeric)

    Returns:
        Float value

    Example:
        >>> parse_spanish_decimal("12,24")
        12.24
        >>> parse_spanish_decimal(12.24)
        12.24
    """
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        return float(value.replace(DECIMAL_SEPARATOR_INPUT, DECIMAL_SEPARATOR_OUTPUT))
    return float(value)


def parse_spanish_date(
    date_str: str,
    format: str = DATE_FORMAT_INPUT,
    errors: str = "coerce"
) -> pd.Timestamp:
    """
    Parse date string in Spanish format.

    Args:
        date_str: Date string to parse
        format: Expected date format
        errors: How to handle errors ('raise', 'coerce', 'ignore')

    Returns:
        Pandas Timestamp

    Example:
        >>> parse_spanish_date("31/01/2024")
        Timestamp('2024-01-31 00:00:00')
    """
    try:
        return pd.to_datetime(date_str, format=format, errors=errors)
    except Exception as e:
        if errors == "raise":
            raise
        logger.warning(f"Could not parse date '{date_str}': {e}")
        return pd.NaT


def get_memory_usage(df: pd.DataFrame, detailed: bool = False) -> Union[float, pd.Series]:
    """
    Get memory usage of DataFrame.

    Args:
        df: DataFrame to analyze
        detailed: Whether to return detailed breakdown by column

    Returns:
        Total memory in MB or Series of memory by column

    Example:
        >>> memory_mb = get_memory_usage(df)
        >>> print(f"DataFrame uses {memory_mb:.2f} MB")
    """
    memory_bytes = df.memory_usage(deep=True)
    if detailed:
        return memory_bytes / 1024**2  # Convert to MB
    return memory_bytes.sum() / 1024**2  # Total in MB


def reduce_memory_usage(df: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
    """
    Reduce memory usage by downcasting numeric types.

    Args:
        df: DataFrame to optimize
        verbose: Whether to print memory reduction info

    Returns:
        Optimized DataFrame

    Example:
        >>> df_optimized = reduce_memory_usage(df)
    """
    start_mem = get_memory_usage(df)

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()

            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)

            elif str(col_type)[:5] == "float":
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    end_mem = get_memory_usage(df)
    reduction = 100 * (start_mem - end_mem) / start_mem

    if verbose:
        logger.info(
            f"Memory reduced from {start_mem:.2f} MB to {end_mem:.2f} MB "
            f"({reduction:.1f}% reduction)"
        )

    return df


def get_dataframe_info(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Get comprehensive information about a DataFrame.

    Args:
        df: DataFrame to analyze

    Returns:
        Dictionary with DataFrame statistics

    Example:
        >>> info = get_dataframe_info(df)
        >>> print(f"Shape: {info['shape']}")
    """
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "null_counts": df.isnull().sum().to_dict(),
        "null_percentages": (df.isnull().sum() / len(df) * 100).to_dict(),
        "memory_mb": get_memory_usage(df),
        "duplicates": df.duplicated().sum(),
        "numeric_columns": list(df.select_dtypes(include=[np.number]).columns),
        "categorical_columns": list(df.select_dtypes(include=["object"]).columns),
    }


def print_dataframe_summary(df: pd.DataFrame, name: str = "DataFrame") -> None:
    """
    Print a nice summary of DataFrame.

    Args:
        df: DataFrame to summarize
        name: Name for the DataFrame

    Example:
        >>> print_dataframe_summary(df, "Ventas")
    """
    info = get_dataframe_info(df)

    print(f"\n{'='*70}")
    print(f"{name} Summary")
    print(f"{'='*70}")
    print(f"Shape: {info['shape'][0]:,} rows x {info['shape'][1]} columns")
    print(f"Memory: {info['memory_mb']:.2f} MB")
    print(f"Duplicates: {info['duplicates']:,}")
    print(f"\nData Types:")
    for dtype, cols in pd.Series(info['dtypes']).groupby(lambda x: info['dtypes'][x]):
        print(f"  {dtype}: {len(cols)} columns")
    print(f"\nNull Values:")
    nulls = pd.Series(info['null_counts'])
    if nulls.sum() == 0:
        print("  No null values")
    else:
        for col, count in nulls[nulls > 0].items():
            pct = info['null_percentages'][col]
            print(f"  {col}: {count:,} ({pct:.2f}%)")


def ensure_dir(path: Union[str, Path]) -> Path:
    """
    Ensure directory exists, create if not.

    Args:
        path: Directory path

    Returns:
        Path object

    Example:
        >>> ensure_dir('data/processed')
    """
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj


def get_timestamp(format: str = "%Y%m%d_%H%M%S") -> str:
    """
    Get current timestamp as formatted string.

    Args:
        format: datetime format string

    Returns:
        Formatted timestamp

    Example:
        >>> timestamp = get_timestamp()
        >>> print(timestamp)  # e.g., "20241121_143022"
    """
    return datetime.now().strftime(format)


def flatten_dict(d: Dict, parent_key: str = "", sep: str = "_") -> Dict:
    """
    Flatten nested dictionary.

    Args:
        d: Dictionary to flatten
        parent_key: Prefix for keys
        sep: Separator for nested keys

    Returns:
        Flattened dictionary

    Example:
        >>> d = {'a': {'b': 1, 'c': 2}}
        >>> flatten_dict(d)
        {'a_b': 1, 'a_c': 2}
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def split_train_test_temporal(
    df: pd.DataFrame,
    date_column: str,
    test_size: float = 0.2
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into train/test sets based on temporal ordering.

    Args:
        df: DataFrame to split
        date_column: Name of date column
        test_size: Proportion for test set

    Returns:
        Tuple of (train_df, test_df)

    Example:
        >>> train, test = split_train_test_temporal(df, 'Fecha', test_size=0.2)
    """
    df_sorted = df.sort_values(date_column)
    split_idx = int(len(df_sorted) * (1 - test_size))
    train_df = df_sorted.iloc[:split_idx].copy()
    test_df = df_sorted.iloc[split_idx:].copy()

    logger.info(
        f"Split data: {len(train_df)} train ({(1-test_size)*100:.0f}%), "
        f"{len(test_df)} test ({test_size*100:.0f}%)"
    )

    return train_df, test_df
