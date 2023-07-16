# Sets in Python

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

## Operations:
Python provides several operations that can be performed on sets. Here are the most common ones:

1. **Union (`union()` or `|`):** Returns a set which is the union of sets.

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.union(set2))  # Outputs: {1, 2, 3, 4, 5}
    print(set1 | set2)       # Outputs: {1, 2, 3, 4, 5}
    ```

2. **Intersection (`intersection()` or `&`):** Returns a set which is the intersection of sets.

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.intersection(set2))  # Outputs: {3}
    print(set1 & set2)              # Outputs: {3}
    ```

3. **Difference (`difference()` or `-`):** Returns a set which is the difference of two sets.

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.difference(set2))  # Outputs: {1, 2}
    print(set1 - set2)            # Outputs: {1, 2}
    ```

4. **Symmetric Difference (`symmetric_difference()` or `^`):** Returns a set which is the symmetric difference of two sets.

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.symmetric_difference(set2))  # Outputs: {1, 2, 4, 5}
    print(set1 ^ set2)                      # Outputs: {1, 2, 4, 5}
    ```

5. **Add (`add()`):** Adds an element to a set.

    ```python
    set1 = {1, 2, 3}
    set1.add(4)
    print(set1)  # Outputs: {1, 2, 3, 4}
    ```

6. **Remove (`remove()`):** Removes an element from a set. Raises a KeyError if the element does not exist.

    ```python
    set1 = {1, 2, 3}
    set1.remove(2)
    print(set1)  # Outputs: {1, 3}
    ```

7. **Discard (`discard()`):** Removes an element from a set if it is a member. If the element is not a member, do nothing.

    ```python
    set1 = {1, 2, 3}
    set1.discard(2)
    print(set1)  # Outputs: {1, 3}
    ```

8. **Pop (`pop()`):** Removes and returns an arbitrary set element. Raises KeyError if the set is empty.

    ```python
    set1 = {1, 2, 3}
    set1.pop()
    print(set1)  # Outputs: {2, 3} or {1, 3} or {1, 2}, arbitrary
    ```

9. **Clear (`clear()`):** Removes all elements from the set.

    ```python
    set1 = {1, 2, 3}
    set1.clear()
    print(set1)  # Outputs: set()
    ```

10. **Length (`len()`):** Returns the number of items in a set.

    ```python
    set1 = {1, 2, 3}
    print(len(set1))  # Outputs: 3
    ```

11. **Membership test (`in` or `not in`):** Test whether an item exists in a set.

    ```python
    set1 = {1, 2, 3}
    print(1 in set1)        # Outputs: True
    print(4 not in set1)    # Outputs: True
    ```

12. **Subset (`issubset()` or `<=`), Superset (`issuperset()` or `>=`), and Proper subset (`<`), Proper superset (`>`):** Test whether a set is a subset, superset, proper subset, or proper superset of another set.

    ```python
    set1 = {1, 2, 3}
    set2 = {1, 2}
    print(set2.issubset(set1))  # Outputs: True
    print(set1 <= set2)         # Outputs: False
    print(set1.issuperset(set2))  # Outputs: True
    print(set1 >= set2)          # Outputs: True
    print(set1 < set2)           # Outputs: False
    print(set1 > set2)           # Outputs: True
    ```

These operations make the set a very flexible and powerful data type in Python.
