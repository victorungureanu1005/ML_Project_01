from Services.LoadData import Data
from Constants.Constants import DATA_PATH, TARGET_COLUMNS
data = Data(DATA_PATH, TARGET_COLUMNS)
data.load_data()

# print(data.X_pandas)
# print(data.y_pandas)
# print(data.X_pandas.columns)
# print(data.y_pandas.columns)