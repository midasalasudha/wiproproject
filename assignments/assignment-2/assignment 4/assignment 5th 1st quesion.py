import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Step 1: Load the Titanic dataset
file_path = 'titanic.csv'  # Adjust the path as needed
titanic_df = pd.read_csv(file_path)

# Step 2: Identify and handle missing values
# Handle missing values in Age using median
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)

# Handle missing values in Embarked using mode
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0], inplace=True)

# Handle missing values in Cabin using a placeholder
titanic_df['Cabin'].fillna('Unknown', inplace=True)

# Step 3: Standardize the numerical features (Age, Fare)
scaler_standard = StandardScaler()
titanic_df[['Age_standard', 'Fare_standard']] = scaler_standard.fit_transform(titanic_df[['Age', 'Fare']])

# Step 4: Normalize the numerical features (Age, Fare)
scaler_minmax = MinMaxScaler()
titanic_df[['Age_normalized', 'Fare_normalized']] = scaler_minmax.fit_transform(titanic_df[['Age', 'Fare']])

# Step 5: Compare the distributions using histograms
plt.figure(figsize=(12, 8))

# Original Age and Fare
plt.subplot(3, 2, 1)
plt.hist(titanic_df['Age'], bins=30, edgecolor='k')
plt.title('Original Age')

plt.subplot(3, 2, 2)
plt.hist(titanic_df['Fare'], bins=30, edgecolor='k')
plt.title('Original Fare')

# Standardized Age and Fare
plt.subplot(3, 2, 3)
plt.hist(titanic_df['Age_standard'], bins=30, edgecolor='k')
plt.title('Standardized Age')

plt.subplot(3, 2, 4)
plt.hist(titanic_df['Fare_standard'], bins=30, edgecolor='k')
plt.title('Standardized Fare')

# Normalized Age and Fare
plt.subplot(3, 2, 5)
plt.hist(titanic_df['Age_normalized'], bins=30, edgecolor='k')
plt.title('Normalized Age')

plt.subplot(3, 2, 6)
plt.hist(titanic_df['Fare_normalized'], bins=30, edgecolor='k')
plt.title('Normalized Fare')

plt.tight_layout()
plt.show()
