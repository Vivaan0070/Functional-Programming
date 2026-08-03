# 1.
elements = int(input("Enter the number of elements: "))
list_of_elements = []
for i in range(elements):
    num = int(input("Enter element {}: ".format(i + 1)))
    list_of_elements.append(num)
print("List of elements:", list_of_elements)
print("the greatest number is:", max(list_of_elements), "the smallest number is:", min(list_of_elements))
list_of_elements.sort()
print("the min and max is: ", list_of_elements[0], "and", list_of_elements[-1])

# 2.
list1 = [1, 2, 3]
list1[0], list1[-1] = list1[-1], list1[0]  # Swapping first and last elements
#a = list1[0]
#b = list1[-1]
#list1[0] = b
#list1[-1] = a
print("List after swapping first and last elements:", list1)

# 3.
tupple1 = ("math", "java", "python", "physics", "chemistry")
for i in tupple1:
    print(i, end="\n")

    