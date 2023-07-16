A = {1,2,3,4}
B = {1,1,2,2,3,3,4}
C = {3,2,1,4}

# Sets A, B, and C are Equal (Axiom is that the order, duplicates do not matter)
print(A == C == B) # True

# Get the Union of C and B
print(C.union(B)) # Union of sets C and B is {1,2,3,4}
# You can also get a Union like this:
u = C | B
print(u)
