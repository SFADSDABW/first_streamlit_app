import streamlit
import pandas

streamlit.title('My First streamlit file in Python')

streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
streamlit.text('Coffee')
streamlit.text('More Coffee')
streamlit.text('Crumpets')
streamlit.text('Even More Coffee')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
