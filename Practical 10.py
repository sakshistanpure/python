product_name=[]
product_price=[]

while True:
    print("_________PRODUCT INVENTORY SYSTEM_________")
    print("1. Insert Product.")
    print("2. Display Product.")
    print("3. Update Product.")
    print("4. Delete Product.")
    print("5. Search Product.")
    print("6. Sort Product.")
    print("7. Exit.")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        product=input("Enter your product: ")
        product_name.append(product)
                
        price=float(input("Enter your product price: "))
        product_price.append(price)
        print("Product Inserted Successfully.")
        
    elif choice==2:
        if len(product_name)==0:
            print("No Products Is Available")
            
        else:
            print("Products\tprice")
            
            for i in range(len(product_name)):
                print(product_name[i],"\t\t" ,product_price[i])
                
    elif choice==3:
        product2=input("Enter Product Name to Update: ")
        if product2 in product_name:
            product_name.index(product)
            
            new_price=int(input("Enter Updated Price: "))
            
                
    else:
        break
            
            
        
    
        

        