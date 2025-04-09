# server.py
import os
from flask import Flask, request, send_file
import folium

app = Flask(__name__)

@app.route("/generate_map", methods=["POST"])
def generate_map():
    data = request.json
    ip = data.get("ip")
    lat = float(data.get("latitude"))
    lon = float(data.get("longitude"))

    map_ = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=f"IP: {ip}").add_to(map_)
    map_.save("map.html")

    return send_file("map.html")

if __name__ == "__main__":
    # This is the magic for Render:
    # 1. Use PORT from the environment
    # 2. Listen on 0.0.0.0
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
