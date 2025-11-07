"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [12, 15, 14, 10, 9, 13, 16]
city_population = {
    "Riga": 630000,
    "Tallinn": 440000,
    "Vilnius": 560000,
    "Warsaw": 1790000,
    "Berlin": 3700000
}

# TODO: Compute aggregates
# Average temperature
average_temperature = sum(temperatures) / len(temperatures)

# Find city with the largest population
largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]

# Find city with the smallest population
smallest_city = min(city_population, key=city_population.get)
smallest_population = city_population[smallest_city]

# Total population across all cities
total_population = sum(city_population.values())

# TODO: Print results

print(f"Average temperature for the week: {average_temperature:.2f} °C")
print(f"Highest population: {largest_city} - {largest_population:,} people")
print(f"Smallest population: {smallest_city} - {smallest_population:,} people")
print(f"Total population of all cities: {total_population:,} people")