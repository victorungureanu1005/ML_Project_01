from Services.Data import Data
from Constants.Constants import DATA_PATH, TARGET_COLUMNS
data = Data(DATA_PATH, TARGET_COLUMNS)
data.load_data()

# print(data.X_pandas)
# print(data.y_pandas)
# print(data.X_pandas.columns)
# print(data.y_pandas.columns)
# print(data.header)

# data.show_class_distribution()

# data.dim_types()

#data.missing()

data.describe()