import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the Titanic dataset
file_path = 'titanic.csv'  # Adjust the path as needed
titanic_df = pd.read_csv(file_path)

# Step 2: Create box plots to identify outliers in the Age and Fare columns
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=titanic_df, x='Age')
plt.title('Box Plot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(data=titanic_df, x='Fare')
plt.title('Box Plot of Fare')

plt.tight_layout()
plt.show()

# Step 3: Create histograms and KDE plots to visualize the distribution of Age and Fare
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.histplot(titanic_df['Age'].dropna(), kde=False, bins=30)
plt.title('Histogram of Age')

plt.subplot(2, 2, 2)
sns.kdeplot(data=titanic_df['Age'].dropna(), fill=True)
plt.title('KDE Plot of Age')

plt.subplot(2, 2, 3)
sns.histplot(titanic_df['Fare'], kde=False, bins=30)
plt.title('Histogram of Fare')

plt.subplot(2, 2, 4)
sns.kdeplot(data=titanic_df['Fare'], fill=True)
plt.title('KDE Plot of Fare')

plt.tight_layout()
plt.show()

# Step 4: Create scatter plots to visualize the relationship between Age and Fare, and Pclass and Survived
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(data=titanic_df, x='Age', y='Fare', hue='Survived')
plt.title('Scatter Plot of Age vs Fare')

plt.subplot(1, 2, 2)
sns.scatterplot(data=titanic_df, x='Pclass', y='Survived', hue='Survived')
plt.title('Scatter Plot of Pclass vs Survived')

plt.tight_layout()
plt.show()

# Step 5: Use pair plots to visualize the relationships between multiple numerical features
numerical_features = ['Age', 'Fare', 'Pclass', 'Survived']
sns.pairplot(titanic_df[numerical_features], hue='Survived', diag_kind='kde')
plt.show()
