#Ostad Live test-1 by Hasan Mahmud
#Module 1-5; 19 september 2024

#Start coding

def discount(time, ticketprice):
    if (time < 1700):
        discount = (ticketprice*10)/100
        discounted_price = ticketprice - discount
        print("Ticket price:", ticketprice)
        print("Discount: ", discount)
        print("Discounted price: ", discounted_price)
    else:
        print("Ticket price:", ticketprice, "BDT")
        print("Discount: 0.00 BDT ")
        print("Discounted price: ", ticketprice, "BDT")
        
        
try:
    age = int(input("Age: "))
    showtime = int(input("Showtime (HHMM):"))
    if (0<= age <= 10):
        ticketprice = 300
    elif (11<= age <=25):
        ticketprice = 500
    elif (26<= age <=60):
        ticketprice = 800
    elif (age > 60):
        ticketprice = 400
    else:
        print("Invalid input. Age must be a positive integer.")
    discount(showtime, ticketprice)
except Exception as e:
    print(e)


