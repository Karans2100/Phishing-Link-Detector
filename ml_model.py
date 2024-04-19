import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your dataset (you should have a dataset containing features of URLs and their labels)
# Replace 'your_dataset.csv' with the path to your dataset file.

data = pd.read_csv('url_specifications.csv')

# Selecting five features from the dataset (example features)
selected_features = ['URL Length', 'Non Standard Ports', 'HTTPS', 'Special Characters', 'Numeric Characters']

# Assuming your dataset has a 'Label' column for the target variable
X = data[selected_features]  # Features
y = data['Phishing']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the SVM classifier
svm_classifier = SVC(kernel='linear', C=1)

# Train the classifier on the training data
svm_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = svm_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)
