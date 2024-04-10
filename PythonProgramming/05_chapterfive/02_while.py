temp = 37
while temp > 32:
    print("The water is not frozen")
    temp -=1
print("The water becomes ice at 32 degrees Fahrenheit")

#Loop control: break

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -=1
    if temp_f==32:
        break

#Loop control: continue
for number in range (1, 11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))

#Loop control: pass
for number in range(1, 11):
    if number == 3:
        pass
    else:
        print("This is the number {}.".format(number))