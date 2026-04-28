##########
#
# SET
# ----------------
#
# 1. Unordered:
#       - Elements have no defined order and may appear in any sequence.
#
# 2. Unique Elements:
#       - Automatically removes duplicates; all elements must be hashable.
#
# 3. Mutable:
#       - Supports adding and removing elements after creation.
#
# 4. Unindexed:
#       - Does not support indexing or slicing; access is via iteration only.
#
# 5. Optimized for Membership Tests:
#       - Extremely fast lookups using hashing (avg O(1) contains checks).
#
# 6. Supports Set Operations:
#       - Includes union, intersection, difference, symmetric difference.
#
# 7. Literal Syntax:
#       - Defined using curly braces { } or the set() constructor.
#
##########

# Set
names = {"John", "Michael", "Allen", "Dave", "Rodger"}

## Unindexed
print(names[0])
print("Type Error. Sets are not unindexed elements")

for name in names:
    print(name, end=" ")

## Mutable
names.add("James")
names.add("Alejandro")
names.add("Jessie")
names.add("Hosea")
names.remove("Rodger")
names.remove("Dave")

print(names, end= " ")

if "Dave" in names:
    print("Dave is present today!")
else: 
    print("Dave is not present today!")
