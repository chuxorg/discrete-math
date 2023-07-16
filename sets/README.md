# Sets

Chuck Sailer - July 16, 2023

In Python, a set is a built-in data type that can be used to store multiple items in a single variable. It is one of Python's four built-in data types for collections, which also includes List, Tuple, and Dictionary. 

A set is unordered, meaning that the items in a set do not have a defined order. Sets also cannot have duplicate values. This makes sets useful for storing items when their order does not matter and when you want to ensure that an item only appears once.

Here is how you can define a set in Python:

```python
my_set = {1, 2, 3}
print(my_set)
```

In this example, `my_set` is a set that contains the integers 1, 2, and 3. If you run this code, Python will output `{1, 2, 3}`.

You can also create a set from a list using the built-in `set()` function:

```python
my_list = [1, 2, 3, 3, 4, 4, 5, 5]
my_set = set(my_list)
print(my_set)
```

In this case, the list `my_list` contains duplicates. When you pass `my_list` to `set()`, Python creates a new set that includes each unique element from `my_list`. If you run this code, Python will output `{1, 2, 3, 4, 5}`. As you can see, the duplicates from `my_list` are not included in `my_set`.