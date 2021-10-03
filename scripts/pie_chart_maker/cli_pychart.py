#!usr/bin/env python3
from matplotlib.pyplot import pie, show


print(
    "Please write a list of chart wedge names/titles seperated with a comma and space"
)
names = input("Names:\n")
name_list = names.split(", ")
print("Please write the values to each name in the same order and format")
values = input("Values:\n")
value_list = values.split(", ")

final_val = []
for n in value_list:
    final_val.append(float(n))

perc_list = []
for i in final_val:
    p = i / (sum(final_val)) * 100
    perc_list.append(p)

pie(
    x=perc_list,
    labels=name_list,
    radius=1.3,
)

show()
