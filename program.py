'''___________________________________PROBLEM STATEMENT____________________________________'''

'''
https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22
The above API is the REST GET API

Which gives you the response in JSON format and hourly weather forecast of London Location

I want you to write a program to get the option from the user and print the result based on the above API.

1. Get weather
2. Get Wind Speed
3. Get Pressure
0. Exit

If the user press 1,  Prompt the user for the date then print the temp of the input date.
If the user press 2,  Prompt the user for the date then print the wind.speed of the input date.
If the user press 3,  Prompt the user for the date then print the pressure of the input date.
If the user press 0,  Terminate the program.
The program should not terminate until the user press 0.
'''

'''_______________________________________SOLUTION_______________________________________'''

# importing requests and json
import requests

def getWeather(data,date_time):
    data = data['list']
    for indx in range(len(data)):
        if data[indx]['dt_txt'] == date_time:
            print("Temperature =",data[indx]['main']['temp'])
            break
    else:
        print("Enter proper Date & Time format as specified or Date and Time NOT FOUND")

def getWindSpeed(data,date_time):
    data = data['list']
    for indx in range(len(data)):
        if data[indx]['dt_txt'] == date_time:
            print("Wind Speed =",data[indx]['wind']['speed'])
            break
    else:
        print("Enter proper Date & Time format as specified or Date and Time NOT FOUND")


def getPressure(data,date_time):
    data = data['list']
    for indx in range(len(data)):
        if data[indx]['dt_txt'] == date_time:
            print("Pressure =",data[indx]['main']['pressure'])
            break
    else:
        print("Enter proper Date & Time format as specified or Date and Time NOT FOUND")


if __name__ == "__main__":
    # upadting the URL
    URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
    # getting data in the json format
        data = response.json()
        print("Enter a number")
        while True:
            print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
            try:
                num = int(input())
                if num == 1:
                    date_time = str(input("Enter Date & Time (YYYY-MM-DD HH:00:00)\nEnter the Date and time between \"2019-03-27 18:00:00\" and \"2019-03-31 17:00:00\" \n(Example: 2019-03-27 18:00:00): "))
                    getWeather(data,date_time)
                elif num == 2:
                    date_time = str(input("Enter Date & Time (YYYY-MM-DD HH:00:00)\nEnter the Date and time between \"2019-03-27 18:00:00\" and \"2019-03-31 17:00:00\" \n(Example: 2019-03-27 18:00:00): "))
                    getWindSpeed(data,date_time)
                elif num == 3:
                    date_time = str(input("Enter Date & Time (YYYY-MM-DD HH:00:00)\nEnter the Date and time between \"2019-03-27 18:00:00\" and \"2019-03-31 17:00:00\" \n(Example: 2019-03-27 18:00:00): "))
                    getPressure(data,date_time)
                elif num == 0:
                    print("_________________________EXITING______________________")
                    print("________________________THANK YOU_____________________")
                    break
                else:
                    print("Enter a proper number")
                    continue
            except:
                print("Enter a integer type")
                continue
    else:
       # showing the error message
       print("Error in the HTTP request")