#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(num for num in numbers if num % 2 == 0)
print(even_sum)

#2
strings_list = ["Olympic College", "The Olympic Spirit", "Olympic College Athletes", "Sports", "Olympic", "School", "Olympic Northwest", "Homework"]
count = sum(1 for string in strings_list if "Olympic" in string)
print(count)

#3
strings = ["Hi", "Olympic", "College", "Hello", "Animals", "A", "Aidrin", "Is", "And"]
filtered_strings = [s for s in strings if len(s) > 3]
print(filtered_strings)

#4
def count_positive_negative(numbers):
    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)

    print(f"Positive numbers count: {positive_count}")
    print(f"Negative numbers count: {negative_count}")

numbers_list = [10, -5, 3, -1, 0, 7, -8, -12]
count_positive_negative(numbers_list)

#5
original_list = [1, 2, 3, 4, 5]
squared_list = []

for number in original_list:
    squared_list.append(number ** 2)

print(squared_list)
