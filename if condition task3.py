australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

def find_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None
first_city = input("Enter the first city: ")
second_city = input("Enter the second city: ")
first_city_country = find_country(first_city)
second_city_country = find_country(second_city)

if first_city_country and second_city_country:
    if first_city_country == second_city_country:
        print(f"Both cities are in {first_city_country}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not found in the lists")
