a = {"x": "x1", "y": "y1"}

# list out keys and values separately
key_list = list(a.keys())
val_list = list(a.values())

ind = val_list.index("2")
print(key_list[ind])

# a = "..   |   .-   --   |   ...-   ..   ...   ....   .-   .-..   |   -.   ---   .-.-.-   |   .----   "
# lis = a.split("|")
# print(lis)
#
#
# for n in lis:
#     n = n.strip()
#     for n1 in n:
#         lis2 = n1.split("   ")
#         print(lis2)

# a = "   ..._   __.."
# a = a.strip()
# print(a)
# lis = a.split("   ")
# print(lis)