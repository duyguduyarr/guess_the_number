#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math


# In[2]:


#Taking inputs
lower = int(input("Enter the lower bound: "))


# In[3]:


upper = int(input("Enter the upper bound: "))


# In[4]:


print("Your range is",[lower,upper])


# In[5]:


x = random.randint(lower,upper)
#Number of chances to guess
guess = round(math.log(upper-lower+1,2))
#From binary search, player should be use the binary search for his/her best
print ("You have",guess,"chances to guess! Please use wiseley.")


# In[6]:


count = 0
while count<guess:
    #increasing count at the beginning prevents restarting loop after count works.
    count += 1 
    users_guess = int(input("Enter your input: "))
    if users_guess==x:
        print("Congratulations! You guessed it",count,"times. The number was",x)
        break
    elif users_guess>x:
        print("You guessed too high! Lower your guess.")
    elif users_guess<x:
        print("You guessed too low! Increase your guess.")
    
if count>=guess:
    print("Your chances of guessing is over. The number was ",x)
 


# In[ ]:





# In[ ]:





# In[ ]:




