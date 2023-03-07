import requests
from bs4 import BeautifulSoup

http_text = requests.get("https://weather.com/en-CA/weather/tenday/l/63f4de10a8c7b229661a9674a3d0915b9740827451d381e82b730ca1b96bbbf5").text
soup = BeautifulSoup(http_text, 'lxml')
weather_data = soup.find_all('div', class_ = "DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF")
final_data = []

for day in weather_data:
    date = day.find('h3', class_= "DetailsSummary--daypartName--kbngc").text
    temp_section = day.find('div', class_ = "DetailsSummary--temperature--1kVVp")
    span_tags = temp_section.find_all('span')
    max_temp = span_tags[0].text
    min_temp = span_tags[1].span.text
    weather_condition = day.find('div', class_ = "DetailsSummary--condition--2JmHb").span.text
    chance = day.find('div', class_ = "DetailsSummary--precip--1a98O").span.text
    wind_section = day.find('div', class_ = "DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax").span.text
    wind_separated = wind_section.split()
    wind_direction = wind_separated[0]
    wind_speed = wind_separated[1] + wind_separated[2]
    
    final_data.append([date, max_temp, min_temp, weather_condition, chance, wind_direction, wind_speed])

print(final_data)

//change the local directory
with open("Python/ELEC390/ELEC390_Lab2.txt", 'w') as f:
        for data in final_data:
            f.write(str(data) + '\n')
