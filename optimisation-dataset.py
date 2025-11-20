import pandas as pd
from dspy.datasets.dataset import Dataset


class ExcelDataset(Dataset):
    def __init__(self, file_path, *args,**kwargs) -> None:
        super().__init__(*args, **kwargs)

        df = pd.read_excel(file_path)
        self._train = df.iloc[0:20].to_dict(orient='records')

        self._dev = df.iloc[20:].to_dict(orient='records')

dataset = ExcelDataset("dialogue-data-small.xlsx")
print(dataset.train[:1])
print(dataset.devset[:1])