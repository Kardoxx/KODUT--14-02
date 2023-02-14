#Kardo-Tamm_IS22
# Avage fail lugemiseks
with open("sammud.txt", "r") as f:
    # Read the lines of the file into a list of integers
    steps_data = [int(line.strip()) for line in f.readlines()]

# Arvutab sammude koguarvu
total_steps = sum(steps_data)
print("Total number of steps for the week:", total_steps)

# Arvutab keskmise sammude arvu päevas
average_steps = total_steps / len(steps_data)
print("Average number of steps per day:", average_steps)

# Leidke kõige suurema ja väikseima sammuga päev
max_steps = max(steps_data)
min_steps = min(steps_data)
max_day = steps_data.index(max_steps) + 1
min_day = steps_data.index(min_steps) + 1

# Kirjutab tulemused
print("Day with the most steps:", max_day, "with", max_steps, "steps")
print("Day with the least steps:", min_day, "with", min_steps, "steps")