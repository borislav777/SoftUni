countries = input().split(", ")
cities = input().split(", ")

print(*[f"{countries[i]} -> {cities[i]}" for i in range(len(countries))], sep='\n')
