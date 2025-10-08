# The readable approach:
total = 0
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(total)

# Or, as a one-liner:
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
