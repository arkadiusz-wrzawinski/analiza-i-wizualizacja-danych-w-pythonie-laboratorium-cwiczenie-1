import pandas as pd
import plotly.express as px

class DataDrawer:
    @staticmethod
    def draw(data: pd.DataFrame, category_column: str | None, image_path: str):
        if not category_column in data.columns:
            if int(category_column) in data.columns:
                category_column = int(category_column)
            else:
                print(f"Category column {category_column} not found")
                return

        data = data.drop(columns=[category_column]) if category_column is not None else data.copy(deep=True)
        means: pd.Series = data.mean()
        means: pd.DataFrame = means.to_frame().rename_axis("column").sort_values(0).reset_index()
        means["column"] = means["column"].astype(str)

        fig = px.bar(means, x="column", y=0, labels={"0": "mean"})
        fig.update_layout(xaxis = {"tickvals": means["column"]})
        fig.write_image(image_path, width=1920, height=1080)

        print(f"Saved image to {image_path}")