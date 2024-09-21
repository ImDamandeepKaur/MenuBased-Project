from flask import Flask, request, jsonify
from flask_cors import CORS

from geopy.geocoders import Nominatim
app(CORS)

app = Flask(__name__)

# Function to get coordinates
def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location_name)
    if location:
        return {"latitude": location.latitude, "longitude": location.longitude}
    else:
        return {"error": "Location not found"}

@app.route("/coordinates/<location>", methods=['GET'])
def coordinates(location):
    location_name = location
    if not location_name:
        return jsonify({"error": "Location parameter is required"}), 400
    
    coordinates = get_coordinates(location_name)
    return jsonify(coordinates)

if __name__ == '__main__':
    app.run(debug=True)
