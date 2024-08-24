import random


num_rolls = 20

count_6 = 0
count_1 = 0
count_two_sixes_in_a_row = 0
previous_roll = None
for _ in range(num_rolls):
    current_roll = random.randint(1, 6)
    
    if current_roll == 6:
        count_6 += 1
    elif current_roll == 1:
        count_1 += 1
    
    if previous_roll == 6 and current_roll == 6:
        count_two_sixes_in_a_row += 1
    
    previous_roll = current_roll
print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times rolled two 6s in a row:", count_two_sixes_in_a_row)
