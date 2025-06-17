def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

my_list = [10,30,60,80]
print("Average:", calculate_average(my_list))