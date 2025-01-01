from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

def train_models(X, y):
    """
    Trains multiple models and returns them with their test data and performance metrics.
    """
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize models
    models = {
        "Random Forest": RandomForestClassifier(random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=500, random_state=42),
        "Support Vector Machine": SVC(kernel="linear", random_state=42),
    }
    
    trained_models = {}
    performances = {}
    
    for model_name, model in models.items():
        # Train model
        model.fit(X_train, y_train)
        trained_models[model_name] = model
        
        # Predict and evaluate
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Store performance metrics
        performances[model_name] = {
            "accuracy": acc,
            "classification_report": report,
        }
    
    return trained_models, X_test, y_test, performances