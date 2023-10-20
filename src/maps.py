import folium
import math


def crea_mapa(latitud, longitud, zoom=9):
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa 

def create_marker(latitud, longitud, etiqueta, color):
    marcador = folium.Marker([latitud, longitud], popup = etiqueta, icon=folium.Icon(color=color, icon='info-sign')) )