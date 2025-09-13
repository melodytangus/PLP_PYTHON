# Task 1: Load and Explore the Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

try:
    iris = load_iris(as_frame=True)
    df = iris.frame  # DataFrame version
except FileNotFoundError as e:
    print("Error: Dataset not found!", e)
except Exception as e:
    print("Error loading dataset:", e)

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values in dataset:")
print(df.isnull().sum())

df = df.dropna()
print("\nAfter cleaning, shape:", df.shape)

# Task 2: Data Visualization

print("\nBasic Statistics:")
print(df.describe())

group_means = df.groupby("target").mean()
print("\nMean of numerical columns grouped by species:")
print(group_means)
print("\nObservations:")
print("- Setosa flowers generally have smaller petal length and width.")
print("- Virginica flowers tend to have the largest petal dimensions.")
print("- Sepal length increases gradually across species.")