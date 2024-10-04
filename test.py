from math import gcd
from functools import reduce
from collections import Counter

def pgcd_multiple(numbers):
    return reduce(gcd, numbers)

def majority_gcd(numbers):
    count = Counter(numbers)
    majority_threshold = len(numbers) // 2
    for num in count:
        if count[num] > majority_threshold:
            return num
    return None

def filter_values(numbers):
    majority_value = majority_gcd(numbers)
    if majority_value is None:
        return numbers  # No majority value found
    return [num for num in numbers if gcd(num, majority_value) == majority_value]

# Liste des nombres
numbers = [32, 216, 88, 312, 216, 496, 264, 200, 280, 160, 160, 592, 120, 538, 88, 606, 469, 26, 160, 304, 485, 270, 393, 316, 272, 192, 272, 121, 133, 25]

# Filtrer les valeurs gênantes
filtered_numbers = filter_values(numbers)
print("Liste filtrée :", filtered_numbers)
