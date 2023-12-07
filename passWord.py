# A SIMPLE SECURITY APP

def vital():
    print("""	SECURITY APP
Before Setting or Modifying your Password. 
Firstly, Input all the Essentials""")

    print("\nWhat is your Name?")
    name = input('--> ')

    print("\nSet your Password.")
    password = input('--> ')

    print("\nSet your Hints, Should in case you forget your Password.")
    hint = input('--> ')

    print("""\nChoose!
1. Access Device
2. Modify Password""")

    want = input('--> ')
    while True:
        if want == '1':
            print("\n	Access Device")
            print("What is your name")
            username = input('--> ')
            if username != name:
                continue
            print(f"""\nHello {name},
What is your Password?   (Hint --> {hint})""")
            userpassword = input('--> ')
            if userpassword != password:
                continue
            print("ACCESS GRANTED")
            break

        if want == '2':
            print("""\n    Modify Password
Input your old Password""")
            presentpass = input('--> ')
            if presentpass != password:
                continue
            print("\nEnter your new Password")
            newpass = input('--> ')
            print("Re-Enter your new Password to complete the setup")
            reinput = input('--> ')
            if reinput != newpass:
                continue
            print("\nSETUP SUCCESSFULLY COMPLETED.")
            break


vital()
