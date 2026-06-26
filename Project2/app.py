# import datetime from datetime module
import datetime 
import csv
# define function add_session(subject, minutes):
def add_session(subject , minutes):
    # get today's date using strftime day/month/year
    date = datetime.now
    # open studysessions.csv in append mode with newline=""
    with open("studysession.csv" , "a" , newline="")as file:
        # create csv writer
        writer = csv.writer(file)
        # write row with subject, minutes, date
        writer.writerow([subject , minutes , date])

# define function show_sessions():
def show_session():
    try:
        # open studysessions.csv in read mode
        with open("studysessions.csv" , "r") as file:
            # create csv reader
            reader = csv.reader(file)
            # skip header
            next(reader)
            # loop through rows
                # print subject, minutes, date nicely
    # except FileNotFoundError:
    except FileNotFoundError:
        # print no sessions yet
        print("no session yet")

# define function get_total_time():
def get_total_time():
    # total = 0
    total = 0
    try:
        # open studysessions.csv in read mode
        with open ("studysessions.csv" , "r") as file:
            # create csv reader
            reader = csv.reader
            # skip header
            next(reader)
            # loop through rows
                # add minutes to total (convert to int)
    # except FileNotFoundError:
    except FileNotFoundError:
        pass
    # return total
        return total
# main program
# while True:
while True:
    print("\n1. Add session")
    print("2. Show all session")
    print("3. Total time session")
    print("4. Quit")
        # 1. Add session
        # 2. Show all sessions
        # 3. Total time studied
        # 4. Quit
    
    # get choice from user
    choice = input("Choose: ")
    # if choice 1:
    if choice  == "1":
        # get subject from user
        subject = input("Enter subject: ")
        # get minutes from user with validation loop and try/except
        # call add_session
        # print added successfully
    
    # elif choice 2:
    elif choice == "2":
        # call show_sessions
        show_session
    
    # elif choice 3:
    elif choice == "3":
        # call get_total_time
        get_total_time
        # print total in hours and minutes
    
    # elif choice 4:
    elif choice == "4":
     print(" goodbye")
    break