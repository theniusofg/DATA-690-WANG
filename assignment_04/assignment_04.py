# my original attempt at solving the problem without looking at the steps assigned in the hmwk

import re

# this is my todo list
# 1. check for '*' replace with '' make int
# 2. check for ',' replace with '' make int
# 3. check for '$' replace with '' make int
# 4. check for 'Billion' replace with '' make int and multiply by 10e9 make it
# 5. check for ' cents' replace with '' make int and divide by 100
# 6. check for '\n' replace with '' 



# open file and push contents to working variable 'rawdata'
with open("census_cost.txt", "rt") as f:
  rawdata = f.readlines()


# split data by line 
data_lines = [line.split('\t') for line in rawdata]

# store top2 lines and print
top2 = ''.join([','.join(line.split('\t')) for line in rawdata[:2]])

# 
working_data = data_lines[2:]


def mknumstr(a_str):
  return re.sub('[^0-9\.]', '', a_str)

def is_billion(a_str):
  return False if a_str.find('Billion') == -1 else True

def is_cents(a_str):
    return False if a_str.find('cents') == -1 else True



def prep_data(a_str):
  if (is_billion(a_str)):
    return int(float(mknumstr(a_str))*10e8)
  elif (is_cents(a_str)):
    return round(float(mknumstr(a_str))/100, 4)
  else:
    return mknumstr(a_str)

 
clean_data = '\n'.join([','.join(map(str,[(prep_data(a_str)) for a_str in lst])) for lst in working_data])

print (top2, clean_data)