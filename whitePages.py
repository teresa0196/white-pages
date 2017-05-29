print ("Welcome! ") # Print the message


enter = raw_input("Press ENTER to continue ")

if enter == "" :
    filename = raw_input("Set the filename. >>")

    with open(filename, 'w') as p:
        print "Now, you're going to type 3 people's name, birthday, and phone number."

        print ("<First Person's Info>")
        line1 = raw_input("Name: ")
        p.write(line1)
        p.write("\n")
        line2 = raw_input("Birthday: ")
        p.write(line2)
        f.write("\n")
        line3 = raw_input("Phone Number:")
        p.write(line3)
        p.write("\n\n")

        print ("\n<Second Person's Info>")
        line1 = raw_input("Name: ")
        p.write(line1)
        p.write("\n")
        line2 = raw_input("Birthday: ")
        p.write(line2)
        p.write("\n")
        line3 = raw_input("Phone Number:")
        p.write(line3)
        p.write("\n\n")

        print ("\n<Third Person's Info>")
        line1 = raw_input("Name: ")
        p.write(line1)
        p.write("\n")
        line2 = raw_input("Birthday: ")
        p.write(line2)
        p.write("\n")
        line3 = raw_input("Phone Number:")
        p.write(line3)
        p.write("\n\n")

        print "\nThe file is saved. Bye!"
        p.close()
