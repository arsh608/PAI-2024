import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

emails = pd.DataFrame({
    'text': ['Free money now', 'Meeting at 3 PM', 'Congratulations, you won a prize', 'Can we schedule a call?'],
    'label': ['spam', 'ham', 'spam', 'ham']
})

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words and word.isalpha()]
    
    return ' '.join(filtered_tokens)

emails['text'] = emails['text'].apply(preprocess_text)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails['text']) 

y = emails['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Classification Report:\n", classification_report(y_test, y_pred))

# Example prediction with a new email
new_email = ["Get your free prize now"]
new_email_processed = [preprocess_text(email) for email in new_email]
new_email_vectorized = vectorizer.transform(new_email_processed)

# Predict if the new email is spam or ham
prediction = model.predict(new_email_vectorized)
print(f"The new email is classified as: {prediction[0]}")
