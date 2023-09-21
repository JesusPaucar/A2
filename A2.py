import plotly.express as px
import numpy as np

def draw_flower(petal_count):
    # Ángulos para los pétalos
    petal_angles = np.linspace(0, 360, petal_count, endpoint=False)

    # Coordenadas de los pétalos
    x = 0.2 * np.sin(np.deg2rad(petal_angles))
    y = 0.2 * np.cos(np.deg2rad(petal_angles))

    # Crear un DataFrame para los pétalos
    petal_colors = np.random.choice(['#FFD700', '#FFAC33', '#FFD700'], size=petal_count)
    petal_df = {'x': x, 'y': y, 'color': petal_colors}
    
    return petal_df

# Número de pétalos
petal_count = 6

# Crear el DataFrame de los pétalos
petal_df = draw_flower(petal_count)

# Crear la figura de Plotly
fig = px.scatter(petal_df, x='x', y='y', color='color', width=400, height=400)

# Configurar la apariencia de la flor
fig.update_traces(marker=dict(size=12))

# Ocultar ejes y etiquetas
fig.update_xaxes(showticklabels=False, zeroline=False)
fig.update_yaxes(showticklabels=False, zeroline=False)

# Mostrar la figura
fig.show()
