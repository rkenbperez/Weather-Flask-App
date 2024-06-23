from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    response = requests.get(url)
    data = response.json()

    error_message = None
    if data['cod']!= 200:
       error_message = 'City not found.'

    weather_data = data['weather'][0]
    main_data = data['main']
    wind_data = data['wind']

    description = weather_data['description'].capitalize()
    current_temperature = f'{main_data["temp"]}°C'
    min_temperature = f'{main_data["temp_min"]}°C'
    max_temperature = f'{main_data["temp_max"]}°C'
    humidity = f'{main_data["humidity"]}%'
    wind_speed = f'{wind_data["speed"]} m/s'

    return render_template('index.html', city=city, description=description,
                           current_temperature=current_temperature,
                           min_temperature=min_temperature,
                           max_temperature=max_temperature,
                           humidity=humidity,
                           wind_speed=wind_speed,
                           error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
