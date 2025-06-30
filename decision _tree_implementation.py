# 1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 2. Load Dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Build Decision Tree Model
dtree = DecisionTreeClassifier(criterion='entropy', random_state=42)
dtree.fit(X_train, y_train)

# 5. Make Predictions
y_pred = dtree.predict(X_test)

# 6. Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# 7. Visualize the Decision Tree (using matplotlib)
plt.figure(figsize=(15,10))
plot_tree(dtree, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree Visualization (Iris Dataset)")
plt.show()

# Optional: Export to Graphviz format (for better quality visuals)
from sklearn.tree import export_graphviz
import graphviz

dot_data = export_graphviz(dtree, out_file=None,
                           feature_names=iris.feature_names,
                           class_names=iris.target_names,
                           filled=True, rounded=True,
                           special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("iris_decision_tree")  # Saves as PDF
graph.view()
