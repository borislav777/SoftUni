happiness = input().split()
factor = int(input())
happiness_plus_factor = [int(num) * factor for num in happiness]
avg_happines = sum(happiness_plus_factor) / len(happiness_plus_factor)
filtered_happines = list(filter(lambda el: el >= avg_happines, happiness_plus_factor))
half_n = len(happiness_plus_factor) / 2
if half_n <= len(filtered_happines):
    print(f"Score: {len(filtered_happines)}/{len(happiness_plus_factor)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happines)}/{len(happiness_plus_factor)}. Employees are not happy!")


