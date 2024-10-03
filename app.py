from flask import Flask, render_template, request
import folium
import pandas as pd

app = Flask(__name__)

# Park data
data = {
    'park_name': ["James J. Braddock North Hudson County Park", "Guttenberg/North Bergen Waterfront Park", "Donnelly Memorial Park"],
    'park_city': ["North Bergen", "North Bergen", "West New York"],
    'latitude': [40.808880, 40.791580, 40.788860],
    'longitude': [-74.001556, -73.998560, -73.999930],
    'zip_code': ["07047", "07047", "07093"]
}
df = pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parks', methods=['GET', 'POST'])
def parks():
    filtered_parks = None
    park_city = ""
    if request.method == 'POST':
        user_input = request.form['zip_code']
        if user_input in df['zip_code'].values:
            # Filter parks based on the entered zip code
            filtered_parks = df[df['zip_code'] == user_input]
            park_city = filtered_parks['park_city'].iloc[0]

            # Create a folium map centered at the average latitude and longitude of filtered parks
            map_center = [filtered_parks['latitude'].mean(), filtered_parks['longitude'].mean()]
            folium_map = folium.Map(location=map_center, zoom_start=14)

            # Add markers for each park in the filtered results
            for index, row in filtered_parks.iterrows():
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=row['park_name'],
                    tooltip=row['park_name']
                ).add_to(folium_map)

            # Save the map to an HTML file
            folium_map.save('templates/map.html')

    return render_template('parks.html', filtered_parks=filtered_parks, park_city=park_city)

@app.route('/outfits')
def outfits():
    return render_template('outfits.html')

if __name__ == '__main__':
    app.run(debug=True)
