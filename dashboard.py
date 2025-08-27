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
    tgb.selector(value = "{selected_category}", lov = "{categories}", on_change = change_category)
    tgb.chart(
        data = "{chart_data}",
        x = "State",
        y = "Sales",
        type = "bar",
        layout = "{layout}",
    )
    tgb.table(data = "{data}")

if __name__ == "__main__":
    Gui(page=page).run(title= "Sales", dark_mode = False, debug = True)




