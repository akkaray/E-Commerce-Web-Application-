CREATE TABLE AY_Users
(
  id INT NOT NULL AUTO_INCREMENT,
  lname VARCHAR(50) NOT NULL,
  fname VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  pw VARCHAR(50) NOT NULL,
  gender VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  type VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
)ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

CREATE TABLE AY_Products
(
  ProductID INT NOT NULL AUTO_INCREMENT,
  Ptype VARCHAR(50) NOT NULL,
  PColor VARCHAR(50) NOT NULL,
  PSize INT NOT NULL,
  PBrand VARCHAR(50) NOT NULL,
  PPrice DECIMAL(8,2) NOT NULL,
  PName VARCHAR(50) NOT NULL,
  PRIMARY KEY (ProductID)
)ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

CREATE TABLE AY_Transactions
(
  TransactionID INT NOT NULL AUTO_INCREMENT,
  TransactionType VARCHAR(50) NOT NULL,
  Amount DECIMAL(8,2) NOT NULL,
  Tdate DATE NOT NULL,
  Transaction_status VARCHAR(50) NOT NULL,
  Payment_type VARCHAR(50) NOT NULL,
  PRIMARY KEY (TransactionID),

)ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

CREATE TABLE AY_Line_items
(
  Line_itemId INT NOT NULL AUTO_INCREMENT,
  Quantity INT NOT NULL,
  PRIMARY KEY (Line_itemId),
  
)ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

INSERT INTO AY_Users (fname,lname,email,pw,gender,age,type)
VALUES (Ram,Max,abc@gmail.com,123,M,40,Customer)