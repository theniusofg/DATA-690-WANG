import random

# Write a program that generates 100 random integers 0 through 9
# make a 10x10 matrix of random numbers 0-9
matrix_10x10 = lambda: [[random.randint(0,9) for rand_num in range (10)] for lst in range(10)]


# Print them in a 10 by 10 matrix neatly arranged (one space between each number):

matrix_to_string = lambda some_matrix: '\n'.join([' '.join(str(num) + ' ' for num in lst) for lst in some_matrix])

# print (matrix_to_string(matrix_10x10()), '\n')


# If the random number is an odd number, print "@" instead. :

odd_num_to_at = lambda: [['@' if num%2 != 0 else num for num in lst] for lst in matrix_10x10()]

# print(matrix_to_string(odd_num_to_at()), '\n')


# Calculate and Print the total of each row like the following (use "*" to separate the total from the numbers):

def sum_matrix_row(some_matrix):
  sum_row = [sum(lst) for lst in some_matrix if type(lst) is list]
  
  [some_matrix[i].append('* '+ str(sum_row[i])) for i in range (len(some_matrix[0]))]
    
    
  return some_matrix

# print (matrix_to_string(sum_matrix_row(matrix_10x10())) , '\n')



# Optional: Surround the matrix with asterisks (*) like the following:
def beautiful_borders(some_matrix):
  border_row = '*' * (len(some_matrix) + 2)
  [(lst.append('*'), lst.insert(0, '*')) for lst in some_matrix]
  some_matrix.insert(0, border_row)
  some_matrix.append(border_row)

  return matrix_to_string(some_matrix)
  
# print(beautiful_borders(matrix_10x10()), '\n')



# Optional (challenging): Calculate and Print the total of each row and column like the following:

def sum_matrix_columns_rows(some_matrix):
  # print(matrix_to_string(some_matrix))
  sum_columns = [sum(lst) for lst in zip(*some_matrix)]
  some_matrix.append('*'*len(some_matrix))
  some_matrix.append(sum_columns)
  sum_matrix_row(some_matrix)
  return some_matrix


print (matrix_to_string(sum_matrix_columns_rows(matrix_10x10())))
