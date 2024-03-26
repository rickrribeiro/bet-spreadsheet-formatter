import pandas as pd
import utils.column_helper as ch
class SpreadsheetService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        table = pd.read_excel(self.file_path)
        table.columns = [ch.num_to_col_name(i) for i in range(1, len(table.columns) + 1)]
        return table
 
    def write(self, data, newFilePath):
        df_list = []

        for key, values in data.items():
            for value in values:
                df_list.append([key, value["units"], value["green"], value["reds"], value["tips"]])
            # Adicionar uma linha em branco
            df_list.append(["", "", "", "", ""])
        df = pd.DataFrame(df_list, columns=["key", "units", "green", "reds", "tips"])

        df.to_excel(newFilePath, index=False)
