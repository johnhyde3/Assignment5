#1.   Creates a dictionary where student names are keys and their marks are values.
#2.   Asks the user to input a student's name.
#3.   Retrieves and displays the corresponding marks.
#4.   If the student’s name is not found, display an appropriate message

students = {'john': 56,'hyde': 59,'menthula': 89}
name = input("Enter the student's name: ")
if name in students:
        print(f"{name}'s marks: {students[name]}")
else:
        print(f"Student '{name}' not found in the  exam records.")

'''creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

numbers = [1,2,3,4,5,6,7,8,9,10]
firstfive = numbers[:5]
reversedfirstfive = firstfive[::-1]
print("Extracted first five numbers:", firstfive)
print("Reversed list:", reversedfirstfive)







