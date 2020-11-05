import openpyxl
import pandas
import plotly
from us_state_abbrev import us_state_abbrev

def get_data_rows(file_name):
    excel_file = openpyxl.load_workbook(file_name)
    what_ever_we_want= excel_file.active
    return what_ever_we_want.rows

def process_data(all_data):
    state_names_list= []
    unemployment_list= []
    for state_row in all_data:

        name = state_row[0].value
        if name in us_state_abbrev:
            state_abbrev= us_state_abbrev[name]
            state_names_list.append(state_abbrev)
            rate= state_row[1].value
            unemployment_list.append(rate)
    return state_names_list, unemployment_list


def display_data(state_list, unemployment_list):
    our_beautiful_map= plotly.graph_objs.Figure(data=plotly.graph_objs.Choropleth(
        locations= state_list,
        z = unemployment_list,
        locationmode = "USA-states" ,
        colorscale = "Thermal",
        colorbar_title= "Unemployment Rate Data")
    )
    our_beautiful_map.update_layout(
        title_text= "Us Unemployment Sep 2020",
        geo_scope= "usa")

    our_beautiful_map.show()
def main():
    all_data = get_data_rows("lanrderr-unemployment.xlsx")
    state_list, unemployment_list = process_data(all_data)
    display_data(state_list , unemployment_list)


main()