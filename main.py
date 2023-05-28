
import tkinter as tk
import requests
import datetime
from config import APP_ID,API_KEY,USERNAME,PASS
from requests.auth import HTTPBasicAuth

EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT="https://api.sheety.co/5031db1f0702a807ea33cc079d1a8309/myWorkouts/workouts"

def button_click():
    ex = input_field.get()
    ex_head = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    ex_post_params = {
        "query": ex,
        "gender": "male",
        "weight_kg": 100,
        "height_cm": 180,
        "age": 21
    }

    res1 = requests.post(url=EXERCISE_ENDPOINT, headers=ex_head, json=ex_post_params)
    print(res1.text)
    date = datetime.date.today().strftime("%m-%d-%Y")
    time = datetime.datetime.now().time().strftime("%H:%M:%S")
    for exes in res1.json()["exercises"]:
        par = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exes["name"].title(),
                "duration": exes["duration_min"],
                "calories": exes["nf_calories"]
            }
        }
        basic=HTTPBasicAuth(USERNAME,PASS)
        po = requests.post(url=SHEETY_ENDPOINT, json=par,auth=basic)



# Create the tkinter window
window = tk.Tk()

# Create a canvas
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

label = tk.Label(canvas, text="Enter your exercise")
canvas.create_window(200, 100, window=label)

# Create an input field
input_field = tk.Entry(canvas)
canvas.create_window(200, 150, window=input_field)

# Create a button
button = tk.Button(canvas, text="Log my Exercise", command=button_click,)
canvas.create_window(200, 200, window=button)

# Start the tkinter event loop
window.mainloop()