import pandas as pd
import os

# Función para leer archivos y crear un conjunto de datos
def create_dataset(base_path):
    categories = ['positive', 'negative', 'neutral']
    data = []

    for category in categories:
        path = os.path.join(base_path, category)
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                file_path = os.path.join(path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read().strip()
                    data.append({'phrase': text, 'sentiment': category})

    return pd.DataFrame(data)

# Crear conjuntos de datos
train_dataset = create_dataset('train')  # Asegúrate de que 'training' es el nombre correcto de tu carpeta
test_dataset = create_dataset('test')       # Asegúrate de que 'test' es el nombre correcto de tu carpeta

# Guardar a archivos CSV
train_dataset.to_csv('train_dataset.csv', index=False)
test_dataset.to_csv('test_dataset.csv', index=False)
