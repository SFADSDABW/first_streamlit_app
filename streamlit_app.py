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
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Apple','Strawberries'])
# Display it
streamlit.dataframe(my_fruit_list)
