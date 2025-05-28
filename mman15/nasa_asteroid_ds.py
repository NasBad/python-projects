"""
    Student Name: Naseem Badran
    Student ID: 322726662

    This is a python code for MMN15
"""
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    """
    Loads a CSV file into a Pandas DataFrame.

    Parameters:
        filename (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame if successful.
        None: If the file is not found or cannot be parsed.
    """
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.ParserError:
        print("Error: Unable to parse file.")
    return None

def mask_data(df):
    """
    Filters asteroids with Close Approach Date from the year 2000 onward.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A filtered DataFrame containing only records from 2000 onward.
    """
    df["Close Approach Date"] = pd.to_datetime(df["Close Approach Date"], errors='coerce')
    return df[df["Close Approach Date"].dt.year >= 2000]

def data_details(df):
    """
    Cleans data by removing unnecessary columns and returning summary details.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        tuple: (number of rows, list of column names, number of columns).
    """
    df = df.drop(columns=["Neo Reference ID", "Orbiting Body", "Equinox"], errors='ignore')
    return len(df), list(df.columns), df.shape[1]

def max_absolute_magnitude(df):
    """
    Finds the asteroid with the highest Absolute Magnitude.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        tuple: (asteroid name, absolute magnitude, miss distance in kilometers).
    """
    max_mag = df.loc[df["Absolute Magnitude"].idxmax()]
    return (max_mag["Name"], max_mag["Absolute Magnitude"], max_mag["Miss Dist.(kilometers)"])

def closest_to_earth(df):
    """
    Finds the closest asteroid to Earth by Miss Distance.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        str: The name of the closest asteroid.
    """
    return df.loc[df["Miss Dist.(kilometers)"].idxmin(), "Name"]

def common_orbit(df):
    """
    Counts the number of asteroids for each unique Orbit ID.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        dict: A dictionary where keys are Orbit IDs and values are the count of asteroids in each orbit.
    """
    return df["Orbit ID"].value_counts().to_dict()

def min_max_diameter(df):
    """
    Counts asteroids whose max estimated diameter is greater than the average max diameter.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        int: The count of asteroids with a diameter greater than the average.
    """
    avg_max_diameter = df["Est Dia in KM(max)"].mean()
    return len(df[df["Est Dia in KM(max)"] > avg_max_diameter])

def plt_hist_diameter(df):
    """
    Plots a histogram of asteroid diameters.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
    """
    df["Est Dia in KM(max)"].hist(bins=100)
    plt.xlabel("Average Diameter (KM)")
    plt.ylabel("Count")
    plt.title("Distribution of Asteroid Diameters")
    plt.show()

def plt_hist_common_orbit(df):
    """
    Plots a histogram of asteroids based on their Minimum Orbit Intersection values.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
    """
    if 'Minimum Orbit Intersection' in df.columns:
        plt.hist(df['Minimum Orbit Intersection'], bins=10, edgecolor='black')
        plt.title('Distribution of Asteroids by Minimum Orbit Intersection')
        plt.xlabel('Minimum Orbit Intersection')
        plt.ylabel('Number of Asteroids')
        plt.show()
    else:
        print("Column 'Minimum Orbit Intersection' not found.")

def plt_pie_hazard(df):
    """
    Plots a pie chart showing the percentage of hazardous and non-hazardous asteroids.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
    """
    if 'Hazardous' in df.columns:
        hazardous_counts = df['Hazardous'].value_counts()
        labels = ['False', 'True']
        plt.pie(hazardous_counts, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Percentage of Hazardous and Non-Hazardous Asteroids')
        plt.show()
    else:
        print("Column 'Hazardous' not found.")

def plt_linear_motion_magnitude(df):
    """
    Plots a scatter plot of Miss Distance vs Speed.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
    """
    plt.scatter(df["Miss Dist.(kilometers)"], df["Miles per hour"], alpha=0.5)
    plt.xlabel("Miss Distance (kilometers)")
    plt.ylabel("Miles per hour")
    plt.title("Scatter Plot: Miss Distance vs Speed")
    plt.show()

# Example usage
if __name__ == "__main__":
    df = load_data("nasa.csv")
    if df is not None:
        df = mask_data(df)
        print("Data Details (סעיף ג):", data_details(df))
        print("Max Absolute Magnitude (סעיף ד):", max_absolute_magnitude(df))
        print("Closest Asteroid (סעיף ה):", closest_to_earth(df))
        print("Common Orbits (סעיף ו):", common_orbit(df))
        print("Number of Asteroids (סעיף ז):", min_max_diameter(df))
        plt_hist_diameter(df)
        plt_hist_common_orbit(df)
        plt_pie_hazard(df)
        plt_linear_motion_magnitude(df)
