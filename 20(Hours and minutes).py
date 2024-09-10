#Convert the given total minutes into HOURS and MINUTES form.
Value=int(input("Enter the number:\n"))
Hours=Value//60
Minutes=Value-(Hours*60)
print('{}Hour(s) {}Minute(s)'.format(Hours,Minutes))

