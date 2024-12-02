from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def countdown_to_christmas():
    # Obtener la fecha actual
    today = datetime.now()
    christmas = datetime(today.year, 12, 25)

    # Si ya pasó Navidad este año, calcular para el próximo año
    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)

    # Calcular los días restantes de forma precisa
    time_difference = christmas - today
    days_remaining = time_difference.days + (1 if time_difference.seconds > 0 else 0)

    # Mensajes personalizados
    if days_remaining > 10:
        message = "¡Aún hay tiempo para prepararte!"
    elif days_remaining > 0:
        message = "¡La Navidad está muy cerca!"
    else:
        message = "¡Feliz Navidad! 🎅🎄"

    # Generar idea de regalo aleatoria
    gift_ideas = ["Un libro", "Un rompecabezas", "Un juego de mesa", "Una planta", "Unos auriculares"]
    random_gift = random.choice(gift_ideas)

    # Recoger el nombre del usuario si se envió
    name = request.form.get('name', 'Amigo')

    return render_template(
        'index.html',
        days_remaining=days_remaining,
        message=message,
        random_gift=random_gift,
        name=name
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
