# =====================================================================
# PRACTICAL 6B: NEURAL NETWORK WITH LIBRARY (Scikit-Learn)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: 5-Step Scikit-Learn ML Pipeline
#   Step 1: Load Dataset
#   Step 2: Train-Test Split
#   Step 3: Initialize Model (MLPClassifier)
#   Step 4: Train / Fit (model.fit)
#   Step 5: Predict & Evaluate (accuracy_score)
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Change Classifier:
#       Decision Tree: `from sklearn.tree import DecisionTreeClassifier; model = DecisionTreeClassifier()`
#       KNN:           `from sklearn.neighbors import KNeighborsClassifier; model = KNeighborsClassifier()`
#       SVM:           `from sklearn.svm import SVC; model = SVC()`
#   - Change Dataset:  `from sklearn.datasets import load_wine` or `load_digits`
# =====================================================================

import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load Data
iris = load_iris()
X, y = iris.data, iris.target

# Step 2: Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Initialize Neural Network Model (1 hidden layer with 10 neurons)
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

# Step 4: Train Model
model.fit(X_train, y_train)

# Step 5: Predict and Evaluate Accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Test Accuracy: {acc * 100:.2f}%")

# Predict a New Sample
sample = [[5.1, 3.5, 1.4, 0.2]]
pred_class = model.predict(sample)[0]
print(f"Sample Prediction : {iris.target_names[pred_class]}")
