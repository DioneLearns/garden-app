def get_user_input():
    season = input("Enter the current season (summer/winter): ").lower()
    plant_type = input("Enter your plant type (flower/vegetable): ").lower()
    return season, plant_type

def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"

def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

def main():
    season, plant_type = get_user_input()
    advice = get_season_advice(season) + get_plant_advice(plant_type)
    print(advice)

if __name__ == "__main__":
    main()
