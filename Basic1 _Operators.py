print("This Program Takes an Input and uses it")
print("Please Input Two Numbers")

#Taking Inputs
u_In1= float(input('Please Insert Integer One    '))
u_In2= int(input('Please Insert Integer Two    '))

#Adding Inputs
sum= (u_In1 + u_In2)
print("The Summation Is: ", sum)

#Subtracting from the Large One
if u_In1>u_In2:
    subtract= u_In1-u_In2
    print("The Subtraction is: ", subtract)
elif u_In1<u_In2:
    sub2=u_In2-u_In1
    print("The Subtraction is: ", sub2)
else:
    print("Invalid Input")

#Multiplication
Multipl=u_In1*u_In2
print('The Multiplication Is', Multipl)

#Lets See the Type of the Outputs
print("The type of the summation is: ", type(sum))
print("The type of Subtraction is: ", type(sub2))
print("The Multiplication Is: ", type(Multipl))

#Lets Convert The Types if it is float
if type(sum)==float:
    converted_sum=int(sum)
    print("The Converted Sum value Is: ",converted_sum)

if type(sub2)==float:
    converted_sub=int(sub2)
    print("The Coverted Subtraction is: ", converted_sub)

if type(Multipl)==float:
    converted_Multipl=int(Multipl)
    print("The Converted Multiplcation value Is: ", converted_Multipl)

        

 

