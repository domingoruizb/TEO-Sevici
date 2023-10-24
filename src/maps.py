import folium
import math
import webbrowser
import os

def crea_mapa(latitud, longitud, zoom=9):
    mapa = folium.Map(location=[latitud, longitud], zoom_start=zoom)
    return mapa 

def create_marker(latitud, longitud, etiqueta, color):
    marcador = folium.Marker([latitud, longitud], popup = etiqueta, icon=folium.Icon(color=color, icon='info-sign'))
    return marcador

def save_map(map, ruta_fichero):
    map.save(ruta_fichero)
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))