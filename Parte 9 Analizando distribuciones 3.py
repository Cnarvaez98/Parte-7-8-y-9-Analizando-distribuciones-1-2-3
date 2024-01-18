import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

# Eliminar columnas no deseadas
df_reduced = df.drop(columns=['muertos', 'categoria_edad'])

# Convertir el DataFrame a un array de Numpy
X = df_reduced.values

# Extraer el vector y (columna objetivo)
y = df['muertos'].values

# Aplicar t-SNE para reducción de dimensionalidad a 3 dimensiones
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crear DataFrame con las nuevas dimensiones y el vector y
df_embedded = pd.DataFrame({'Dim_1': X_embedded[:, 0], 'Dim_2': X_embedded[:, 1], 'Dim_3': X_embedded[:, 2], 'Muerto': y})

# Crear gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(df_embedded, x='Dim_1', y='Dim_2', z='Dim_3', color='Muerto',
                    title='Visualización 3D de Datos con t-SNE',
                    labels={'Muerto': 'Estado'})

# Mostrar el gráfico
fig.show()
