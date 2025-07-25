import requests
api_key = "e3870c12a802ec0024ddc9b49a2e1743"
while True:
    city_name = input("City Name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        city = data["name"]
        weather = data["weather"][0]["main"]
        temp =data["main"]["temp"]
        description = data["weather"][0]["description"]
        print("--- Weather Report ---")
        print(f"City : {city}")
        print(f"Weather: {weather}")
        print(f'Tempertature: {temp}')
        print(f'Description: {description}')
    else:
        print("City not found")
    x= (input("Type Exit to stop: ")).lower()
    if x=='exit':
        print("Exit Successfully")
        break
    else:
        continue