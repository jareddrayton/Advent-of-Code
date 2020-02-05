limits = (171309,643603)

def increasing(number):

    split_number = [int(x) for x in str(number)]
    
    # Check that digits increase
    for i in range(len(split_number) - 1):
        if split_number[i] <= split_number[i+1]:
            other_condition = True
        else:
            other_condition = False
            break    
    
    # Check that two adjacent digits are the same
    for i in range(len(split_number) - 1):
        if split_number[i] == split_number[i+1]:
            second_condition = True
            break
        else:
            second_condition = False

    return number, other_condition, second_condition

results_1 = []

for i in range(171309, 643603):

    if increasing(i)[1:] == (True, True):
        results_1.append(increasing(i)[0])
        
print("Part A Result:", len(results_1))

##################################################################################

results_2 = []

for number in results_1:
    split_number = [int(x) for x in str(number)]
    
    for digit in split_number:
        if split_number.count(digit) == 2:
            results_2.append(number)
            break  

print("Part B Result:", len(results_2))