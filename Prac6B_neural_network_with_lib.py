# =====================================================================
# PRACTICAL 6B: NEURAL NETWORK WITH LIBRARY (Scikit-Learn)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: 5-Step Scikit-Learn ML Pipeline
#   Step 1: Load Dataset
#   Step 2: Train-Test Split
#   Step 3: Initialize Model (MLPClassifier)
#   Step 4: Train / Fit (model.fit)
#   Step 5: Predict & Evaluate (accuracy_score & classification_report)
#
# EXAM ADAPTATION GUIDE:
#   - Change Classifier:
#       Decision Tree: `from sklearn.tree import DecisionTreeClassifier`
#       KNN:           `from sklearn.neighbors import KNeighborsClassifier`
#       SVM:           `from sklearn.svm import SVC`
#   - Change Dataset:  `from sklearn.datasets import load_wine`
# =====================================================================

import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Data
iris = load_iris()
X, y = iris.data, iris.target
print(f"Step 1: Loaded Dataset ({X.shape[0]} samples, {X.shape[1]} features)")

# Step 2: Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Step 2: Split Data ({len(X_train)} Train, {len(X_test)} Test)")

# Step 3: Initialize Neural Network Model (1 hidden layer with 10 neurons)
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

# Step 4: Train Model
print("Step 3 & 4: Training MLPClassifier Neural Network...")
model.fit(X_train, y_train)

# Step 5: Predict and Evaluate Accuracy + Classification Report
print("\nStep 5: Evaluation Results:")
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Test Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Predict a New Sample
sample = [[5.1, 3.5, 1.4, 0.2]]
pred_class = model.predict(sample)[0]
print(f"Sample Flower Prediction: {iris.target_names[pred_class]}")
