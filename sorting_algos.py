#selection sort
#Insertion sort
#bubble sort
#quick sort
#merge sort
#shell sort

dic = {"data": "first line",
       "comp_1": "another instance",
       "comp_2": "building a list"}


# for idx, element in enumerate(dic):
#     print(f"the index is of {idx} while the key is {element}")
#     print(f"'{dic[element]}', is the content of this index")


dic_3 = {
    "A": {0: None},
    "B": {2: "A"},
    "C": {5: "A"},
    "D": {7: "B"},
    "E": {8: "C"}
}

for idx, element in enumerate(dic_3):
    # print(f"'{dic_3[element]}', is the content of this index")

    for a, b in enumerate(dic_3[element]):
        print(f"{b} is the distance from {element} to {dic_3[element][b]}")


for ky, val in dic_3.items():
    print(f"using items function to print key of {ky} with values {val}")