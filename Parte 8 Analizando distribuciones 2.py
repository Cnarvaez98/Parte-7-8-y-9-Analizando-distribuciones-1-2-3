import matplotlib.pyplot as plt

# Filtrar datos para obtener cantidades
cantidad_anemicos = df['anémicos'].sum()
cantidad_diabeticos = df['diabéticos'].sum()
cantidad_fumadores = df['fumadores'].sum()
cantidad_muertos = df['muertos'].sum()

# Crear subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Configurar los datos para cada gráfica de torta
datos_torta = [cantidad_anemicos, cantidad_diabeticos, cantidad_fumadores, cantidad_muertos]
etiquetas = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']
colores = ['lightblue', 'lightcoral', 'lightgreen', 'gray']

# Crear gráficas de torta
for i, ax in enumerate(axes.flatten()):
    ax.pie(datos_torta, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=90)
    ax.set_title(f'Distribución de {etiquetas[i]}')

plt.tight_layout()
plt.show()
