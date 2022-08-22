import pandas as pd
import numpy as np


class SolanaJobs:
    def __init__(self):
        pass

    def solana_dataframe(self) -> pd.DataFrame:
        """Import Dataset"""
        df = pd.read_csv(
            "./datasets/psycon/solana-usdt-to-20220-4-historical-data/sol-usdt.csv"
        )
        return df
