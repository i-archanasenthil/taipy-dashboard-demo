from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd

def change_category(state):
    state.data = data[data["Category"] == state.selected_category]
    state.chart_data = (
        state.data.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    state.layout = {
        "yaxis" : {"title" : "Revenue (USD)"},
        "title" : f"Sales by State for {state.selected_category}",
    }

data = pd.read_csv("data.csv")
selected_category = "Furniture"
categories = list(data["Category"].unique())


chart_data = (
    data.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

layout = {"yaxis" : {"title" : "Revenue (USD)"}, "title" : "Sales by State"}

with tgb.Page() as page:
    with tgb.part(class_name="container"):
        tgb.text("# Sales by **State**", mode = "md")
        