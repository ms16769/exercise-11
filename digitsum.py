DigitC="00123456" # Constant Value of code
i=0
Const_Sum=0 # Sum of Constant Digit initialize
while i<len(DigitC):
  StoI=DigitC[i]
  StoI=int(StoI) # String to Interger conversion
  Const_Sum=Const_Sum+StoI
  i+=1
print(Const_Sum) # Sum of Constant Digit

UserData=input("Please enter a number: ") # User Data input
i=0
User_Sum=0 # Sum of Constant Digit initialize
while i<len(UserData):
  StoI=UserData[i]
  StoI=int(StoI)
  User_Sum=User_Sum+StoI
  i+=1
print(User_Sum) # Sum of Constant Digit
Diff_C_U=Const_Sum-User_Sum
print("The difference is:", Diff_C_U) # Difference between Constant digit sum and User define sum
