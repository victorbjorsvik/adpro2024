"""
Reads a two-column csv file from an online location
"""

import pandas as pd


class OnlineReader:
    """
    Class to read online data and analyse data as a pandas dataframe.
    
    This is just a suggestion.
    """

    def __init__(self):
        """
        We could have added the read segment during the init
        """
        self.cs_df = []

    def read(self, file_location):
        """
        Reads a file from an online location
        """
        self.cs_df = pd.read_csv(file_location)

    def plot(self):
        """
        Plots the data. Assume the first column is the temporal data.
        """
        self.cs_df.plot(x=self.cs_df.columns[0])

    def save(self, output_file):
        """
        Saves the read dataframe into a csv
        """
        self.cs_df.to_csv(output_file, index=False)
