shop = []
dic = {
}
def add(name):
    if name in shop:
        print("Already in list")
    else:
        shop.append(name)
        print(name, "Item Added\n")

def remove_item(name):
    if name in shop:
        shop.remove(name)
        print(name, "Removed")
    else: 
        print("Item not in the list\n")

def search_item(name):
    if name in shop:
        print("True, item is present in the list")
    else:
        print("False, item is not present in the list")

def display_list():
    for n in shop:
        print(n)

# def binsear(name):
#     n = len(shop)

#     for i in shop:
#         le = len(i)
#         dic[le] = i
#     sorted(shop,reverse=True)
#     s = 0
#     e = n-1
#     ans = "NULL"

#     while s <= e :
#         if n == dic :
#             ans = name
#         elif 
#     ans = ans[::-1]
#     return ans


while True:
    var = str(input("Enter the grocery item to be added (Enter -1 to stop adding):"))
    if var == "-1":
        break
    else:
        add(var)

rem = str(input("Enter the grocery item to be removed:"))
remove_item(rem)

sear = str(input("\nEnter the grocery item to be searched:"))
search_item(sear)
# print(binsear(sear))

print("\nThe Current Grocery list is :")
display_list()
