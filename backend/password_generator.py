# import libs 
import random
import string


# create class for charactors 
class characters: 
    chars = int(input())
    # create while that breaks when input done 
    while True: 
        if chars == 'Letters':
            chars += string.ascii_letters
        elif chars == 'Numbers':
            chars += string.digits
        elif chars == 'Specials Characters':
            chars += string.punctuation
        else:
            print('Please input the following!!')
        # place elif inside while 

# create function generator 
    # uses the random class 
    # append that to the a new string 

    
# call  function and print 