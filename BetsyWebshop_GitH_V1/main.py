# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line
from models import *

# Connect to the database
db.connect()


def search(term):
    try:
        #search for products with names containing the given term(case-insentitive)
        products=Product.select().where(Product.name **f'%{term}%')
        #print the result
        if products:
            print(f"Products containing '{term}':")
            for product in products:
                print(f"ID:{product.product_id}, Name:{product.name},Description:{product.description},Price:{product.price},Stock:{product.quantity_description_amount_in_stock}")
        else:
             print(f"No products found containing'{term}'")

    except Exception as e:
        print(f"Error occurred: {e}")

def list_user_products(user_id):
    try:
        #retrieve the user from the database
        user=User.get(User.user_id==user_id)
        
        #Fetch all products owned by the user
        products=Product.select().where(Product.owner==user)
        list_i=[]
        for product in products:
           list_i.append(product.name) 
        print('product:',list_i)      
        return list_i
    except User.DoesNotExist:
        print( f"User with ID {user_id} does not exist")
        return f"User with ID {user_id} does not exist"
    except Exception as e:
        Print(f"Error:{e}")
        return f"Error:{e}"

def list_products_per_tag(tag_id):
   try:
      query=TagProduct.select().where(TagProduct.tag_id==tag_id)#w?y
      query_with_product=query.join(Product, on=(TagProduct.product_id==Product.product_id))
      products=query_with_product.select()
      
      for product in products:
          print(f"{product.product_id}, {product.product.name}, {product.product.description}, {product.product.price}, {product.product.quantity_description_amount_in_stock}, {product.product.owner_id}")

   except Exception as e:
        print(f"Error occurred:{e}")
                

def add_product_to_catalog(user_id, product_detail):
    try:
        user=User.get(User.user_id==user_id)
        #create a new product object with the provided details
        new_product=Product.create(
           name=product_detail['name'],
           description=product_detail['description'],
           price=product_detail['price'],
           quantity_description_amount_in_stock=product_detail['quantity_description_amount_in_stock'],
           owner=user
           )
            
        db.commit()
        print("Product added succesfully to the catalog.")
        return new_product
    except User.DoesNotExist:
        print(f"User with Id {user_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None


def update_stock(product_id, new_quantity):
    try:
        product=Product.get(Product.product_id==product_id)
        # update the amount in stock
        product.quantity_description_amount_in_stock=new_quantity
        product.save()
        
        print(f"Stock for product with ID {product_id} updated to {new_quantity}")
        return True
    except Product.DoesNotExist:
        print(f"Product with Id {product_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None


def purchase_product(product_id, buyer_id, quantity):
    try:
        
        buyer=User.get(User.user_id==buyer_id)
        print('r 119 buyer:', buyer.username)
        product=Product.get(Product.product_id==product_id)
        print('r121 product:',product.name)
        
        #2)check_2.1:buyer_id (table Transaction)and owner(table Product) is not the same
        if buyer.user_id != product.product_id:
            print('R 125 buyer.user_id != product.product_id TRUE ')
        else:
            print('The buyer and owner are the same, please give an other buyer')
            return
        #check_2.2:check: the product which is bought is in the table Product(_id)
        if product.product_id ==product_id:
           print('r 131 (argument)product_id exist in colomn product_id of tabel Product ')
        else:
            print('The product_id do not exist in tabel Product, please give an other product_id')
            return
        #check_2.3:if the bought product is in the table Product
        if  quantity > product.quantity_description_amount_in_stock:
            print(f"Sorry, there are only {product.quantity_description_amount_in_stock} items in stock.")
            return
        # If there is enough stock, proceed with the purchase
        # Deduct the quantity from the available stock
        
        product.quantity_description_amount_in_stock -= quantity
        product.save()  

        # Create a new transaction record
        Transaction.create(buyer_id=buyer_id, product_id=product_id, quantity_bought=quantity)
        print(f"Successfully purchased {quantity} {product.name}(s)!")

    except Product.DoesNotExist:
        print(f"Product with Id {product_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None


def remove_product(product_id):
    try:
        product=Product.get(Product.product_id==product_id)
        product_delete=product.delete_instance()
        print(f"Product with Id {product_id} has been removed")

        return product_delete
    except Product.DoesNotExist:
        print(f"Product with Id {product_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None

if __name__ == "__main__":
   product_id=1
   buyer_id=2
   quantity=1
   purchase_product(product_id, buyer_id, quantity)
   
  