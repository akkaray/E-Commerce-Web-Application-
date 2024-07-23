# E-Commerce Application for Purchasing Clothing
 ## Project Overview:
	
This project is an e-commerce application designed to facilitate the purchase of clothing. It allows users to search for clothing items, add them to a cart, and proceed to checkout. Additionally, employees have the ability to manage the product inventory by adding or deleting products and adjusting prices.
	
## User Types-

## Customer
### Use Cases:

**Search for Clothing:** Customers can browse through the available clothing items by applying various filters and search criteria.

**Add to Cart:** Customers can add desired clothing items to their shopping cart.

**Checkout:** Customers can proceed to checkout to complete their purchase.

 ### Customer Credentials:

**Username:** abc@gmail.com

**Password:** 123

**Type:** customer

## Employee
### Use Cases:

**Add or Delete a Product:** Employees can manage the product inventory by adding new products or removing existing ones.

**Change the Price for Clothing:** Employees can update the prices of clothing items.

### Employee Credentials:

**Username:** jim@sur.com

**Password:** 1234

**Type:** employee

## Relational Schema
The relational schema of the database is illustrated in the attached image (SchemaLatest.png). The database consists of the following tables:

### Users
id: Primary Key
lname: Last Name
fname: First Name
email: Email
pw: Password
gender: Gender
age: Age
type: User Type (customer or employee)
### Transactions
TId: Primary Key
Amount: Transaction Amount
Tdate: Transaction Date
Tstatus: Transaction Status
Paymenttype: Payment Type
CID: Customer ID (Foreign Key)
### Line_Items
Line_ItemId: Primary Key
Quantity: Quantity of Items
TId: Transaction ID (Foreign Key)
ProductId: Product ID (Foreign Key)
### Products
ProductId: Primary Key
PType: Product Type
PColor: Product Color
PSize: Product Size
PBrand: Product Brand
PPrice: Product Price
PName: Product Name
img: Product Image
 

![RelationalSchema](Documentation/SchemaLatest.png)

# SQL Queries
Below are some SQL queries used in the application:

### Transaction.py
**sql**

SELECT * FROM AY_Transactions WHERE Tstatus=%s AND CID=%s;

This query retrieves all transactions for a specific customer with a given status. The %s placeholders are for the Tstatus (transaction status) and CID (customer ID).

### Line_Items.py
**sql**

SELECT * FROM AY_Line_items 
LEFT JOIN AY_Products ON AY_Products.ProductId=AY_Line_items.ProductId 
WHERE TId=%s;

This query retrieves all line items for a specific transaction ID, joining the Line_Items and Products tables on the ProductId.

### Note
Please note that the application login functionality will not work as the university access has expired.

### Conclusion
This project provides a comprehensive e-commerce platform for purchasing clothing, with distinct functionalities for customers and employees. The relational schema and SQL queries demonstrate the backend structure and data retrieval processes essential for the application's operation.










