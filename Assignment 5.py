#1.   Creates a dictionary where student names are keys and their marks are values.
#2.   Asks the user to input a student's name.
#3.   Retrieves and displays the corresponding marks.
#4.   If the student’s name is not found, display an appropriate message.



    # Step 1: Create a dictionary with student names and their marks
students = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "David": 88,
        "Eva": 90
    }

    # Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

    # Step 3 & 4: Retrieve and display marks or show message if not found
if name in students:
        print(f"{name}'s marks: {students[name]}")
else:
        print(f"Student '{name}' not found in the records.")

'''creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_first_five = first_five[::-1]

# Step 4: Print both the extracted list and the reversed list
print("Extracted first five elements:", first_five)
print("Reversed list:", reversed_first_five)







