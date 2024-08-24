australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Enter a city name: ")

if city_name in australia:
    print(f"{city_name} is in Australia")
elif city_name in uae:
    print(f"{city_name} is in UAE")
elif city_name in india:
    print(f"{city_name} is in India")
else:
    print("City not found in the lists")
