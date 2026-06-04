# mylist = ["apple","banana","cherry","mango","kiwi"]#index = 0 to 4, length = 5
# mylist[1:3] = ["papaya","pineapple"]
# print(mylist)

# basket = ["apple","orange","banana","orange"]
# basket.pop(3)
# print(basket)


#
# basket = ["apple","orange","banana"]
# for y in basket:
#     print(y)


fruits = ["apple","orange","banana","kiwi","papaya"]
basket = [x for x in fruits if "a" in x]
print(basket)
