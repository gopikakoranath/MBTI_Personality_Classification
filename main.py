import pandas as pd
from utils import download_dataset
from preprocessing import preprocess_data
from eda import perform_eda
from model import train_models

def main():
    # Kaggle dataset details
    kaggle_dataset = "darrelldolens/mbti-personality-types"
    dataset_name = "mbti.csv"
    
    # Download dataset
    dataset_path = download_dataset(kaggle_dataset, dataset_name)
    
    # Preprocessing
    df, X, y = preprocess_data(dataset_path)
    
    # Exploratory Data Analysis
    perform_eda(df)
    
    # Train and evaluate models
    trained_models, X_test, y_test, performances = train_models(X, y)
    
    # Compare performances
    print("\nModel Performance Comparison:")
    performance_df = pd.DataFrame({
        model: {"Accuracy": perf["accuracy"]}
        for model, perf in performances.items()
    })
    print(performance_df)
    
    # Display classification reports
    for model_name, performance in performances.items():
        print(f"\nClassification Report for {model_name}:")
        print(pd.DataFrame(performance["classification_report"]).transpose())

if __name__ == "__main__":
    main()