log_file = open("um-server-01.txt") # this is connecting the file for the function and setting it to log_file it opens the file


def sales_reports(log_file): # this is the same as making a function
    for line in log_file:  # this loops trough the log file that is set the the function
        line = line.rstrip() #This breaks down the lines in the file that is set in the function and sets them to a variable of line
        day = line[0:3] #this looks for the first 3 charaters in the line from line 6 and sets them to the variable of day, they are looking for the index of 0 through the index of 3
        if day == "Mon": # This looks to see if the the day that is indidated in line 7 is mon
            print(line) #if Line 8 is true then it will print the Line indicated in line 6


sales_reports(log_file) #this calls the function for log_file that was made in line 1

