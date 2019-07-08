

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        # max length of array
        self.capacity = capacity
        # occupied length of array
        self.count = 0
        # underlying data structure
        self.elements = [None] * capacity


# Double the size of the given array
def resize_array(arr):
    # set new capacity to double
    new_capacity = arr.capacity * 2
    # create new elements storage unit
    new_elements = [None] * new_capacity
    # copy over the elements
    for i in range(arr.count):
        new_elements[i] = arr.elements[i]
    # set the new elements and capacity to the current array instance
    arr.elemets = new_elements
    arr.capacity = new_capacity


# Return an element of a given array at a given index
def array_read(arr, index):
    # Throw an error if array is out of the current count
    if index >= arr.count:
        print("ERROR: elements " + str(index) + " is out of range.")
        return None
    return arr.elements[index]


# Insert an element in a given array at a given index
def array_insert():
    # Throw an error if array is out of the current count

    # Resize the array if the number of elements is over capacity

    # Move the elements to create a space at 'index'
    # Think about where to start!

    # Add the new element to the array and update the count
    pass


# Add an element to the end of the given array
def array_append():

    # Hint, this can be done with one line of code
    # (Without using a built in function)

    # Your code here
    pass


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove():
    # Your code here
    pass


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop():
    # Throw an error if array is out of the current count
    # Your code here
    pass


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
# arr = array(1)

# array_insert(arr, "STRING1", 0)
# array_print(arr)
# array_pop(arr, 0)
# array_print(arr)
# array_insert(arr, "STRING1", 0)
# array_append(arr, "STRING4")
# array_insert(arr, "STRING2", 1)
# array_insert(arr, "STRING3", 2)
# array_print(arr)
