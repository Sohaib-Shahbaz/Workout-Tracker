import os
import requests
from datetime import datetime

EXERCISE_ENDPOINT = "<NUTRITION_API_ENDPOINT>"  
APP_ID = os.getenv("NUTRITION_APP_ID") or "<NUTRITION_APP_ID>"
API_KEY = os.getenv("NUTRITION_API_KEY") or "<NUTRITION_API_KEY>"

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT") or "<SHEETY_API_ENDPOINT>"

user_query = input("Describe your exercise (e.g. 'ran 3 miles'): ").strip()

payload = {
    "query": user_query,
    "weight_kg": 80,
    "height_cm": 180,
    "age": 22,
    "gender": "male",
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(EXERCISE_ENDPOINT, headers=headers, json=payload, timeout=15)

try:
    response.raise_for_status()
except requests.HTTPError:
    print("Nutrition API Status:", response.status_code)
    print("Nutrition API Body:", response.text)
else:
    data = response.json()
    exercises = data["exercises"]

    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")

    for ex in exercises:
        name = ex["name"]
        duration = ex["duration_min"]
        calories = ex["nf_calories"]

        row = {
            "date": date_str,
            "time": time_str,
            "exercise": name.title(),
            "duration": duration,
            "calories": calories,
        }

        print(row)
        print(f"{name.title()} | {duration} min | {calories} kcal")

        sheety_payload = {"workout": row}
        sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_payload, timeout=15)

        try:
            sheety_response.raise_for_status()
        except requests.HTTPError:
            print("Sheety Status:", sheety_response.status_code)
            print("Sheety Body:", sheety_response.text)
        else:
            print("Uploaded to sheet ✅")