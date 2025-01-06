#TASK 3
#5)Get the height from user.
#if given height is less than 150, output will be small.
#if given height is greater than or equal 150 and height less than 165, output will be Average Height.
#if given height is greater than or equal 165 and height less than 195, output will be  Taller.
#otherwise output will be Abnormal height.




height=int(input("Enter the value:"))
  if(height<150):
     print("Output will be small")
  elif(height>=150 and height<165):
     print("Output will be average height")
   elif(height>=165 and height<195):
     print("Output will be Taller")
   else: 
     print("Output will be abnormal height")