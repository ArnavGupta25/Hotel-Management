# RECORD FUNCTION
def Record():

    # checks if any record exists or not
    if phno != []:
        print("	 * HOTEL RECORD *\n")
        print(
            "| Name	 | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 |"
        )
        print(
            "----------------------------------------------------------------------------------------------------------------------"
        )

        for n in range(0, i):
            print(
                "|",
                name[n],
                "\t |",
                phno[n],
                "\t|",
                add[n],
                "\t|",
                checkin[n],
                "\t|",
                checkout[n],
                "\t|",
                room[n],
                "\t|",
                price[n],
            )

        print(
            "----------------------------------------------------------------------------------------------------------------------"
        )

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()

    else:
        exit()


# Driver Code
Home()
