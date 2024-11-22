import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Get the path to the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '..', 'data', 'all_users.csv')

    # Load data
    data = pd.read_csv(csv_path)

    # Visualize the data: City Distribution
    city_counts = data['City'].value_counts()

    # Bar chart for city distribution
    city_counts.plot(kind='bar', figsize=(8, 5), color='skyblue', edgecolor='black')
    plt.title('User Distribution by City', fontsize=14)
    plt.xlabel('City', fontsize=12)
    plt.ylabel('Number of Users', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
