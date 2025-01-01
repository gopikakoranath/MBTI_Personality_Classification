import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)
    
    # Extract text and labels
    X_raw = df['posts']
    y_raw = df['type']
    
    # Encode labels
    le = LabelEncoder()
    y = le.fit_transform(y_raw)
    
    # Text vectorization using TF-IDF
    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    X = tfidf.fit_transform(X_raw).toarray()
    
    return df, X, y