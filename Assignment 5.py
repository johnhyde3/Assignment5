#1.   Creates a dictionary where student names are keys and their marks are values.
#2.   Asks the user to input a student's name.
#3.   Retrieves and displays the corresponding marks.
#4.   If the student’s name is not found, display an appropriate message.

students = {'john':55,'hyde': 69,'pavan': 23}
Name= input("Enter student name: ")
if Name in students:
    print("Marks:",students[Name])
else:
    print("Sorry, you are not examined.")


'''creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

john = [1,2,3,4,5,6,7,8,9,10]
b = john[0:5]
hyde = john[0:5]
c = hyde[::-1]
print(b,c)







