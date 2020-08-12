def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    print("Hello User! This Program is made by Mr.Himanshu, please take his permission to access it! \nplease input yes if you take his permission and no if don't take")
    speak("Hello User! This Program is made by Mr.Himanshu, please take his permission to access it! please input yes if you take his permission and no if don't take")
    z= input()
    if z== "yes":
        print("Welcome Next Generation Calculator\nEnter the first number")
        speak("Welcome Next Generation Calculator, Enter the first number")
        num1= int(input())
        print("Enter second number") 
        speak("Enter second number")
        num2= int(input())
        print("Enter + for Addition, - for subtraction, / for division, * for multiplication and % for find remainder")
        speak("Enter plus for Addition, minus for subtraction, divide for division, star for multiplication and % for find remainder")
        y= input()
        if y== "+":
            print(f"Addition be {num1+num2}, have a nice day")
            speak(f"Addition be {num1+num2}, have a nice day")
        elif y== "-":
            print(f"Subtraction be {num1-num2}, have a nice day")
            speak(f"Subtraction be {num1-num2}, have a nice day")
        elif y== "*":
            print(f"Multiplication be {num1*num2}, have a nice day")
            speak(f"Multiplication be {num1*num2}, have a nice day")
        elif y== "/":
            print(f"Division be {float(num1)/float(num2)}, have a nice day")
            speak(f"Division be {float(num1)/float(num2)}, have a nice day")
        elif y== "%":
            print(f"Remainder be {num1%num2}, have a nice day")
            speak(f"Remainder be {num1%num2}, have a nice day")
        else:
            print("This is an invalid input, please try again later")
            speak("This is an invalid input, please try again later")
    elif z== "no":
        print("Please take the permission of Mr. Himanshu and try again! Thank you")
        speak("Please take the permission of Mr. Himanshu and try again! Thank you")
    else:
        print("This is an invalid input, please try again later")
        speak("This is an invalid input, please try again later")
