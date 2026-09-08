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
            print("\nProducts\tprice")
            
            for i in range(len(product_name)):
                print(product_name[i],"\t\t" ,product_price[i])
                
    elif choice==3:
        product2=input("Enter Product Name to Update: ")
        if product2 in product_name:
            index=product_name.index(product2)
            new_price=int(input("Enter Updated Price: "))  
            product_price[index]=new_price
            print("Product Updated Successfully.")
        else:
            print("Product Not Found.")
            
    elif choice==4:
        product3=input("Enter Product Name to Delete: ")
        if product3 in product_name:
            index=product_name.index(product3)
            product_name.pop(index)
            product_price.pop(index)
            print("Product Deleted Successfully.")
        else:
             print("Product Not Found.")
             
    elif choice==5:
        product4=input("Enter Product Name to Search: ")
        if product4 in product_name:
            index=product_name.index(product4)
            print("Product Found.") 
            print("Product:", product_name[index])
            print("Price:", product_price[index])
        else:
           print("Product Not Found.")
           
    elif choice==6:
        if len(product_name) == 0:        
            print("No Products Is Available")
        else:
            for i in range(len(product_name)):
                
                for j in range(i + 1, len(product_name)):
                    if product_name[i] > product_name[j]:
                        product_name[i], product_name[j] = product_name[j], product_name[i]
                        product_price[i], product_price[j] = product_price[j], product_price[i]
                        print("Products Sorted Successfully.")
                        print(product_name,product_price)
                                    
    elif choice == 7:    
        print("Thank You for Using Product Inventory System.")
        break
            
    else:
        print("Invalid Choice. Please Try Again.")
            
            
                        
    
            
        
    
        

        