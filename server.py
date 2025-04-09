# server.py
from flask import Flask, request, send_file
import folium

app = Flask(__name__)

@app.route("/generate_map", methods=["POST"])
def generate_map():
    data = request.json
    ip = data.get("ip")
    lat = float(data.get("latitude"))
    lon = float(data.get("longitude"))

    map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=f"IP: {ip}").add_to(map)
    map.save("map.html")

    return send_file("map.html")

if __name__ == "__main__":
    app.run(port=5001)
