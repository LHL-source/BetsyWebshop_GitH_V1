# Models go here
from peewee import *

db = SqliteDatabase('BetsyWebshop.db')
class BaseModel(Model):
    class Meta:
        database=db


#Adress:adress_id, name
class Address(BaseModel):
    address_id=AutoField()
    street=CharField(max_length=40)
    house_nr=CharField(max_length=5)
    city=CharField(max_length=30)
   

#Customer table:id, name, id_adress,id_seller, billing, number_of_products
class User(BaseModel):
    user_id=AutoField()
    username=CharField(max_length=30, null=False, unique=True)
    user_address_id= ForeignKeyField(Address)
    billing_info=CharField(max_length=50)
    


#product:id, name, description, price_per_unit,quantity_discription, amount_in_stock

class Product(BaseModel):
    product_id=AutoField()
    name=CharField(max_length=20, null=False, index=True)
    description=CharField(max_length=50, null=False, index=True)
    price=DecimalField(decimal_places=2,
        auto_round=True,
        default=0,
        constraints=[Check("price < 1000000")],
        )
    quantity_description_amount_in_stock=IntegerField()
    owner=ForeignKeyField(User)


#Transaction:transaction_id, customer_id,Seller_id, (id_product: c.verlaan vraagt zich af of dit nodig is), quantity_of_purchase_item, price_per??
class Transaction(BaseModel):
    transaction_id=AutoField()
    buyer_id=ForeignKeyField(User, backref="transaction")
    product_id=ForeignKeyField(Product,backref="products") 
    quantity_bought=IntegerField(default=0, constraints=[Check("quantity_bought < 1000")])
    
#Tag:tag_id, name
class Tag(BaseModel):
    tag_id=AutoField()
    name=CharField(max_length=20, null=False, unique=True)

    class Meta:
        constraints=[SQL('UNIQUE(name)')]
    

#TagProduct:TagProduct_id, product_id, tag_id
class TagProduct(BaseModel):
    tagproduct_id=AutoField()
    tag=ForeignKeyField(Tag, backref="tagproduct")
    product=ForeignKeyField(Product, backref="tagproduct")

