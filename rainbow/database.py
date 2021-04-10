from flask import Flask
import pymysql
app = Flask(__name__)

#this is to refresh everything in a database, all data will be lost and a default admin account will be created.

#connect('host', 'username', 'password', 'database_name')
db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')

#cursor executes sql commands
cursor = db.cursor()

try:
	cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
	cursor.execute("DROP TABLE IF EXISTS Account")
	cursor.execute("DROP TABLE IF EXISTS categories")
	cursor.execute("DROP TABLE IF EXISTS products")
	cursor.execute("DROP TABLE IF EXISTS cart")
	cursor.execute("DROP TABLE IF EXISTS Order")
	cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
finally:
	account_table = """CREATE TABLE Account (
	AccountID int AUTO_INCREMENT,
	Type enum ('User', 'Admin'),
	Name varchar(20),
	Email varchar(255),
	Password varchar(30),
	PRIMARY KEY (AccountID))"""
	cursor.execute(account_table)
	# create admin account for accessing to the admin page
	cursor.execute("INSERT INTO Account (Type, Name, Email, Password) VALUES ('Admin', 'Admin1', 'admin1@gmail.com', '12345678')")

	category_table = """CREATE TABLE categories (
	id int AUTO_INCREMENT,
	category varchar(20),
	PRIMARY KEY (id))"""
	cursor.execute(category_table)
	#create existing categories
	cursor.execute("INSERT INTO categories (category) VALUES ('T-Shirts'), ('Shoes'), ('Trackpants'), ('Socks'), ('Watches')")

	product_table = """CREATE TABLE products (
	ProductID int AUTO_INCREMENT,
	CategoryID int,
	ProductName varchar(50),
	ProductDesc text,
	Image longblob,
	Quantity int,
	Price int,
	PRIMARY KEY (ProductID),
	FOREIGN KEY (CategoryID) REFERENCES categories(id),
	"""
	cursor.execute(product_table)

	cart_table = """CREATE TABLE cart (
	CartID int AUTO_INCREMENT,
	ProductID int,
	AccountID int,
	PRIMARY KEY (CartID),
	FOREIGN KEY (AccountID) REFERENCES Account(AccountID),
	FOREIGN KEY (ProductID) REFERENCES products(ProductID))
	"""
	cursor.execute(cart_table)

	order_table = """CREATE TABLE OrderDesc (
	OrderID int AUTO_INCREMENT,
	ProductID int,
	AccountID int,
	OrderDate datetime,
	PRIMARY KEY (OrderID),
	FOREIGN KEY (ProductID) REFERENCES products(ProductID),
	FOREIGN KEY (AccountID) REFERENCES Account(AccountID))
	"""
	cursor.execute(order_table)

db.close()