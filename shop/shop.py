
product = input("enter a product: ")
f = open("product.txt","r")
lines = f.readlines()
f.close()
status = False
for i in range(len(lines)):
        model,price,inventory= lines[i].strip().split(",")
        if product == model and int(inventory) > 0:
                status = True
                print(price)
                print(inventory)
                command=input("buy: (y/n)")
                if command=="y":
                        inventory= int(inventory)-1
                        lines[i] = f"{model},{price},{inventory}\n"         
if status == False:
        print("dose not exist")
file = open("product.txt","w")
for line in lines:
        file.write(line)
f.close               
       









