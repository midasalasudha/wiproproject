import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the Iris dataset
file_path = 'iris.csv'  # Adjust the path as needed
iris_df = pd.read_csv(file_path)

# Step 2: Perform one-hot encoding on the Species column
iris_one_hot = pd.get_dummies(iris_df, columns=['Species'], prefix='Species')

# Step 3: Perform label encoding on the Species column
label_encoder = LabelEncoder()
iris_df['Species_label'] = label_encoder.fit_transform(iris_df['Species'])

# Step 4: Create a new feature PetalArea by multiplying PetalLength and PetalWidth
iris_df['PetalArea'] = iris_df['PetalLengthCm'] * iris_df['PetalWidthCm']

# Step 5: Create a new feature SepalArea by multiplying SepalLength and SepalWidth
iris_df['SepalArea'] = iris_df['SepalLengthCm'] * iris_df['SepalWidthCm']

# Display the resulting DataFrame with the new features and encoded columns
print(iris_df.head())
print("\nOne-hot encoded DataFrame:")
print(iris_one_hot.head())

# Visual comparison
print("\nLabel Encoded 'Species' Column:")
print(iris_df[['Species', 'Species_label']].head())
