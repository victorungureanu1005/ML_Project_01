import pandas as pd
class Data:
    def __init__(self, path, coloane_target):
        self.path = path
        self.coloane_target = coloane_target

    def load_data(self):
        try:
            data_frame = pd.read_csv(self.path)
            self.data_frame = data_frame
            data_numpy = data_frame.to_numpy()
            self.X_numpy = data_numpy[:, :-len(self.coloane_target)]
            self.y_numpy = data_numpy[:, -len(self.coloane_target):]
            self.X_pandas = data_frame.drop(columns = self.coloane_target)
            self.y_pandas = data_frame[self.coloane_target]
        except:
            print("Datele nu au fost incarcate cu succes")
