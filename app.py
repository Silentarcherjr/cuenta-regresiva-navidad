from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def countdown():
    # Fecha actual
    today = datetime.now()
    # Fecha de Navidad
    christmas = datetime(today.year, 12, 25)
    # Fecha de Año Nuevo
    new_year = datetime(today.year + 1, 1, 1)

    # Si ya pasó Navidad este año, calcula para el próximo año
    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)

    # Calcular los días restantes de forma precisa
    time_difference_christmas = christmas - today
    days_to_christmas = time_difference_christmas.days + (1 if time_difference_christmas.seconds > 0 else 0)

    time_difference_new_year = new_year - today
    days_to_new_year = time_difference_new_year.days + (1 if time_difference_new_year.seconds > 0 else 0)

    # Mensajes personalizados
    if days_to_christmas > 10:
        message_christmas = "¡Aún hay tiempo para prepararte para Navidad!"
    elif days_to_christmas > 0:
        message_christmas = "¡La Navidad está muy cerca!"
    else:
        message_christmas = "¡Feliz Navidad! 🎅🎄"

    if days_to_new_year > 0:
        message_new_year = "¡El Año Nuevo está por llegar!"
    else:
        message_new_year = "¡Feliz Año Nuevo! 🎉🎆"

    # Generar idea de regalo aleatoria
    gift_ideas = ["Un libro", "Un rompecabezas", "Un juego de mesa", "Una planta", "Unos auriculares"]
    random_gift = random.choice(gift_ideas)

    return render_template(
        'index.html',
        days_to_christmas=days_to_christmas,
        days_to_new_year=days_to_new_year,
        message_christmas=message_christmas,
        message_new_year=message_new_year,
        random_gift=random_gift
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


