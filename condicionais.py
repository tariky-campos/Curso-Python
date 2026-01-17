n1 = float(input("Input a first number: "))
n2 = float(input("Input a second number: "))

average = (n1 + n2) /2

if(average > 7): 
    print("True")
elif(average>5.5):
    print("Recuperation...")
else:
    print("False")

print("Your average is: {}".format(average))