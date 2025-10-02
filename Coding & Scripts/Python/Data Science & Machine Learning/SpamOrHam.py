# Importing necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample email data (you can replace this with your own dataset)
emails = [
    {'text': 'Get a free iPhone now!', 'label': 'spam'},
    {'text': 'Hey, how are you doing?', 'label': 'ham'},
    {'text': 'Claim your prize money!', 'label': 'spam'},
    {'text': 'Meeting tomorrow at 10 AM', 'label': 'ham'},
    {'text': 'Limited time offer - 50% off', 'label': 'spam'}
]

# Create DataFrame from the sample data
df = pd.DataFrame(emails)

# Feature extraction using Bag-of-Words (BoW) approach
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predicting on the testing set
y_pred = classifier.predict(X_test)

# Evaluating the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Example usage: Predicting labels for new emails
new_emails = ['Congratulations! You won a lottery.', 'Meeting agenda for next week']
new_emails_vectorized = vectorizer.transform(new_emails)
predicted_labels = classifier.predict(new_emails_vectorized)
print("\nPredicted Labels for New Emails:")
for email, label in zip(new_emails, predicted_labels):
    print(f"Email: {email} | Predicted Label: {label}")
