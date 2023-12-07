print("This is the Math Module:")
print("________________________")

# import math # this imports the entire module

# from math import pi, sqrt # You are importing functions from the module

# print(pi, sqrt(33))
print("\n\n\n")
print("Import math Module code snippet")
print("===============================")
import math
v1 = math.sqrt(36)
v2 = math.sqrt(12)
v3 = math.sqrt(2)
print(v1, v2, v3)
print("Using floor from math:")
print(math.floor(v1), math.floor(v3))
print("\n\nUsing ceil from math:")
print(math.ceil(v2), math.ceil(v3))

print("\n\n\n")
print("Alternate Import forms:")

import math as cooper # you can rename the module
print(cooper.sqrt(1234))

from math import log
print(log(128, 2))

from math import * # import math
print(sqrt(1234))














