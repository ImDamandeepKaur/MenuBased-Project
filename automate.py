import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    """Load dataset from a CSV file"""
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def handle_missing_values(data):
    """Handle missing values by either dropping or filling"""
    if data.isnull().sum().sum() > 0:
        print("Handling missing values...")
        data.fillna(data.mean(), inplace=True)  # Fill missing numerical values with mean
        data.fillna('Unknown', inplace=True)  # Fill missing categorical values with 'Unknown'
    return data

def encode_categorical_variables(data):
    """Encode categorical variables into numerical format"""
    print("Encoding categorical variables...")
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data, label_encoders

def scale_numerical_features(data):
    """Scale numerical features to standardize them"""
    print("Scaling numerical features...")
    scaler = StandardScaler()
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    return data, scaler

def visualize_data(data):
    """Generate some basic visualizations"""
    print("Visualizing data...")
    sns.pairplot(data)
    plt.show()

def main(file_path):
    # Load the dataset
    data = load_dataset(file_path)
    if data is None:
        return
    
    # Handle missing values
    data = handle_missing_values(data)
    
    # Encode categorical variables
    data, label_encoders = encode_categorical_variables(data)
    
    # Scale numerical features
    data, scaler = scale_numerical_features(data)
    
    # Visualize data
    visualize_data(data)
    
    # Print processed dataset head
    print("Processed Data Sample:")
    print(data.head())

if __name__ == "__main__":
    file_path = "MenuBasedProject/MenuWebsite/ML/LWstartup.csv"  # Replace with the path to your dataset
    main(file_path)
