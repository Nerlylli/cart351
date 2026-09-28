import requests

#city argument
city = "Toronto"

#my api key -> you should add yours
api_key = "2ba267fc5ab5b4c99201b8efab509d99" 
url_with_city ="http://api.openweathermap.org/data/2.5/weather?q=" +city 
url_to_send = url_with_city + "&APPID=" + api_key 
#make the request
response = requests.get(url_to_send) 
#get the response as json
data = response.json() 

#print
print(data)
print(type(data))
print((data.keys))