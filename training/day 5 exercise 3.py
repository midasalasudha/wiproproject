import pandas as pd

# Create sample DataFrames for the exercise

# DataFrame 1
data1 = {
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
}
df1 = pd.DataFrame(data1)

# DataFrame 2
data2 = {
    'id': [3, 4, 5, 6],
    'age': [23, 34, 45, 56]
}
df2 = pd.DataFrame(data2)

# Task 1: Perform an inner join on the 'id' column
inner_join_df = pd.merge(df1, df2, on='id', how='inner')
print("Inner Join DataFrame:")
print(inner_join_df)

# Task 2: Perform an outer join on the 'id' column
outer_join_df = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter Join DataFrame:")
print(outer_join_df)

# Task 3: Concatenate two DataFrames vertically
# Create another set of sample DataFrames with the same columns

# DataFrame 3
data3 = {
    'id': [7, 8, 9],
    'name': ['Eve', 'Frank', 'Grace']
}
df3 = pd.DataFrame(data3)

# DataFrame 4
data4 = {
    'id': [10, 11, 12],
    'name': ['Hannah', 'Ivy', 'Jack']
}
df4 = pd.DataFrame(data4)

# Concatenate the DataFrames vertically
concatenated_df = pd.concat([df3, df4], ignore_index=True)
print("\nConcatenated DataFrame:")
print(concatenated_df)
