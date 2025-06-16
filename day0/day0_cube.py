## this function take the list as input
def cube_list(numbers):
    return [num**3 for num in numbers]

my_list = [1, 2, 3 , 5]
print("cubes:",cube_list(my_list))