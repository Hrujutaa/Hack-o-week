import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("Airbnb_Open_Data.csv", low_memory=False)

print("First 5 Rows")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)



df.drop_duplicates(inplace=True)


df.columns = df.columns.str.strip()


if 'price' in df.columns:
    df['price'] = (
        df['price']
        .astype(str)
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
    )
    df['price'] = pd.to_numeric(df['price'], errors='coerce')


numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col].fillna(df[col].mean(), inplace=True)


categorical_columns = df.select_dtypes(include='object').columns

for col in categorical_columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nCleaned Dataset Shape")
print(df.shape)



print("\nSummary Statistics")
print(df.describe())


if 'room type' in df.columns:
    print("\nAverage Price by Room Type")
    print(df.groupby('room type')['price'].mean())

#
plt.figure(figsize=(8,5))
plt.hist(df['price'], bins=30)
plt.title("Distribution of Airbnb Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Bar Chart
room_counts = df['room type'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(room_counts.index, room_counts.values)
plt.title("Number of Listings by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Pie Chart
plt.figure(figsize=(7,7))
plt.pie(room_counts.values,
        labels=room_counts.index,
        autopct='%1.1f%%')
plt.title("Room Type Distribution")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df['availability 365'], df['price'])
plt.title("Availability vs Price")
plt.xlabel("Availability (Days)")
plt.ylabel("Price")
plt.show()



# Histogram
plt.figure(figsize=(8,5))
sns.histplot(df['price'], bins=30, kde=True)
plt.title("Price Distribution")
plt.show()

# Boxplot
plt.figure(figsize=(10,5))
sns.boxplot(x='room type', y='price', data=df)
plt.xticks(rotation=45)
plt.title("Room Type vs Price")
plt.show()

# Countplot
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='room type')
plt.xticks(rotation=45)
plt.title("Room Type Count")
plt.show()

# Heatmap
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()