import pandas as pd
from sklearn.impute import SimpleImputer

# Example DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
}
df = pd.DataFrame(data)

# Handling missing values using mean imputation
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("Original DataFrame:")
print(df)
print("\nDataFrame after Imputation:")
print(df_imputed)