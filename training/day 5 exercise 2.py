import pandas as pd

# Task 1: Load a dataset with missing values, identify columns with missing values, and fill them with the mean of the column.
# For the purpose of this example, let's create a sample dataset with missing values.

# Sample data with missing values
data_with_missing_values = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, None],
    'C': [1, 2, 3, 4, 5]
}
df_with_missing = pd.DataFrame(data_with_missing_values)

print("Original DataFrame with Missing Values:")
print(df_with_missing)

# Identify columns with missing values
missing_columns = df_with_missing.columns[df_with_missing.isnull().any()]
print("\nColumns with Missing Values:", missing_columns)

# Fill missing values with the mean of the column
df_filled = df_with_missing.copy()
for col in missing_columns:
    df_filled[col].fillna(df_filled[col].mean(), inplace=True)

print("\nDataFrame after Filling Missing Values:")
print(df_filled)

# Task 2: Load a dataset where numerical columns are mistakenly read as strings and convert them to appropriate data types.
# For the purpose of this example, let's create a sample dataset with numerical columns as strings.

# Sample data with numerical columns as strings
data_with_strings = {
    'A': ['1', '2', '3', '4', '5'],
    'B': ['6', '7', '8', '9', '10'],
    'C': ['11.0', '12.1', '13.2', '14.3', '15.4']
}
df_with_strings = pd.DataFrame(data_with_strings)

print("\nOriginal DataFrame with Numerical Columns as Strings:")
print(df_with_strings)

# Convert columns to appropriate data types
df_converted = df_with_strings.copy()
df_converted['A'] = pd.to_numeric(df_converted['A'])
df_converted['B'] = pd.to_numeric(df_converted['B'])
df_converted['C'] = pd.to_numeric(df_converted['C'])

print("\nDataFrame after Converting to Appropriate Data Types:")
print(df_converted)

# Task 3: Load a dataset with duplicate rows, remove the duplicates, and display the cleaned DataFrame.
# For the purpose of this example, let's create a sample dataset with duplicate rows.

# Sample data with duplicate rows
data_with_duplicates = {
    'A': [1, 2, 2, 3, 4],
    'B': [5, 6, 6, 7, 8],
    'C': [9, 10, 10, 11, 12]
}
df_with_duplicates = pd.DataFrame(data_with_duplicates)

print("\nOriginal DataFrame with Duplicate Rows:")
print(df_with_duplicates)

# Remove duplicate rows
df_no_duplicates = df_with_duplicates.drop_duplicates()

print("\nDataFrame after Removing Duplicate Rows:")
print(df_no_duplicates)
