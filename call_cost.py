"""
In this app we will read cost per second of call.
Read start of call in fomrmat HH:MM:SS [ 00:00:00 - 23:59:59 ].
Read end of the call in same format [ 00:00:00 - 23:59:59 ].
and output length of the call in seconds and the cost.
"""

# Read tarif cost per second
cena=int(input("cena"))
print(cena)
# Read call start
start=input("start")
end=input("end")
start2=start.split(":")
end2 = end.split(":")

# check if we have correct format 
# just check that we have 2 semicolons
# If wrong format print error message and exit the program

# Read call end

# check format agian

# compute difference
seconds_start = int(start2[2])
seconds_start = seconds_start + 60*int(start2[1])
seconds_start = seconds_start + 3600 * int(start2[0])

seconds_end = int(end2[2])
seconds_end = seconds_end + 60*int(end2[1])
seconds_end = seconds_end + 3600 * int(end2[0])

print("Hovor trval " + str(seconds_end - seconds_start) + " sekund")

print("Hovor stal " + str(seconds_end * cena - seconds_start * cena) + " CZK")



# print length in seconds and the cost

