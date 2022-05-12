def is_palindrome(user_input):
    rvs_string = user_input[::-1]
    if(rvs_string != user_input):
        palindrome = False
    else:
        palindrome = True
    return palindrome  

def ask_input():
    user_input = str(input("Enter a String: "))
    return_palindrome = is_palindrome(user_input)
    if(return_palindrome):
        print("{}, is a palindrome".format(user_input))
        while True:
            value = input("Do You Want to Try Again? (Y/N):")
            try: 
                if value == "y":
                    ask_input()
                elif value == "n":
                    print("Have a Nice Day!")
                else:
                    raise Exception("System Only Accepts 'Y' or 'N' value. Plese Try Again!")
            except Exception as e:
                    print(e)
            else:
                break
    else:
        print("{}, is a palindrome".format(user_input))
        while True:
            value = input("Do You Want to Try Again? (Y/N):")
            try: 
                if value == "y":
                    ask_input()
                elif value == "n":
                    print("Have a Nice Day!")
                else:
                    raise Exception("System Only Accepts 'Y' or 'N' value. Please Try Again!")
            except Exception as e:
                    print(e)
            else:
                break
ask_input()