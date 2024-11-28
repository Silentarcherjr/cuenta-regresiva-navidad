from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def countdown_to_christmas():
    today = datetime.now()
    christmas = datetime(today.year, 12, 25)
    
    # Si ya pasó Navidad este año, calcula para el próximo año
    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)
    
    days_remaining = (christmas - today).days
    return render_template('index.html', days_remaining=days_remaining)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

