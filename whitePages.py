print ("WELCOME!")# Print the message


enter = raw_input("Press ENTER to continue... ") # set the variable named enter to get input from the user

if enter == "" : # set how to response when the enter variable gets nothing for the input
    filename = raw_input("Set the file name. >> ") # create a filename variable that gets the input from the user

    with open(filename, 'w') as p: # open the file that user had created above in writing mode
        print ("\nOkay, so your file name is <" + filename + ">.\n\nNow, you're going to type 3 people's name, birthday, and phone number.") # print the message

        print ("\n<First Person's Info>") # print the message
        name = raw_input("Name: ") # create name variable as the input from the user
        p.write(name + "\n") # write name in the text file
        bday = raw_input("Birthday: ") # craete bday variable as the input from the user
        p.write(bday + "\n") # write bday in the text file
        pNumber = raw_input("Phone Number:") # create pNumber variable as the input from the user
        p.write(pNumber + "\n\n") # write pNumber in the text file


        print ("\n<Second Person's Info>") # print the message
        name = raw_input("Name: ") # create name variable as the input from the user
        p.write(name + "\n") # write name in the text file
        bday = raw_input("Birthday: ") # create bday variable as the input from the user
        p.write(bday + "\n")  # write bday in the text file
        pNumber = raw_input("Phone Number:") # create pNumber variable as the input from the user
        p.write(pNumber + "\n\n") # write pNumber in the text file

        print ("\n<Third Person's Info>") # print the message
        name = raw_input("Name: ") # create name variable as the input from the user
        p.write(name + "\n")  # write name in the text file
        bday = raw_input("Birthday: ") # create bday variable as the input from the user
        p.write(bday + "\n") # write bday in the text file
        pNumber = raw_input("Phone Number:") # create pNumber variable as the input from the user
        p.write(pNumber + "\n\n") # write pNumber in the text file


        print ("\nYour file <" + filename + "> is saved. Thank you!") # print the message
        p.close() # close the file
