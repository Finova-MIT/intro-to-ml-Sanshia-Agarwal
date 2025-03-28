import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Display basic information about the dataset
print(titanic.info())

# Display summary statistics
print(titanic.describe(include='all'))

# Check for missing values
print(titanic.isnull().sum())

# Visualize the distribution of the 'age' column
sns.histplot(titanic['age'].dropna(), kde=True)
plt.title('Age Distribution')
plt.show()

# Countplot for 'class' column
sns.countplot(x='class', data=titanic)
plt.title('Passenger Class Distribution')
plt.show()

# Heatmap of missing values
sns.heatmap(titanic.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()