# Install surprise if not already installed
# pip install scikit-surprise

# Import required libraries
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate
from surprise import accuracy

# Step 1: Load sample dataset (MovieLens for demonstration)
# Or you can load your own CSV with user-item-rating format
data = Dataset.load_builtin('ml-100k')  # MovieLens 100k dataset
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Step 2: Build and train the model (Matrix Factorization - SVD)
model = SVD()
model.fit(trainset)

# Step 3: Make predictions
predictions = model.test(testset)

# Step 4: Evaluate the model
print("Root Mean Squared Error (RMSE):", accuracy.rmse(predictions))
print("Mean Absolute Error (MAE):", accuracy.mae(predictions))

# Step 5: Show top N recommendations for a given user
from collections import defaultdict

def get_top_n(predictions, n=5):
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n

top_n = get_top_n(predictions, n=5)

# Display top 5 recommended items for first 3 users
for uid, user_ratings in list(top_n.items())[:3]:
    print(f"\nTop recommendations for User {uid}:")
    for (iid, rating) in user_ratings:
        print(f"  Item {iid} with predicted rating {rating:.2f}")