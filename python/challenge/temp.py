print("Enter the water temperature:")
temperature = int(input())

water_state = None
safety_message = None

if temperature >= 212:
    water_state = "Boiling"
    safety_message = "Caution: Hot!"

if temperature in range(115,211):
    water_state = "Hot"

if temperature in range(80, 115):
    water_state = "Warm"

if temperature in range(33, 80):
    water_state = "Cold"

if temperature < 33:
    water_state = "Frozen"
    safety_message = "Watch out for ice!"

print(water_state)

if(safety_message != None):
    print(safety_message)