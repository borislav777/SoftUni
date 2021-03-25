budget=float(input())
season=input()
destination=""
type_of_rest=""
if budget<=100:
    destination="Bulgaria"
    if season=="summer":
        budget*=0.30
        type_of_rest="Camp"
    elif season=="winter":
        budget*=0.70
        type_of_rest="Hotel"
elif budget<=1000:
    destination="Balkans"
    if season=="summer":
        budget*=0.40
        type_of_rest="Camp"
    elif season=="winter":
        budget*=0.80
        type_of_rest="Hotel"
elif budget>1000:
    destination="Europe"
    budget*=0.90
    type_of_rest="Hotel"
print(f"Somewhere in {destination}")
print(f"{type_of_rest} - {budget:.2f}")

