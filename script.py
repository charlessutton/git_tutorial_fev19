import numpy as np
import pandas as pd

# lecture du dataset
df = pd.read_csv("dataset_vma.csv")

# remplace des valeurs "na" par des rééls NA
df.replace("na",np.nan)

df["diameter"] = np.sqrt(df["d1"].astype(int)**2 + df["d2"].astype(int)**2)
