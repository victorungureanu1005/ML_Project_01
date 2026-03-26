import pandas as pd
from collections import Counter
class Data:
    def __init__(self, path, coloane_target):
        self.path = path
        self.coloane_target = coloane_target

    def load_data(self):
        try:
            data_frame = pd.read_csv(self.path)
            self.loaded = True
            self.data_frame = data_frame
            data_numpy = data_frame.to_numpy()
            self.X_numpy = data_numpy[:, :-len(self.coloane_target)]
            self.y_numpy = data_numpy[:, -len(self.coloane_target):]
            self.X_pandas = data_frame.drop(columns = self.coloane_target)
            self.y_pandas = data_frame[self.coloane_target]
            self.header = data_frame.columns.tolist()
        except:
            print("Data loaded unsuccessful")

    def show_class_distribution(self):
        if self.loaded:
            print("Class distribution")
            for i in self.header:
                print(f"\nAttribute {i} distribution:")
                # dictionar = dict(sorted(Counter(self.data_frame[i]))) #nu merge  -> most_common - utilizat in mod curent
                dictionar = Counter(self.data_frame[i])
                total = sum(dictionar.values())

                for valoare, numar in dictionar.most_common():
                    print(f"{valoare}: {numar} entries- {numar/total*100:.2f}%")

    def get_dim_types(self):
        if self.loaded:
            types = self.data_frame.dtypes
            ran, col = self.data_frame.shape
            return (types, ran, col)

    def dim_types(self):
        if self.loaded:
            (types, ran, col) = self.get_dim_types()
            print("Types:")
            print(types)
            print("Dimensions:")
            print(f"Rows: {ran}, Columns: {col}")

    def missing(self):
        lipsa = self.data_frame.isna().sum() #suma per coloana
        print("Missing values:")
        for coloana, suma in lipsa.items():
            print(f"{coloana}:{suma/len(self.data_frame)*100:.2f}%")

    def describe(self):
        if self.loaded:
            print("Dataset info")
            print(self.data_frame.describe())
