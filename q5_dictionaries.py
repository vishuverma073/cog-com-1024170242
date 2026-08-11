"""Q5 - Dictionaries"""

my_dict = {
    "name": "Vishu Verma",
    "roll_no": "1024170242",
    "branch": "CSE",
    "age": 20,
    "city": "Ludhiana",
}
print("original:", my_dict)

my_dict["location"] = my_dict.pop("city")
print("city renamed to location:", my_dict)

my_dict["cgpa"] = 8.4
print("after adding cgpa:", my_dict)

my_dict["age"] += 1
print("after ageing by a year:", my_dict)

copy_for_pop = dict(my_dict)
removed = copy_for_pop.pop("branch")
print("pop() gave back:", removed)
print("copy after pop:", copy_for_pop)

copy_for_del = dict(my_dict)
del copy_for_del["branch"]
print("copy after del:", copy_for_del)
# pop() hands the removed value back so you can still use it, del only wipes the key and returns nothing

for key, value in my_dict.items():
    print(f"{key} -> {value}")

if "email" in my_dict:
    print("email:", my_dict["email"])
else:
    print("email is not stored in this dictionary")

friend_dict = {
    "name": "Aman Gupta",
    "roll_no": "1024170199",
    "branch": "ECE",
    "age": 21,
    "city": "Jaipur",
}

merged = {**my_dict, **friend_dict}
print("merged:", merged)
# whichever dictionary is unpacked last wins the clash, so friend_dict overwrites the shared keys

only_strings = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("string values only:", only_strings)
