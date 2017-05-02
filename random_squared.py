#small_numbers = [num for num in nums if num < 6]
#three_letters_words = [ word.title() for word in words if len(word) == 3 ]

from random import sample

my_range = sample(range(0,49), 20)
my_squared = [number**2 for number in my_range]
print(my_range)
print(my_squared)