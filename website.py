import streamlit as st
import pandas as pd

data = {
    'latitude': [40.808880],
    'longitude': [-74.001556],
}
df = pd.DataFrame(data)

# Create a sidebar for navigation
st.sidebar.title("Navigation")

# Add different options in the sidebar as a dropdown (selectbox)
option = st.sidebar.selectbox("Choose a page", ["About", "Parks", "Outfits"])

# About tab content
if option == "About":
    st.title("About Us")
    st.write("This is the about page with company information.")

# Parks tab content
elif option == "Parks":
    # Create a textbox
    user_input = st.text_input("Enter your text here:")

    # Display the user input
    if user_input:
        st.write("You entered:", user_input)

    st.title("Our Parks")
    st.write("Here we provide a list of parks.")
    st.title("Simple Map with st.map")
    st.map(df)

# Outfits tab content
elif option == "Outfits":
    st.title("Outfit Selector")
    st.write("Here we provide a outfit selector.")
