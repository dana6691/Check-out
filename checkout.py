cart=list()
def findinventory(barcode):
    boxfile = open("inventory.txt")
    box = None
    for line in boxfile:
        if barcode in line:
            box=line.split(",")
    return box
while True:
    barcode = input("enter item barcode: ")
    item=findinventory(barcode)
    if(item!=None):
        print(item[1]+ ","+item[2]+ ","+item[3])
        cart.append(item)
        print(cart)
    else:
        print("item not in inventory")
    a_barcode = input("Add more? (y/n)")
    if (str(a_barcode).lower()!='y'):
        break;
    
                     