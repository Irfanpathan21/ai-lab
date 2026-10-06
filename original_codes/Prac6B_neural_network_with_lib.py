# =====================================================================
# PRACTICAL 6B: NEURAL NETWORK WITH LIBRARY (Scikit-Learn)
# 4-STEP ML FRAMEWORK (Hinglish Guide)
# Goal: Iris flower dataset ko Multi-Layer Perceptron (MLP) Neural
#       Network se train karke accuracy nikaalna.
# =====================================================================

import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# STEP 1: DATA LOAD KARNA (Input X aur Output y)
# Iris dataset me 3 tarah ke phool (Setosa, Versicolor, Virginica) hote hain.
iris = load_iris()
X = iris.data    # 4 features: sepal/petal length aur width
y = iris.target  # Labels: 0, 1, ya 2

# STEP 2: DATA KO TRAIN AUR TEST ME BAANTNA (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# STEP 3: NEURAL NETWORK MODEL BANANA
# MLPClassifier = Multi Layer Perceptron (Feedforward Neural Network)
# hidden_layer_sizes=(10,) -> Ek hidden layer jisme 10 neurons hain.
model = MLPClassifier(
    hidden_layer_sizes=(10,),
    max_iter=1000,
    random_state=42
)

# STEP 4: MODEL KO FIT / TRAIN KARNA (Training)
# Model inputs aur targets ke beech ke patterns seekhta hai.
model.fit(X_train, y_train)

# STEP 5: TEST DATA PAR PREDICTION AUR ACCURACY EVALUATION
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Model Test Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Optional Exam Question: "Predict a new sample"
sample = [[5.1, 3.5, 1.4, 0.2]]
predicted_class = model.predict(sample)
print(f"Sample Flower Prediction: {iris.target_names[predicted_class[0]]}")
