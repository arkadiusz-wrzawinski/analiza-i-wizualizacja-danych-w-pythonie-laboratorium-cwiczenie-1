import pandas as pd


class DataDescriber:
    @staticmethod
    def describe(data: pd.DataFrame, category_column: str | None):
        DataDescriber.print_size(data)
        DataDescriber.print_category_data(data, category_column)
        DataDescriber.print_attributes_data(data, category_column)

    @staticmethod
    def print_size(data: pd.DataFrame):
        print(f"Rows: {data.shape[0]}")
        print(f"Columns: {data.shape[1]}")

    @staticmethod
    def print_category_data(data: pd.DataFrame, category_column: str | None):
        if category_column is None:
            print(f"No category column")
            return

        if not category_column in data.columns:
            if int(category_column) in data.columns:
                category_column = int(category_column)
            else:
                print(f"Category column {category_column} not found")
                return

        print(f"Number of categories: {data[category_column].nunique()}")
        print(f"Categories: {data[category_column].unique().tolist()}")

        max_occurrences = data[category_column].value_counts()[data[category_column].mode()][0]
        print(f"Most pronounced categories: {data[category_column].mode().tolist()} with {max_occurrences} {"occurrence" if max_occurrences == 1 else "occurrences"}")

        value_counts = data[category_column].value_counts()
        min_occurrences = value_counts.min()
        print(f"Least pronounced categories: {value_counts[value_counts == min_occurrences].index.tolist()} with {min_occurrences} {"occurrence" if min_occurrences == 1 else "occurrences"}")

    @staticmethod
    def print_attributes_data(data: pd.DataFrame, category_column: str | None):
        if not category_column in data.columns:
            if int(category_column) in data.columns:
                category_column = int(category_column)
            else:
                print(f"Category column {category_column} not found")
                return

        data = data.drop(columns=[category_column]) if category_column is not None else data.copy(deep=True)

        print(f"Means of columns:")
        for column in data.columns:
            print(f"Column: {column}")
            print(f"Mean: {data[column].mean()}")
            print(f"Median: {data[column].median()}")