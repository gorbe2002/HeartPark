import streamlit as st

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
    st.title("Our Parks")
    st.write("Here we provide a list of parks.")

# Outfits tab content
elif option == "Outfits":
    st.title("Outfit Selector")
    st.write("Here we provide a outfit selector.")
