import streamlit

streamlit.title('My Name is Mayur...')
streamlit.header('Abcd')
streamlit.text('abchd')
streamlit.text('🥣 🥗 🐔 🥑🍞')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits: ",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
