import streamlit as st
import pandas as pd

# North Bergen coordinates (https://www.latlong.net/convert-address-to-lat-long.html)
data = {
    'latitude': [40.808880],
    'longitude': [-74.001556],
}
df = pd.DataFrame(data)

# can use given dataset here:
zip_to_city = {
    "07047": "North Bergen"
}

# Create a sidebar for navigation
st.sidebar.title("Navigation Bar")

# Add different options in the sidebar as a dropdown (selectbox)
option = st.sidebar.selectbox("Choose a page", ["About", "Parks", "Outfits"])

# About tab content
if option == "About":
    st.title("About Us")
    st.write("This is the about page with company information.")

# Parks tab content
elif option == "Parks":
    # Create a textbox
    st.title("Welcome to our \"Park Selector\" feature!")
    user_input = st.text_input("Enter your zip code here:")

    # Get the park name based on the zip code
    if user_input in zip_to_city:
        st.title("Parks in " + zip_to_city[user_input])
        # st.title("Simple Map with st.map")
        st.map(df)

# Outfits tab content
elif option == "Outfits":
    st.title("Outfit Selector")
    st.write("Here we provide a outfit selector.")
