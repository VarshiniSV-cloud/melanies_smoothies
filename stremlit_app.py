# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write("Customize your smoothie here:")


name_on_order=st.text_input("Name on Smoothie")
st.write("The name on Smoothie will be:", name_on_order)

from snowflake.snowpark import Session

session = Session.builder.configs({
  "account" = "JAZZBKK-FIB07714"
  "user" = "VARSHINIS"
  "password" = "Varshinigopal12"
  "role" = "SYSADMIN"
  "warehouse" = "COMPUTE_WH"
  "database" = "SMOOTHIES"
  "schema" = "PUBLIC"
}).create()

cnx = st.connection("Snowflake")
session = cnx.session()
