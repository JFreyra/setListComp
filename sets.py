## // 17.04.21 // ##
## // Julius F // ##

def union(l1,l2):
    return l1+[x for x in l2 if x not in l1]

def intersection(l1,l2):
    return [x for x in union(l1,l2) if x in l1 and x in l2]

def setDiff(l1,l2):
    return [x for x in union(l1,l2) if x in l1 and x not in l2]

def symDiff(l1,l2):
    return union(setDiff(l1,l2),setDiff(l2,l1))

def cartProd(l1,l2):
    return [(x,y) for x in l1 for y in l2]

## Test Cases

print
print "All test cases are func([1,2,3],[2,3,4]) and func([2,3,4],[1,2,3])"

# Unions
print "Unions:"
print union([1,2,3],[2,3,4])
print union([2,3,4],[1,2,3])

# Intersection
print "Intersections:"
print intersection([1,2,3],[2,3,4])
print intersection([2,3,4],[1,2,3])

# Set Difference
print "Set Differences:"
print setDiff([1,2,3],[2,3,4])
print setDiff([2,3,4],[1,2,3])

# Symmetric Difference
print "Symmetric Differences:"
print symDiff([1,2,3],[2,3,4])
print symDiff([2,3,4],[1,2,3])

# Cartesian Product
print "Cartesian Products:"
print cartProd([1,2,3],[2,3,4])
print cartProd([2,3,4],[1,2,3])
