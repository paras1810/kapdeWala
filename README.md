# kapdeWala
Excel will be named as Year named
Inside excel multiple sheets are there with month name 
Values are classified as:
    Purchase: Added in Purchase 
    Sale: Added in Sale 
    PurchaseReturn: Deleted from Purchase 
    SaleReturn: Deleted From Sale 
Excel need to updated from flask Application.

Input via web form:
    Comma-separated dates
Corresponding values for:
    Purchase
    Sale
    PurchaseReturn
    SaleReturn
For each row (date):
    Compute:
        Total Purchase = Purchase - PurchaseReturn
        Total Sale = Sale - SaleReturn
Output:
    Append to (or create) an Excel file named by the year (e.g. 2025.xlsx)
    With columns: Date, Total Purchase, Total Sale
    If file exists → append
    If not → create new

Buyer_name
ColorPurchase(Comma Separated)
ColorPurchaseReturn(Comma Separated)
Purchase(Comma Separated)
PurchaseReturn(Comma Separated)
TotalPurchase
TotalPurchaseReturn
Date 

Customer_name
ColorSale(Comma Separated)
ColorSaleReturn(Comma Separated)
Sale(Comma Separated)
SaleReturn(Comma Separated)
TotalSale
TotalSaleReturn
Date


Daily Purchases
DailySales
TotalLeft
