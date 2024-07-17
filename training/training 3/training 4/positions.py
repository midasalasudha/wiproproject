'''
DataFrame Attributes and Methods
Attributes, Methods

'''

print(df_from_dict.index)  # RangeIndex(start=0, stop=3, step=1)
print(df_from_dict.columns)  # Index(['Name', 'Age', 'City'], dtype='object')
print(df_from_dict.values)  # 2D array of the DataFrame values

print(df_from_dict.head(2))  # First 2 rows
print(df_from_dict.tail(1))  # Last row
print(df_from_dict.info())  # Information about the DataFrame
print(df_from_dict.describe())  # Statistical summary of numeric columns

# Indexing and Slicing DataFrames
print(df_from_dict['Name'])
print(df_from_dict[['Name', 'City']])

print(df_from_dict.iloc[0])  # By integer index
print(df_from_dict.loc[0])  # By label index (same as iloc in this case)

print(df_from_dict.iloc[0:2])  # First 2 rows
print(df_from_dict.loc[0:1])  # Rows with labels 0 and 1

# Single column selection:
print(df_from_dict['Age'])

# Multiple columns selection:
print(df_from_dict[['Name', 'City']])

# Row selection using labels (loc):
print(df_from_dict.loc[0])
print(df_from_dict.loc[0:2])

# Row selection using integer positions (iloc):
print(df_from_dict.iloc[0])
print(df_from_dict.iloc[0:2])
