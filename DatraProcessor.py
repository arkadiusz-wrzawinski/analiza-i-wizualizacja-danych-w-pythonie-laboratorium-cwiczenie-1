import pandas as pd


class DataProcessor:
    @staticmethod
    def process(data: pd.DataFrame, category_column: str | None) -> pd.DataFrame | None:
        if not category_column in data.columns:
            if int(category_column) in data.columns:
                category_column = int(category_column)
            else:
                print(f"Category column {category_column} not found")
                return

        frame = data.drop(columns=[category_column]) if category_column is not None else data.copy(deep=True)

        number_of_columns = int(frame.shape[1] * 0.20)

        means: pd.Series = data.mean()
        means = means.nlargest(number_of_columns)
        column_names = means.index

        frame = frame[column_names]

        if category_column is not None:
            frame[category_column] = data[category_column]

        return frame