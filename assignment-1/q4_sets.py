"""Q4 - Sets"""

roll_no = 1024170242

digits = [int(d) for d in str(roll_no)][:8]  # roll number has 10 digits, the question asks for 8
print("digits used:", digits)

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}
print("A =", A)
print("B =", B)

print("union:", A.union(B))
print("intersection:", A.intersection(B))

print("A - B:", A.difference(B))
print("B - A:", B.difference(A))
# difference() is one sided and keeps only what the left set has, while symmetric_difference() collects the leftovers of both sides in one go
print("symmetric difference:", A.symmetric_difference(B))

print("is A a subset of B:", A.issubset(B))
print("is B a superset of A:", B.issuperset(A))

x = int(input("Enter a value to remove from A: "))
A.discard(x)  # discard() quietly does nothing if x is missing, remove() would have crashed with a KeyError
print("A after discard:", A)
