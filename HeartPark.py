import streamlit as st
import pandas as pd

# park coordinates (https://www.latlong.net/convert-address-to-lat-long.html)
data = {
    'park_name': ["North Bergen 80th Street Park", "Guttenberg/North Bergen Waterfront Park", "Donnelly Memorial Park"],
    'park_city' : ["North Bergen", "North Bergen", "West New York"],
    'latitude': [40.801472, 40.791580, 40.788860],
    'longitude': [-74.006798, -73.998560, -73.999930],
    'zip_code': ["07047", "07047", "07093"]
}
df = pd.DataFrame(data)

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
    if user_input in df['zip_code'].values:
        # Filter the DataFrame for the entered zip code
        filtered_parks = df[df['zip_code'] == user_input]

        parkCity = filtered_parks['park_city'].iloc[0]

        st.title("Parks in " + parkCity + ":")

        for park in filtered_parks['park_name']:
            st.write(f"- {park}")  # Bulleted list

        # Display map centered on the selected park07047
        st.map(filtered_parks[['latitude', 'longitude']], zoom=12)


# Outfits tab content
elif option == "Outfits":
    st.title("Outfit Selector")
    st.write("Here we provide a outfit selector.")
