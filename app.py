import plotly.express as px
from shiny.express import input, render, ui
from shinywidgets import render_plotly
import seaborn as sns
import ipyleaflet as ipyl

# Cargar el conjunto de datos Titanic
titanic_df = sns.load_dataset('titanic')

# Menú desplegable para seleccionar una variable del Titanic
ui.input_select("var", "Select variable", choices=titanic_df.columns.tolist())

# Diseño de columnas para mostrar el histograma y la tabla
with ui.layout_columns(height="300px"):
    # Función para renderizar el histograma
    @render_plotly
    def hist():
        p = px.histogram(titanic_df, x=input.var())
        p.update_layout(height=200, xaxis_title=None)
        return p

    # Función para renderizar la tabla de datos del Titanic
    @render.data_frame
    def table():
        return titanic_df

# Menú desplegable para seleccionar variables adicionales
with ui.layout_columns():
    ui.input_select("var1", None, choices=titanic_df.columns.tolist(), width="100%")
    ui.input_select("var2", None, choices=titanic_df.columns.tolist(), width="100%")

with ui.layout_columns():
    @render_plotly
    def plot1():
        p = px.histogram(titanic_df, x=input.var1())
        p.update_layout(height=200, xaxis_title=None)
        return p

    @render_plotly
    def plot2():
        p = px.histogram(titanic_df, x=input.var2())
        p.update_layout(height=200, xaxis_title=None)
        return p
city_centers = {
    "Cherbourg": (49.6500, -1.6500),
    "Londres": (51.5074, -0.1278),
    "Southampton": (50.9000, -1.4000)
}

# Menú desplegable para seleccionar un centro de mapa
ui.input_select("center", "Center", choices=list(city_centers.keys()))

# Función para renderizar el mapa
@render_widget
def map():
    return ipyl.Map(zoom=4)

# Función reactiva para actualizar el centro del mapa según la selección del usuario
@reactive.effect
def update_map_center():
    map.widget.center = city_centers[input.center()]
