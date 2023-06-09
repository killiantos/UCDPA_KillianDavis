
#package importing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.expand_frame_repr', False)
#Had to add r at the start of the file path as it was reading it as a unicode
AirQ = pd.read_csv(r"C:\Users\Killian\PycharmProjects\UCDPA_KillianDavis\datasets\AQI and Lat Long of Countries.csv")
Climate = pd.read_csv(r"C:\Users\Killian\PycharmProjects\UCDPA_KillianDavis\datasets\climate_change_data.csv")
# print(AirQ.head())
# print(AirQ.shape)
# print(AirQ.describe().T)
# print(AirQ.columns)
#print(AirQ.dtypes)
# AirQ.drop_duplicates()
# print(AirQ.shape)
print(AirQ.isnull().sum())
# print(Climate.isnull().sum())

# sns.lineplot(data=AirQ, x='City', y='AQI Value')
# plt.grid()
# plt.show()