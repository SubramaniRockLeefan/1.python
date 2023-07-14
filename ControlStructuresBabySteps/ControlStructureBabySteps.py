print("Welcome To Assignment-1")

num1=int(input("Num1="))
num2=int(input("Num2="))
add=num1+num2
print("add ",add)

BMI=float(input("Enter the BMI Index:"))
if(BMI<18.5):
 print("Underweight")
elif(BMI<=24.9):
 print("Normal Range")
else:
 print("Very OverWeight")