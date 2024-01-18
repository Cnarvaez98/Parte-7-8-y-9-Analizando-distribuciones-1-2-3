import matplotlib.pyplot as plt

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 6))
plt.hist(df['edad'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Graficar histogramas agrupados por hombre y mujer
categorias = ['anémicos', 'diabéticos', 'fumadores', 'muertos']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

for i, categoria in enumerate(categorias):
    # Filtrar datos por categoría y género
    hombres = df[(df['género'] == 'hombre') & (df[categoria] == 1)]['edad']
    mujeres = df[(df['género'] == 'mujer') & (df[categoria] == 1)]['edad']

    # Crear histogramas agrupados por hombre y mujer
    axes[i // 2, i % 2].hist([hombres, mujeres], bins=20, color=['skyblue', 'lightcoral'],
                             edgecolor='black', label=['Hombres', 'Mujeres'], align='edge')
    
    axes[i // 2, i % 2].set_title(f'Distribución de Edades - {categoria.capitalize()}')
    axes[i // 2, i % 2].set_xlabel('Edad')
    axes[i // 2, i % 2].set_ylabel('Frecuencia')
    axes[i // 2, i % 2].legend()
    axes[i // 2, i % 2].grid(True)

plt.tight_layout()
plt.show()
