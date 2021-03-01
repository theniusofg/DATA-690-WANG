# rough draft created in repl.it
LIST_SIZE = 10

print(f'HI! I\'m a program. I preform mathematical operations. To get me to run I need you enter a set consisting of {LIST_SIZE} numbers, then I\'ll calculate the following operations for you: \n\nMinimum \nMaximum \nRange \nMean \nVariance \nStandard Deviation')

def get_data():
  a_list = []

  count = len(a_list)

  while count < LIST_SIZE:
    
    print (f'\nIt look\'s like we still need {LIST_SIZE - count} out of {LIST_SIZE} numbers to complete the set.')
    usr_input = input('\nPlease enter a whole number: ')
    
    try:
      usr_input = int(usr_input)
      a_list.append(usr_input)
      count = len(a_list)
      print (f'Thanks for entering {usr_input}, I\'m adding it to your set for safe keeping.')  

    except:
      print(f'Uh oh! it look\'s like you entered {usr_input}, that\'s not a whole number. But that\'s okay, please try again.')

  return a_list

def get_sum(some_list):
  some_sum = 0
  for num in some_list:
    some_sum += num
  return some_sum

def get_variance(some_list):
  some_sum = 0
  for num in some_list:
    some_sum += num**2
  return some_sum


# prepare data to be used in mathematical operations
usr_list = get_data()
usr_sum = get_sum(usr_list)
usr_list.sort()


# Minimum 
usr_min = usr_list[0]

# Maximum 
usr_max = usr_list[-1]

# Range (the difference between lowest and highest values)
usr_range = usr_max - usr_min

# Mean (sum of all values in a set divided by the number of values)
usr_mean = usr_sum / len(usr_list)

# Variance (all values squared and then take their sum)
usr_variance = get_variance(usr_list)

# Standard Deviation (square root of variance)
usr_std_dev = usr_variance**.5

# print the results out to the console for the user to view
result = f'''\n\nBeep boop beep brrzt. I calculated several mathematical operations based on your entries, {usr_list} they are displayed below \n\nMinimum: {usr_min}  \nMaximum: {usr_max}  \nRange: {usr_range} \nMean: {usr_mean} \nVariance: {usr_variance} \nStandard Deviation {usr_std_dev}'''
print(result)