import time
for c in range (1,4,1): # this for loop is for printing it three times
 for i in range(1, 6, 1): # first for loop  to print "*"
   
    for j in range(i):  # Secound  for loop for space  
        time.sleep(0.005)
        print(' ', end=' ')
    time.sleep(0.005)
    print('*')

 for a in range(4, 0, -1): # first for loop  to print "*"
    
    for b in range (a):   # Secound  for loop for space 
     time.sleep(0.005)  
     print (" ",end=" ") 
     time.sleep(0.005)

    print("*")
 