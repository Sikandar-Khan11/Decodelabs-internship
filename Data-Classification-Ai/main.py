# ==========================================
# Project 2: Data Classification Using AI
# Author: Sikandar Khan
# ==========================================

# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("=" * 50)
print("      DATA CLASSIFICATION USING AI")
print("=" * 50)

# -----------------------------
# Load the Iris dataset
# -----------------------------
iris = load_iris()

# Create a DataFrame
data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target column
data["Species"] = iris.target

print("\nFirst Five Rows of Dataset:\n")
print(data.head())

# -----------------------------
# Dataset Information
# -----------------------------
print("\nDataset Information:\n")
print(data.info())

print("\nDataset Shape:", data.shape)

print("\nMissing Values:\n")
print(data.isnull().sum())

# -----------------------------
# Features and Target
# -----------------------------
X = iris.data
y = iris.target

# -----------------------------
# Split the Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# -----------------------------
# Train the Model
# -----------------------------
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# -----------------------------
# Make Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy : {:.2f}%".format(accuracy * 100))

# -----------------------------
# Predict New Flower
# -----------------------------
print("\nPrediction Example")

sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample)

print("Flower Measurements :", sample[0])
print("Predicted Class :", iris.target_names[prediction][0])

print("\nProject Completed Successfully!")