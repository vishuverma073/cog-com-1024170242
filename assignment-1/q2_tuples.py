"""Q2 - Tuples"""

roll_no = 1024170242

L = [int(d) * 10 for d in str(roll_no)]
scores = tuple(L[:8])
print("scores =", scores)

highest = max(scores)
lowest = min(scores)
print("highest:", highest, "at index", scores.index(highest))
print("lowest:", lowest, "appears", scores.count(lowest), "time(s)")

# a tuple is immutable so it has no .reverse() of its own - reversed() builds a fresh sequence instead
print("reversed as list:", list(reversed(scores)))

value = int(input("Enter a score to search for: "))
if value in scores:
    print(value, "first occurs at index", scores.index(value))
else:
    print(value, "is not present in scores")

try:
    scores[0] = 100
except TypeError as err:
    print("Error raised:", err)
    # tuples block item assignment entirely; the same line on a list would have worked since lists are mutable

first, second, *rest = scores
print("first:", first)
print("second:", second)
print("rest:", rest)
