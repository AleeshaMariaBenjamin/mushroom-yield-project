sensor = {
    "temperature": 24.5,
    "humidity": 85,
    "co2": 650,
    "yield": 12.8  
}

print("Sensor Readings")
print(f"Temperature: {sensor['temperature']} °C")
print(f"Humidity: {sensor['humidity']} %")
print(f"CO2: {sensor['co2']} ppm")
print(f"Yield: {sensor['yield']} kg/m²")  

print("Smoke test passed")