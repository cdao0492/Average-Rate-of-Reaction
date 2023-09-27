#The function allows user to input their data points and store inside a list
def data_point(data_num):
    
    #If there is no number of data points indicated, the program terminates
    if data_num == 0:
        print(">>>NO DATA POINTS! PROGRAM ENDED<<<")
        exit()
     
    #If the user only input one data point, the program terminates
    if data_num == 1:
        print(">>>There should be more than 1 data point! Try again. <<<")
        exit()
        
    for i in range(data_num):
        print(">>>Please input data point " + str(i+1))
        time_val = float(input("Time (in seconds): "))
        concentration_val = float(input("Concentration of product (in M): "))
        #This list will store a data point
        coordinate = []
    #Using append method to create a group of one data point
        coordinate.append(time_val)
        coordinate.append(concentration_val)
    #Using insert method to add the coordinate to the data list
        data_list.insert(i,coordinate)
        data_list.sort()
        print("Current data_table: " + str(data_list))
        print()

#This function allows the program to store the index value of time and concentration
#the user want to know the average rate of reaction
def time_period(num): 
    
    #Declaring the global variable start and end to store the time period
    global start, end, index_1, index_2
    global list_id1, list_id2, time_list
    
    #If there is no time period indicated, the program terminates
    if abs(num) == 0:
        print(">>>No time periods! Program ended<<<")
        exit()
    
    #Create a list that only contains the time value to simplify the program
    time_list = []
    for i in range(len(data_list)):
        time_list.append(data_list[i][0])
        time_list.sort()
    # The list represents the possible time value that the user can input
    print (">>>Data table: " + str(data_list))
    print(">>>Range of time: " + str(time_list))
    print()
        
    #Create a list that contains the index number of the element matching
    # with the starting and ending value
    list_id1 = []
    list_id2 = []
        
    #The program repeatedly ask the user to input the starting and ending 
    #time corresponding to the number of time period they want to calculate
    for i in range(abs(num)):
        print(">>>Please input time period " + str(i+1))
        start = float(input("Starting time: "))
        #The for loop statement determine whether the inputted value matches
        #with the data list
        for i in range(len(time_list)):
        #While loop and count method to continuously ask the user to input 
        #the valid time value
            while time_list.count(start) == 0:
                print("Starting time is out of range! Try again.")
                start = float(input("Starting time: "))
            if start == time_list[i]:
                index_1 = time_list.index(start)
                #Using append method to save the index value of the starting
                #time
                list_id1.append(index_1)
       
        end = float(input("Ending time: "))
        for i in range(len(time_list)):
            #While loop and count method to continuously ask the user to input 
            #the valid time value
            while time_list.count(end) == 0:
                print("Ending time is out of range! Try again.")
                end = float(input("Ending time: "))
            #While loop to remind the user they cannot input the ending time
            #equal to starting time
            while end == start:
                print("Ending time cannot be the same as starting time! Try again. ")
                end = float(input("Ending time: "))
            if end == time_list[i]:
                index_2 = time_list.index(end)
                #Using append method to save the index value of the ending
                #time
                list_id2.append(index_2)
        print()

#The function will calculate the average rate of reaction by retrieve information
#from the data_list
def average_rate(num):
    for i in range(abs(num)):
        #The concentration value will be accessed from the data_list 
        #lists that store the corresponding index values of starting and
        #ending time
        initial_c = data_list[list_id1[i]][1]
        final_c = data_list [list_id2[i]][1]
        diff_concentration = final_c - initial_c
        
        #The time period will be accessed from the time_list using lists
        #that store the corresponding index values of starting and ending time
        end_t = data_list[list_id2[i]][0]
        start_t = data_list[list_id1[i]][0]
        diff_time = end_t - start_t
        #The average rate is difference in concentration over difference in time
        #The rate must be positive so abs() function
        rate = abs(diff_concentration/diff_time)
        print(str(i+1) + ". THE AVERAGE RATE OF REACTION BETWEEN " + str(start_t) +"s " + "AND " + str(end_t)  + "s IS: " + str(rate) + " M/s")
        print()

#Program
print(">>>>>WELCOME TO THE AVERAGE RATE OF REACTION SIMULATION<<<<<")
print()

#This asks user  how many data points they will provide
data_num = int(input(">>>How many data points are there? "))
print()

#This list will store all the data points the user provided
data_list = []
#This allows the user to input and store their information into the data_list
data_point(data_num)

#This asks user how many time periods they want to know the rate of reaction
period_num = int(input("How many time periods you want to calculate? "))
#This repeatedly asks the user to input the time range where they want to calculate
#the rate of reaction
time_period(period_num)
print ()

#This allows the program to calculate the average rate of reaction
average_rate(period_num)


