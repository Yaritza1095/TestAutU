#Comparison operators
print(1<1)
print(1>1)
print(1<=1)
print(1>=1)
print(1==1)
print(1!=1)

#Control structures if, elif, else
"""
 see != Basically, what this statement says is that any name that is not “Mariah” should print out, "You're not Mariah!".

Just by looking at those 2 lines of code and that statement, it would stand to reason that if I typed “Yaritza”, that the "You're not Mariah!" statement should print.


What actually happens is that once the condition is met, none of the other conditions matter.

"""
name = input("What is your name?")
if name == "Yaritza":
    print("Hello. nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello you are a great person")
#elif name != "Mariah": see != above
    #print("You are not Mariah!")
elif name == "Kingston":
    print("Hi, {}, let's have lunch sooon!".format(name))
else:
    print("Have a nice day")
