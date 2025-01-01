import os
import subprocess

def download_dataset(kaggle_dataset, dataset_name):
    """
    Downloads a Kaggle dataset and returns the path to the downloaded CSV file.
    Args:
        kaggle_dataset (str): Kaggle dataset identifier, e.g., "username/dataset-name".
        dataset_name (str): Name of the file in the dataset, e.g., "file.csv".
    Returns:
        str: Path to the downloaded CSV file.
    """
    dataset_dir = "datasets"
    os.makedirs(dataset_dir, exist_ok=True)
    
    # Download dataset
    subprocess.run(
        ["kaggle", "datasets", "download", "-d", kaggle_dataset, "-p", dataset_dir],
        check=True,
    )
    
    # Extract dataset
    zip_path = os.path.join(dataset_dir, f"{kaggle_dataset.split('/')[-1]}.zip")
    subprocess.run(["unzip", "-o", zip_path, "-d", dataset_dir], check=True)
    
    # Return path to the CSV file
    return os.path.join(dataset_dir, dataset_name)