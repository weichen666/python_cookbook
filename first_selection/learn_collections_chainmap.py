#!/usr/bin/env python

a = """

"""

_,*t, _ = a.split("\n")

m = [i.split(",")[0] for i in t]

r = ["'" + str(i) +"'" for i in m]
print (",".join(r))

