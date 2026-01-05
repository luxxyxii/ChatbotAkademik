import json
import pickle
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# ===============================
# LOAD DATASET
# ===============================
with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern.lower())   # preprocessing: lowercase
        labels.append(intent["tag"])

print(f"Total data: {len(texts)}")
print(f"Total intent: {len(set(labels))}")


# ===============================
# FEATURE EXTRACTION (TF-IDF)
# ===============================
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),    # unigram + bigram (nilai plus)
    max_features=3000
)

X = vectorizer.fit_transform(texts)
y = labels


# ===============================
# SPLIT DATA (TRAIN & TEST)
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# ===============================
# TRAIN MODEL (NAIVE BAYES)
# ===============================
model = MultinomialNB()
model.fit(X_train, y_train)


# ===============================
# EVALUATION
# ===============================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\n=== HASIL EVALUASI MODEL ===")
print(f"Accuracy: {accuracy:.2f}\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))


# ===============================
# SAVE MODEL & VECTORIZER
# ===============================
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel dan vectorizer berhasil disimpan.")
