# MBTI Personality Classifier

This project classifies individuals into MBTI personality types using a dataset from Kaggle. It preprocesses textual data, performs exploratory data analysis, and trains multiple machine learning models for classification.

## Features
- **Automatic Dataset Download**: The Kaggle API is used to download the MBTI dataset directly.
- **Text Preprocessing**: Uses TF-IDF vectorization for feature extraction.
- **Multiple Models**: Trains and evaluates three models:
  - Random Forest
  - Logistic Regression
  - Support Vector Machine
- **Performance Comparison**: Outputs accuracy and detailed classification reports for all models.

## Requirements
- Python 3.7 or higher
- Kaggle API set up with `kaggle.json` file

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/mbti-classifier.git
   cd mbti-classifier
2. Install Dependencies
    ```bash
    pip install -r requirements.txt
3. Set up the Kaggle API:
    - Download your kaggle.json file from your Kaggle account.
    - Place the file in the ~/.kaggle/ directory or the project root.
4. Run the main script:
    ```bash
    python main.py
5.	The script will:
	•	Download the dataset.
	•	Preprocess the data.
	•	Perform Exploratory Data Analysis (EDA).
	•	Train three models and compare their performances.

