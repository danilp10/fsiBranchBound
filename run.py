# Search methods

import search
import utils

ab = search.GPSProblem('A', 'B', search.romania)
result = search.branch_and_bound_search(ab)
result2 = search.branch_and_bound_search_with_sub(ab)
print("Path without subestimation:", result.path())
print("Path with subestimation:", result2.path())
print("------------------------------------------------------")

zg = search.GPSProblem('Z', 'G', search.romania)
result = search.branch_and_bound_search(zg)
result2 = search.branch_and_bound_search_with_sub(zg)
print("Path without subestimation:", result.path())
print("Path with subestimation:", result2.path())
print("------------------------------------------------------")

bl = search.GPSProblem('B', 'L', search.romania)
result = search.branch_and_bound_search(bl)
result2 = search.branch_and_bound_search_with_sub(bl)
print("Path without subestimation:", result.path())
print("Path with subestimation:", result2.path())



#print(search.branch_and_bound_search(ab).path()) # Result: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
#print(search.branch_and_bound_search_with_sub(ab).path())





#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
