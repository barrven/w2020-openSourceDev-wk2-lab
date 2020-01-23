# invoice program - will calculate the discount to award to a customer based on the type of the customer and the invoice total

# display program title
print('Invoice Calc Program')
# get user input for the customer type and the invoice total
customerType = input('enter customer type: (r/w)')
invoiceTotal = float(input('Enter the invoice total: '))
# determine the discount based on the customer type
# calc discount for retail customers
# calc discount for default customers
discount = 0
if customerType.lower() == 'r':
    if invoiceTotal > 0 and invoiceTotal < 100:
        discount = 0
    elif invoiceTotal >= 100 and invoiceTotal < 250:
        discount = 0.1
    elif invoiceTotal >= 500:
        discount = 0.25
# calc discount for wholesale customers
elif customerType.lower() == 'w':
    if invoiceTotal > 0 and invoiceTotal < 500:
        discount = 0.4
    elif invoiceTotal >= 500:
        discount = 0.5
# calculate discount amount
discountAmount = round((invoiceTotal*discount), 2)
# calculate the new invoice total
newInvoiceTotal = invoiceTotal - discountAmount

# print the results
