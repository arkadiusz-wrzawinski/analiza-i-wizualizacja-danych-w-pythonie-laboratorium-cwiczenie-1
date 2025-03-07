import os

import pandas as pd


class DataSaver:
    @staticmethod
    def save(data: pd.DataFrame, path: str, separator: str, header: int | None):
        ext = os.path.splitext(path)[1]
        try:
            match ext:
                case ".xlsx":
                    data.to_excel(path, header=header is not None)
                case ".csv":
                    data.to_csv(path, index=False, sep=separator, header=header is not None, float_format="%.7e")
                case ".txt":
                    data.to_csv(path, index=False, sep=separator, header=header is not None, float_format="%.7e")
                case _:
                    return None
            print(f"Saved results to {path}")
        except Exception as e:
            print(e)
            return None
