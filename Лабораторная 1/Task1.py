numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_2 = numbers[:4] + numbers[5:]
lenght = len(numbers)
sum_numbers_2 = sum(numbers_2)
average = round(sum_numbers_2 / lenght, 2)
numbers[4] = average
print("Измененный список:", numbers)
