import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from typing import List, Tuple, Optional, Union

# ----------------------- File Handling Functions -----------------------

def read_csv_file(filepath: str) -> pd.DataFrame:
    """
    Reads a CSV file into a Pandas DataFrame.
    """
    # Check if the file exists at the given path
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} does not exist.")
    
    # Read CSV using pandas and return the DataFrame
    return pd.read_csv(filepath)

def save_dataframe_to_csv(df: pd.DataFrame, filepath: str) -> None:
    """
    Saves a DataFrame to a CSV file.
    """
    # Save the DataFrame to CSV without the index column
    df.to_csv(filepath, index=False)
    
    # Confirm successful saving
    print(f"Data saved to {filepath}")

# ----------------------- Data Inspection Functions -----------------------

def get_basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns basic statistics (mean, median, std) for numeric columns.
    """
    # Use pandas describe to get summary statistics
    return df.describe()

def missing_data_report(df: pd.DataFrame) -> pd.Series:
    """
    Reports the number of missing values per column.
    """
    # Count missing (NaN) values in each column
    return df.isnull().sum()

# ----------------------- Data Cleaning Functions -----------------------

def fill_missing_with_mean(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Fills missing values with mean for specified columns.
    """
    # Iterate through the given columns
    for col in columns:
        # Only fill if the column is numeric
        if df[col].dtype in [np.float64, np.int64]:
            mean_val = df[col].mean()
            df[col].fillna(mean_val, inplace=True)  # Replace NaNs with mean
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from the DataFrame.
    """
    # Drop duplicate rows and return the cleaned DataFrame
    return df.drop_duplicates()

# ----------------------- Statistical Functions -----------------------

def calculate_correlation(df: pd.DataFrame, method: str = 'pearson') -> pd.DataFrame:
    """
    Calculates the correlation matrix using specified method.
    """
    # Compute correlation matrix using specified method
    return df.corr(method=method)

def standardize_column(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Standardizes a single column (z-score).
    """
    # Calculate mean and std for the column
    mean = df[column].mean()
    std = df[column].std()
    
    # Apply z-score standardization formula
    return (df[column] - mean) / std

# ----------------------- Data Transformation Functions -----------------------

def encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    One-hot encodes all categorical columns.
    """
    # Use get_dummies to encode categoricals, drop first to avoid dummy trap
    return pd.get_dummies(df, drop_first=True)

def normalize_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Normalizes specified columns to range [0,1].
    """
    # Normalize each selected column to range [0, 1]
    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    return df

# ----------------------- Visualization Functions -----------------------

def plot_histogram(df: pd.DataFrame, column: str) -> None:
    """
    Plots a histogram of a specified column.
    """
    # Set figure size
    plt.figure(figsize=(8, 5))
    
    # Plot histogram with density curve
    sns.histplot(df[column], kde=True, color='skyblue')
    
    # Add labels and grid
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Plots a heatmap of the correlation matrix.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))
    
    # Generate and show heatmap
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

# ----------------------- Utility Functions -----------------------

def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Detects outliers in a column using the IQR method.
    """
    # Calculate Q1 and Q3
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier boundaries
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Flag outliers outside the boundaries
    df['is_outlier'] = ~df[column].between(lower, upper)
    return df

def rename_columns(df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
    """
    Renames columns in the DataFrame.
    """
    # Use pandas rename function with dictionary mapping
    return df.rename(columns=rename_map)

def summarize_dataframe(df: pd.DataFrame) -> None:
    """
    Prints a summary of the DataFrame structure.
    """
    # Print number of rows and columns
    print("DataFrame Shape:", df.shape)

    # Print data types and non-null counts
    print("\nColumn Info:")
    print(df.info())

    # Display first 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

