"""Q1 - Lists"""

roll_no = 1024170242

L = [int(d) * 10 for d in str(roll_no)]
print("L =", L)

L.append(55)
print("after append(55):", L)  # 55 gets added at the very end of the list

L.insert(3, 99)
print("after insert(3, 99):", L)  # 99 takes index 3 and everything from there shifts one step right

L.remove(70)
print("after remove(70):", L)

popped = L.pop(2)
print("after pop(2):", L, "| removed value was", popped)

L.sort()
print("ascending:", L)

L.sort(reverse=True)
print("descending:", L)

print("first three:", L[:3])
print("last three:", L[-3:])

avg = sum(L) / len(L)
above_avg = [n for n in L if n > avg]
print("average of L:", avg)
print("elements greater than average:", above_avg)
