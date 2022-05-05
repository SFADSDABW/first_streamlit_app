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
fruit_choice = streamlit.text_input('What Fruit would you like information about?','Kiwi')
streamlit.write('The User entered',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM PC_RIVERY_DB.public.fruit_load_list") 
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")         
streamlit.dataframe(my_data_rows)

# Get user to add a new fruit into the list
add_my_fruit = streamlit.text_input('What Fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding',add_my_fruit)

#This will not work for now, but just go with it
my_cur.execute("insert into PC_RIVERY_DB.public.fruit_load_list values ('from streamlit')")

# my_cur.execute("SELECT CURRENT_USER(),CURRENT_ACCOUNT(),CURRENT_REGION()")
# streamlit.text("Hello from Snowflake:")

