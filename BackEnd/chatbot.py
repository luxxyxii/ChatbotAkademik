import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class Chatbot:
    def __init__(self):
        # ======================
        # LOAD INTENTS
        # ======================
        with open("intents.json", encoding="utf-8") as f:
            data = json.load(f)

        self.corpus = []
        self.labels = []
        self.responses = {}

        for intent in data["intents"]:
            tag = intent["tag"]
            self.responses[tag] = intent["responses"]
            for pattern in intent["patterns"]:
                self.corpus.append(pattern.lower().strip())
                self.labels.append(tag)

        # ======================
        # VECTOR & MODEL
        # ======================
        self.vectorizer = TfidfVectorizer(
            analyzer="char_wb",
            ngram_range=(2, 4)
        )

        X = self.vectorizer.fit_transform(self.corpus)

        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X, self.labels)

        print("✅ Chatbot model & dataset berhasil dimuat")

    def get_response(self, message: str) -> str:
        text = message.lower().strip()
        vector = self.vectorizer.transform([text])

        # ===== TAMBAHAN FALLBACK =====
        probabilities = self.model.predict_proba(vector)[0]
        max_prob = max(probabilities)

        if max_prob < 0.15:  # threshold bisa kamu atur 
            return "Maaf, saya tidak mengerti pertanyaan Anda."

        tag = self.model.predict(vector)[0]
        return random.choice(self.responses[tag])
