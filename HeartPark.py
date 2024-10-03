import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import folium
import pandas as pd
import datetime

# park coordinates (https://www.latlong.net/convert-address-to-lat-long.html)
data = {
    'park_name': ["James J. Braddock North Hudson County Park", "Guttenberg/North Bergen Waterfront Park", "Donnelly Memorial Park"],
    'park_city' : ["North Bergen", "North Bergen", "West New York"],
    'latitude': [40.808880, 40.791580, 40.788860],
    'longitude': [-74.001556, -73.998560, -73.999930],
    'zip_code': ["07047", "07047", "07093"]
}
df = pd.DataFrame(data)

# Create a sidebar for navigation
st.sidebar.title("Navigation Bar")

# Add different options in the sidebar as a dropdown (selectbox)
option = st.sidebar.selectbox("Choose a page", ["About Us", "Parks", "Outfits"])

# About tab content
if option == "About Us":
    st.title("Our Mission")
    st.write("We are strong advocates for outdoor recreation in urban areas as well as promoting city conservation efforts within neighborhoods.")
    st.title("Our Vision")
    st.write("We want to lead the streetwear-fashion movement in outdoor gear and make parks a more welcoming environment to urban areas.")

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

        map_center = [filtered_parks['latitude'].mean(), filtered_parks['longitude'].mean()]
        folium_map = folium.Map(location=map_center, zoom_start=14)

        # Add markers for each park in the filtered results
        for index, row in filtered_parks.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=row['park_name'],
                tooltip=row['park_name']
            ).add_to(folium_map)

        # Render the Folium map in Streamlit
        folium_static(folium_map)

        # Calendar feature
        st.title("Select a Date Range")

        # Default start and end dates
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=1)

        # Create a date range input
        date_range = st.date_input(
            "Select the date range",
            value=(start_date, end_date)
        )

        # Display the selected date range
        st.write(f"You selected the date range from {date_range[0]} to {date_range[1]}")

# Outfits tab content
elif option == "Outfits":
    st.title("Outfit Selector")
    st.write("Here we provide a outfit selector.")