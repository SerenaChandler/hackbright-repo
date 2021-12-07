log_file = open("um-server-01.txt")

# creates a function titled saled_reports
def sales_reports(log_file):
# uses a for loop to loop through log_file
    for line in log_file:
        # changes line to be equal to each individual row
        line = line.rstrip()
        #makes day equal to the first 3 indexes of each row
        day = line[0:3]
        # checks if day is equal to a string of "Mon", if it is, it prints the current line
        if day == "Mon":
            print(line)

# calls the fuction, and feeds it log_file as a parameter
sales_reports(log_file)
