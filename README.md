# Workout Tracker

A simple Python script that takes a natural-language workout description (e.g. **"ran 3 miles"**) and:
1) calculates estimated calories + duration using the **Nutrition & Exercise API**
2) logs the results into **Google Sheets** using **Sheety**

## Features
- Natural language workout input (single or multiple activities)
- Automatically adds **Date, Time, Exercise, Duration, Calories**
- Stores everything neatly in Google Sheets

## Example
Input:
- `ran 3 miles and walked 20 min`

Output (logged to Google Sheets):
- Running | 22 min | 130 kcal
- Walking | 20 min | 85 kcal

## Setup

### 1) Install requirements
```
pip install requests
```
