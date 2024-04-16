In this ReadMe you can read the following parts:
part 1: Description of the assignment: Betsy Webshop
part 2: the test set of main.py 

Part 1  Description of the assignment: Betsy Webshop

Subjects of this assignment:

Writing functions and function arguments;
SQL joins;
Database modelling;

It is time to put all your SQL knowledge to the test. You will design a database for a fictional web marketplace called Betsy. 
Betsy is a site where people can sell homemade goods. This assignment will test your skills in modelling data as well as using the peewee ORM. 
The requirements for this assignment can be split into 2 parts: Modelling and Querying.

Modelling:
Define your models and initialize the database in models.py
A key part of the Betsy webshop is the database. At its core are the users and the products they offer:

1)A user has a name, address data, and billing information.
2)Each user must be able to own a number of products.
3)The products must have a name, a description, a price per unit, and a quantity describing the amount in stock.
4)The price should be stored in a safe way; rounding errors should be impossible.
5)The tags should not be duplicated.
6)We want to be able to track the purchases made on the marketplace, therefore a transaction model must exist
7)You can assume that only users can purchase goods
8)The transaction model must link a buyer with a purchased product and a quantity of purchased items

Querying:

In order to manage the database, the webshop must have a number of querying utlities. The scaffolding for the utilities can be found in main.py Extend the methods with the relevant functionality.

In this first iteration of the database we want to be able to:
1)Search for products based on a term. Searching for 'sweater' should yield all products that have the word 'sweater' in the name. This search should be case-insensitive
2)View the products of a given user.
3)View all products for a given tag.
4)Add a product to a user.
5)Remove a product from a user.
6)Update the stock quantity of a product.
7)Handle a purchase between a buyer and a seller for a given product

Test data:
To test if your database and queries are working we want to be able to populate the database with data quickly. 
Add a populate_test_database function that fills the database with example data that works with your queries

PART 2:the test set of main.py 

test items for functions:
1)def list_user_products(user_id):
1.1)Test line for where user_id does exist in the model User:user_id(1), so the invoke statement will be: list_user_products(1)
1.2)Test line for where user_id does NOT exist in the model User:user_id(4) so the invoke statement will be: list_user_products(4)

2) def add_product_to_catalog(user_id, product_detail):
2.1 Testset for where user_id exist and also there is product_detail. 
The invoke statements will be :
user_id=1
   product_detail={
    'name':'socks',
    'description':'red socks',
    'price':1.89,
    'quantity_description_amount_in_stock':10
   }
   add_product_to_catalog(user_id, product_detail)
   The expected result is:Product added succesfully to the catalog.
2.2 Test line for where user_id does NOT exist in the model User:user_id(4) so the invoke statement will be: 
user_id=4
   product_detail={
    'name':'socks',
    'description':'red socks',
    'price':1.89,
    'quantity_description_amount_in_stock':10
   }
   add_product_to_catalog(user_id, product_detail)
   The expected result is:User with Id 4 does not exist

2.3:The testset for the function:remove_product(product_id):,assumption there is product_id=5 
like this:table Product looks like this:
product_id, name,   description,   price, amount_in_stock, owner
1         , sweater, red, sweater, 24,99, 2              ,1     (John)  
2         , trouser, red, trouser, 15,50, 5              ,3     (Helen)
3         , bike,  , blue, bike,   50,80, 1              ,2     (David)
4         , blazer , red,blazer,   14.99, 2              ,1     (John)
5         , socks  , red,socks,     1.89, 10             ,1     (John)

2.3.1 use the following statements to remove product_id=5:
product_id=5
remove_product(product_id)
the result will be:Product with Id 5 has been removed
 2.3.2 use the following statement to remove product which do not exist:
product_id=6 
invoke function: remove_product(product_id)

the result will be:Product with Id 6 does not exist

2.4: Testset for the function:update_stock(product_id, new_quantity):
2.4.1. update
product_id=5
new_quantity=4
update_stock(product_id, new_quantity)

2.5 The testset for the function:search(term):
search("sweater")
result for example:
Products containing 'sweater':
ID:1, Name:sweater,Description:red, sweater,Price:24.99,Stock:2
ID:4, Name:Sweater,Description:blue, sweater,Price:23.99,Stock:7

save date in github:13 april 2024 18.23 u

2.6 The testset for function:list_products_per_tag(tag_id):
 tag_id=4
   list_products_per_tag(tag_id)

2.7 The testset for function:purchase_product(product_id, buyer_id, quantity)
The analyse is:
1)needed are three tables with rows. Table: User, Product and Transaction. The tables with rows will display here under with the rows copy from the DB brouwer for SQlite.
2)check_2.1:buyer_id (table Transaction)and owner(table Product) is not the same
check_2.2:check: the product which is bought is in the table Product(_id)
check_2.3:if the bought product is in the table Product, check if there is enough (work further out this section)
3)if there is enough items of the asked product so update the amount of stock in table Product
4)add a row in the table Transaction

tests
product_id=1
   buyer_id=2
   quantity=1
   purchase_product(product_id, buyer_id, quantity)
   


