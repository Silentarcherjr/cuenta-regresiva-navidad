from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def countdown_to_christmas():
    # Obtener la fecha actual
    today = datetime.now()
    # Fecha de Navidad para el año actual
    christmas = datetime(today.year, 12, 25)
    
    # Si la fecha actual es posterior a Navidad, calcular para el próximo año
    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)
    
    # Calcular los días restantes
    days_remaining = (christmas - today).days
    
    # Debugging: Imprimir los días restantes en los logs
    print(f"Días restantes para Navidad: {days_remaining}")
    
    # Renderizar la plantilla con la variable 'days_remaining'
    return render_template('index.html', days_remaining=days_remaining)

# Esto asegura que el servidor solo se ejecute cuando se llame directamente al archivo
if __name__ == '__main__':
    # Configuración para el entorno local
    app.run(debug=True, host='0.0.0.0', port=5000)
