# PAYMENT FUNCTION
def Payment():

    ph = str(input("Phone Number: "))
    global i
    f = 0

    for n in range(0, i):
        if ph == phno[n]:

            # checks if payment is
            # not already done
            if p[n] == 0:
                f = 1
                print(" Payment")
                print(" --------------------------------")
                print(" MODE OF PAYMENT")

                print(" 1- Credit/Debit Card")
                print(" 2- Paytm/PhonePe")
                print(" 3- Using UPI")
                print(" 4- Cash")
                x = int(input("-> "))
                print("\n Amount: ", (price[n] * day[n]) + rc[n])
                print("\n		 Pay For DUA RESORTS")
                print(" (y/n)")
                ch = str(input("->"))

                if ch == "y" or ch == "Y":
                    print("\n\n --------------------------------")
                    print("		 Hotel DUA RESORTS")
                    print(" --------------------------------")
                    print("			 Bill")
                    print(" --------------------------------")
                    print(
                        " Name: ",
                        name[n],
                        "\t\n Phone No.: ",
                        phno[n],
                        "\t\n Address: ",
                        add[n],
                        "\t",
                    )
                    print(
                        "\n Check-In: ",
                        checkin[n],
                        "\t\n Check-Out: ",
                        checkout[n],
                        "\t",
                    )
                    print(
                        "\n Room Type: ",
                        room[n],
                        "\t\n Room Charges: ",
                        price[n] * day[n],
                        "\t",
                    )
                    print(" Restaurant Charges: \t", rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ", (price[n] * day[n]) + rc[n], "\t")
                    print(" --------------------------------")
                    print("		 Thank You")
                    print("		 Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)

                    # pops room no. and customer id from list and
                    # later assigns zero at same position
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n, 0)
                    custid.insert(n, 0)

            else:

                for j in range(n + 1, i):
                    if ph == phno[j]:
                        if p[j] == 0:
                            pass

                        else:
                            f = 1
                            print("\n\tPayment has been Made :)\n\n")
    if f == 0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
