#list of mixed data elements
data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None, {"name": "John", "age": 25}]

#input for index
print("Enter index:")

index = int(input())

index_type = type(index)

index_message = None

iterable_list = ["list", "str", "dict"]
numeric_list = ["int", "float"]

if index_type in iterable_list:
    index_message = "This element is iterable"
if index_type in numeric_list:
    index_message = "This element is numeric"

#Element: 2024, Type: int, Message: This element is numeric.

print(f"Element: {index}, Type: {index_type}, Message: {index_message}.")
