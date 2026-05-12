import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

# Load Dataset
df = pd.read_csv("placement.csv")

# Features
X = df[['CGPA', 'IQ', 'Communication', 'Internship']]

# Target
y = df['Placed']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
models = {

    "Logistic Regression":
    LogisticRegression(),

    "KNN":
    KNeighborsClassifier(),

    "SVM":
    SVC(probability=True),

    "Decision Tree":
    DecisionTreeClassifier(),

    "Naive Bayes":
    GaussianNB()
}

accuracy_results = {}

# Train Models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    accuracy_results[name] = accuracy * 100

    filename = f"models/{name}.pkl"

    joblib.dump(model, filename)

# Accuracy Output
print("\nMODEL ACCURACY RESULTS\n")

for model_name, accuracy in accuracy_results.items():

    print(model_name, ":", accuracy)