# Import the required libraries
import os
import pandas as pd

def from_dta_to_csv(folder_path):
    """
    It transforms a set of DTA files to csv automotically

    Args:
        folder_path (str, optional): Introduce the folder path where the DTA are stored".
    """
    # Get the filenames
    file_list = os.listdir(folder_path) 

    # Transfrom the dta files into csv
    for file in file_list:
        data = pd.io.stata.read_stata(file)
        # Split if there's a point
        name = file.split('.')[0]
        data.to_csv(name + ".csv")



