import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My First streamlit file in Python')

streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
streamlit.text('Coffee')
streamlit.text('More Coffee')
streamlit.text('Crumpets')
streamlit.text('Even More Coffee')

# start importing data into Python and displaying it
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add in a multi-select widget
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Apple','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display it
streamlit.dataframe(fruits_to_show)

# Create the repeatable code block (function)
def get_fruity_advice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# New Section to display fruityvace api response
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What Fruit would you like information about?')
  if not fruit_choice:
    streamlit.write('Please select a fruit to get information')
  else:
    back_from_function = get_fruity_advice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
    streamlit.error()
    
streamlit.header('The fruit list contains')    
# Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM PC_RIVERY_DB.public.fruit_load_list") 
    return my_cur.fetchall()
   
# Add button to load fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

# Get user to add a new fruit into the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into PC_RIVERY_DB.public.fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding: " + new_fruit
    
add_my_fruit = streamlit.text_input('What Fruit would you like to add?')
if streamlit.button('Add Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)  
  
# don't run anything past here whilst we troubleshoot
#streamlit.stop()

