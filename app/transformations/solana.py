import pandas as pd
import numpy as np


class SolanaJobs:
    def __init__(self):
        pass

    def solana_dataframe(self) -> None:
        """Import Dataset"""
        self.df = pd.read_csv(
            "./datasets/psycon/solana-usdt-to-20220-4-historical-data/sol-usdt.csv"
        )
        return self.df

    def dataframe_to_numpy_array(self) -> None:
        """Convert dataframe to numpy array"""
        self.df_np = self.df.to_numpy()
        return self.df_np
