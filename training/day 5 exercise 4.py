import pandas as pd

# Task 1: Group by category and compute the sum of value for each category
data1 = {
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'],
    'value': [10, 20, 30, 40, 50, 60, 70, 80]
}
df1 = pd.DataFrame(data1)

grouped_sum_df = df1.groupby('category')['value'].sum().reset_index()
print("Grouped by Category and Sum of Value:")
print(grouped_sum_df)

# Task 2: Group by category and compute the mean and standard deviation of value for each category
grouped_stats_df = df1.groupby('category')['value'].agg(['mean', 'std']).reset_index()
print("\nGrouped by Category and Mean, Standard Deviation of Value:")
print(grouped_stats_df)

# Task 3: Create a pivot table that shows the sum of value for each combination of category and subcategory
data2 = {
    'category': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C'],
    'subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'X', 'Y'],
    'value': [5, 10, 15, 20, 25, 30, 35, 40, 45]
}
df2 = pd.DataFrame(data2)

pivot_table = df2.pivot_table(values='value', index='category', columns='subcategory', aggfunc='sum', fill_value=0)
print("\nPivot Table with Sum of Value for Each Combination of Category and Subcategory:")
print(pivot_table)
