from flask import Flask, render_template, request
import pandas as pd
import folium
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
import requests
from datetime import datetime, timedelta

# park data (https://www.latlong.net/convert-address-to-lat-long.html)
data = {
    'park_name': ["James J. Braddock North Hudson County Park", "Guttenberg/North Bergen Waterfront Park", "Donnelly Memorial Park"],
    'park_city': ["North Bergen", "North Bergen", "West New York"],
    'latitude': [40.808880, 40.791580, 40.788860],
    'longitude': [-74.001556, -73.998560, -73.999930],
    'zip_code': ["07047", "07047", "07093"]
}
df = pd.DataFrame(data)

# API keys
load_dotenv()
weather_api_key = os.getenv('OPENWEATHER_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parks', methods=['GET', 'POST'])
def parks():
    filtered_parks = None
    park_city = ""
    map_html = ""
    weather_data = None
    clothing_recommendation = []

    if request.method == 'POST':
        user_input = request.form['zip_code']
        if user_input in df['zip_code'].values:
            print(user_input)
            # Filter parks based on the entered zip code
            filtered_parks = df[df['zip_code'] == user_input]
            print("filtered_parks", filtered_parks)
            park_city = filtered_parks['park_city'].iloc[0]
            print("park_city is:", park_city)

            # Create a folium map centered at the average latitude and longitude of filtered parks
            map_center = [filtered_parks['latitude'].mean(), filtered_parks['longitude'].mean()]
            folium_map = folium.Map(location=map_center, zoom_start=12)

            print(folium_map)

            # Add markers for each park in the filtered results
            for index, row in filtered_parks.iterrows():
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=row['park_name'],
                    tooltip=row['park_name']
                ).add_to(folium_map)

            #renders the map html representation
            map_html = folium_map._repr_html_()

            print(map_html)

            # Get weather data from OpenWeatherAPI for the first park's location
            lat = filtered_parks['latitude'].iloc[0]
            lon = filtered_parks['longitude'].iloc[0]
            weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric'
            
            # Make the API call
            weather_response = requests.get(weather_url)
            if weather_response.status_code == 200:
                weather_json = weather_response.json()
                weather_data = {
                    'description': weather_json['weather'][0]['description'],
                    'temp': weather_json['main']['temp'],
                    'humidity': weather_json['main']['humidity']
                }

                # Determine clothing recommendation based on temperature (temp is in Celcius)
                temperature = weather_data['temp']
                if temperature < 20:
                    clothing_recommendation.extend(["T-Shirt", "Pants", "Walking Shoes", "Backpacks"])
                else:
                    clothing_recommendation.extend(["T-Shirt", "Shorts", "Walking Shoes", "Backpacks"])

            else:
                weather_data = {'error': 'Could not retrieve weather information'}

    return render_template('parks.html', map_html=map_html, filtered_parks=filtered_parks, park_city=park_city, weather_data=weather_data, clothing_recommendation=clothing_recommendation)

@app.route('/clothing')
def clothing():
    clothesDict = {
                    "Park Tee":["$25", "parkshirt.png"],
                    "\"All\" Love Tee":["$25", "allloveshirt.png"],
                    "Park Shorts":["$20", "parkshorts.png"],
                    "\"All Love\" Shorts":["$20", "allloveshorts.png"],
                    "Cargo Pants":["$30", "pants.png"],
                    "Hearty Hiker Boots":["$60", "boots.png"],
                    "Packed Up Park Backpack":["$35", "backpack.png"]
    }

    return render_template('clothing.html', clothesDict = clothesDict)

# @app.route('/parkai', methods=['GET', 'POST'])
# def parkai():
#     response_message = None

#     if request.method == 'POST':
#         pants_or_shorts = request.form['pants_or_shorts']
#         pants = True if pants_or_shorts == 'Pants' else False

#         PantsComp = "https://i.imgur.com/G6K2X9J.png"
#         ShortsComp = "https://i.imgur.com/cvhqvfY.png"

#         # Select appropriate image URL based on pants or shorts selection
#         url = PantsComp if pants else ShortsComp

#         # Make an OpenAI API call
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a friendly park ranger who knows fashion and always has an opinion on whether pants or shorts are the best option."},
#                 {"role": "user", "content": f"Is this outfit suitable for a park that can go up to 100 degrees Fahrenheit?"},
#                 {"role": "user", "content": f"Image: {url}"}
#             ],
#             temperature=0.5
#         )

#         # Get the response message
#         response_message = response['choices'][0]['message']['content']

#     return render_template('parkai.html', response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)
