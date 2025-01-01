import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    # Distribution of personality types
    sns.countplot(data=df, x='type', order=df['type'].value_counts().index)
    plt.title("Distribution of MBTI Personality Types")
    plt.xticks(rotation=45)
    plt.show()
    
    # Example posts from each type
    for ptype in df['type'].unique():
        print(f"\nSample post from {ptype}:\n")
        print(df[df['type'] == ptype]['posts'].iloc[0])