# progetto/Social/ml_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import io
import base64

def train_and_predict(csv_file):

    
    # Carica i dati dal CSV
    data = pd.read_csv(csv_file)
    
    # Supponiamo che il CSV abbia colonne 'feature' e 'target'
    X = data[['feature']]  # Sostituisci con le tue colonne di input
    y = data['target']     # Sostituisci con la tua colonna di output

    # Dividi i dati in set di addestramento e test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Addestra il modello
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Fai previsioni
    predictions = model.predict(X_test)

    # Crea un grafico
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='Dati Reali')
    plt.plot(X_test, predictions, color='red', linewidth=2, label='Previsioni')
    plt.title('Previsioni vs Dati Reali')
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.legend()

    # Salva il grafico in un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return predictions, image_base64