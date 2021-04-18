import pandas as pd
import matplotlib.pyplot as plt
import twstock as ts



tar = ts.Stock('1472')
tar_df = pd.DataFrame(tar.raw_data)
print(tar_df)