import pandas as pd

# Load CSV file into a DataFrame
csv_df = pd.read_csv('data.csv')

# Load JSON file into a DataFrame
json_df = pd.read_json('data.json')

# Load Excel file into a DataFrame
excel_df = pd.read_excel('data.xlsx')

# Ask the user how many rows to display from the DataFrames
num_rows = int(input("Enter the number of rows to display: "))

# Display the specified number of rows from each DataFrame
print("\nCSV DataFrame:")
print(csv_df.head(num_rows))

print("\nJSON DataFrame:")
print(json_df.head(num_rows))

print("\nExcel DataFrame:")
print(excel_df.head(num_rows))
