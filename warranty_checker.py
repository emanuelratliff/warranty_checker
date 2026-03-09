from datetime import date 
from dateutil.relativedelta import relativedelta 

answer = ""
new_m = ""
new_y = ""

while True:
    serial_number = input("Please enter serial number: ")
    while len(serial_number) == 0:
        print("Please input the correct serial number")
        serial_number = input("Please enter serial number: ")
    # The two foward slashes are used to determine if the scanner is using a specific code
    # I allow the inputs of a specified scanner code, direct scanning with carriage return, or manual input
    # If the string contains the two forward slashes, it is sliced from the beginning and end
    if "\\" in serial_number and "311" == serial_number[1:4]:
        print("The serial number is: " + serial_number[1:-1])
        # This code slices to string to get the year and month
        test = serial_number[8:-5]
        new_y = int("20" + test[:-2])
        new_m = int(test[2:])
    if "\\" not in serial_number and "311" == serial_number[:3]:
        print("The serial number is: " + serial_number)
        test = serial_number[7:-4]
        new_y = int("20" + test[:-2])
        new_m = int(test[2:])
            
    # This function takes the date and month and addes uses a date time object to count ahead based on warranty experiation.     
    def add_years(month, year, years_to_add):
        orig_date = date(year, month, 1)
        new_date = orig_date + relativedelta(years=years_to_add)
        return new_date
    # Years to add is the constant since the mobius batteries have a four year contract
    month = new_m
    year = new_y
    years_to_add = 4

    new_date = add_years(month, year, years_to_add)
    new_date_str = str(new_date)[:-3]

    if new_date < date.today():
        print("Warranty Year: " + str(new_y))
        print("Warranty Month: " + str(new_m))
        print("Warranty End Date: " + new_date_str)
        print("Warranty Status: Expired")
    else:
        print("Warranty Year: " + str(new_y))
        print("Warranty Month: " + str(new_m))
        print("Warranty End Date: " + new_date_str)
        print("Warranty Status: Active")
        
    answer = input("Quit? enter y or n: ")
    while answer != "y" or answer != "n":
        if answer == "y" or answer == "n":
                break
        else:
            print("Please choose y or n")
        answer = input("Quit? enter y or n: ")
    if answer == "y":
        break
    if answer == "n":
        pass


    


   


