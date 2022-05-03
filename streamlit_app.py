import streamlit
import pandas

streamlit.title('My First streamlit file in Python')

streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
streamlit.text('Coffee')
streamlit.text('More Coffee')
streamlit.text('Crumpets')
streamlit.text('Even More Coffee')

# start importing data into Python and displaying it
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add in a multi-select widget
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Apple','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display it
streamlit.dataframe(fruits_to_show)


# New Section to display fruityvace api response
streamlit.header('Fruityvice Fruit Advice')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)
