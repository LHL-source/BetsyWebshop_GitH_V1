from peewee import *
from models import *
import os

#functie delete database 
def delete_database():
   db.close() 
   cwd=os.getcwd()
   database_path=os.path.join(cwd,"BetsyWebshop.db")
   if os.path.exists(database_path):
      os.remove(database_path)

#hieronder maak een functie die de database vult met data
def populate_database():
    db.connect()
    db.create_tables([Address,User,Product,Tag,TagProduct,Transaction])
    
    address_list=[
                 ["Escamplaan","20","Den Haag"],
                 ["Kalvermarkt","4","Den Haag"],
                 ["Gouverneurlaan","104","Den Haag"],
                 ]
    for i in address_list:
        Address.create(street=i[0], house_nr=i[1],city=i[2] )    

    #add to model User data 
    john_address=Address.get(Address.address_id==2)
    david_address=Address.get(Address.address_id==3)
    helen_address=Address.get(Address.address_id==1)

    user_list=[
              ["John",john_address,"NL01INGB1234567"],
              ["David",david_address,"NL02ABNA2345678"],
              ["Helen",helen_address,"NL03RABO345678"],
              ]
    for i in user_list:
        User.create(username=i[0],user_address_id=i[1],billing_info=i[2])
   
   #add to model Product data
    john = User.get(User.user_id == 1)
    helen= User.get(User.user_id==3)
    david=User.get(User.user_id==2)
    product_list=[
                 ["sweater","red, sweater",24.99,2,john],
                 ["trouser","red, trouser",15.50,5,helen],
                 ["bike","blue, bike", 50.80,1,david],
                 ["Blazer","red, blazer",14.99,2,john],
     
           
                ]
    for i in product_list:
        Product.create(name=i[0],description=i[1],price=i[2],quantity_description_amount_in_stock=i[3],owner=i[4])
    
 

    #add to model Tag data
    tag_list=[
                 ["red"],
                 ["blue",],
                 ["sweater"],
                 ["trouser"],
                 ["bike"],
                 ]
    for i in tag_list:
        Tag.create(name=i[0])    

    #model TagProduct in a table with rows and data 
    red_tag=Tag.get(Tag.tag_id==1)
    blue_tag=Tag.get(Tag.tag_id==2)
    sweater_tag=Tag.get(Tag.tag_id==3)
    trouser_tag=Tag.get(Tag.tag_id==4)
    bike_tag=Tag.get(Tag.tag_id==5)

    #create the:sweater_product
    sweater_product=Product.get(Product.product_id==1)
    trouser_product=Product.get(Product.product_id==2)
    bike_product=Product.get(Product.product_id==3)

    #create the tagproduct_list:
    tagproduct_list=[
                [red_tag,sweater_product],
                [red_tag,trouser_product],
                [red_tag,bike_product],

                [blue_tag,sweater_product],
                [blue_tag,trouser_product],
                [blue_tag,bike_product],

                [sweater_tag,sweater_product],
                [sweater_tag,trouser_product],
                [sweater_tag,bike_product],

                [trouser_tag,sweater_product],
                [trouser_tag,trouser_product],
                [trouser_tag,bike_product],

                [bike_tag,sweater_product],
                [bike_tag,trouser_product],
                [bike_tag,bike_product],

                ]

    for i in tagproduct_list:
        TagProduct.create(tag_id=i[0],product_id=i[1])

# model Transaction in a table with rows and data 
    john_buyer_transact = User.get(User.user_id == 1)
    helen_buyer_transact= User.get(User.user_id==3)
    david__buyer_transact=User.get(User.user_id==2)

    #create the:sweater_product
    sweater_product=Product.get(Product.product_id==1)
    trouser_product=Product.get(Product.product_id==2)
    bike_product=Product.get(Product.product_id==3)

    transaction_list=[
               [helen_buyer_transact,sweater_product,2]
               ]

    for i in transaction_list:
        Transaction.create(buyer_id=i[0],product_id=i[1],quantity_bought=i[2])
    db.close()
if __name__ == "__main__":
   #delete_database()
   #populate_database()
   pass

