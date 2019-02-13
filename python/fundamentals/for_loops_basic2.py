#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(len(list)):
        if list[i] >0:
            list[i] = "big"
    return list
print(biggie_size([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(list):
    pos_sum = 0
    for i in range(len(list)):
        if list[i] >0:
            pos_sum = pos_sum +1
    list[len(list)-1] = pos_sum
    return list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum_total(list):
    total = 0
    for i in range(0,len(list),1):
        total = total + list[i]
    return total
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def average(my_list):
    total_sum = 0
    for i in range(len(my_list)):
        total_sum = total_sum + my_list[i]
    return total_sum/len(my_list)
print(average([1,2,3,4]))
print(average([15,15,15]))

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def list_length(list):
    return len(list)
print(list_length([37,2,1,-9]))
print(list_length([]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def min_list(list):
    min_number=0
    if list == []:
        return False
    for i in range(len(list)):
        if min_number > list[i]:
            min_number = list[i]
    return min_number
print(min_list([37,2,1,-9]))
print(min_list([]))

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def maximum_list(list):
    max_number=0
    if list == []:
        return False
    for i in range(len(list)):
        if max_number < list[i]:
            max_number = list[i]
    return max_number
print(maximum_list([37,2,1,-9]))
print(maximum_list([]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ult_analysis(list):
    new_dict={'sumTotal':0, 'average':0, 'minimum':0, 'maximum':0}
    for i in range(len(list)):
        new_dict['sumTotal'] = new_dict['sumTotal'] + list[i]
        if new_dict['minimum'] > list[i]:
            new_dict['minimum'] = list[i]
        elif new_dict['maximum'] < list[i]:
            new_dict['maximum'] = list[i]
    new_dict['average'] = new_dict['sumTotal']/ len(list)
    new_dict['lengthlist'] = len(list)
    return new_dict
print(ult_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    for i in range(int(len(list)/2)):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list  
print (reverse_list([37,2,1,-9]))

