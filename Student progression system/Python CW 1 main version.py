Credits_levels =[[120, 0, 0, ], [100, 20, 0], [100, 0, 20], [80, 40, 0], [80, 20, 20], [80, 0, 40], [60, 60, 0],
                [60, 40, 20], [60, 20, 40], [60, 0, 60], [40, 80, 0], [40, 60, 20], [40, 40, 40], [40, 20, 60],
                [40, 0, 80], [20, 100, 0], [20, 80, 20], [20, 60, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100],
                [0, 120, 0], [0, 100, 20], [0, 80, 40], [0, 60, 60], [0, 40, 80], [0, 20, 100], [0, 0, 120]]

Progresion_outcomes = ["Progress", "Progress(module trailer)", "Progress(module trailer)",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Exclude", "Do not progress-module retriever",
                       "do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Exclude", "Exclude",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever", "Exclude", "Exclude",
                       "Exclude"]
combined_list= [("Progress", [120, 0, 0]), ("Progress(module trailer)", [100, 20, 0]),
                 ("Progress(module trailer)", [100, 0, 20]), ("Do not progress-module retriever", [80, 40, 0]),
                 ("Do not progress-module retriever", [80, 20, 20]), ("Do not progress-module retriever", [80, 0, 40]),
                 ("Do not progress-module retriever", [60, 60, 0]), ("Do not progress-module retriever", [60, 40, 20]),
                 ("Do not progress-module retriever", [60, 20, 40]), ("Do not progress-module retriever", [60, 0, 60]),
                 ("Do not progress-module retriever", [40, 80, 0]), ("Do not progress-module retriever", [40, 60, 20]),
                 ("Do not progress-module retriever", [40, 40, 40]), ("Do not progress-module retriever", [40, 20, 60]),
                 ("Exclude", [40, 0, 80]), ("Do not progress-module retriever", [20, 100, 0]),
                 ("do not progress-module retriever", [20, 80, 20]), ("Do not progress-module retriever", [20, 60, 40]),
                 ("Do not progress-module retriever", [20, 40, 60]), ("Exclude", [20, 20, 80]),
                 ("Exclude", [20, 0, 100]), ("Do not progress-module retriever", [0, 120, 0]),
                 ("Do not progress-module retriever", [0, 100, 20]), ("Do not progress-module retriever", [0, 80, 40]),
                 ("Do not progress-module retriever", [0, 60, 60]), ("Exclude", [0, 40, 80]),
                 ("Exclude", [0, 20, 100]), ("Exclude", [0, 0, 120])]



Credits_range=[0,20,40,60,80,100,120]

pro_count=0
mt_count=0
mr_count=0
exc_count=0
total_outcomes=0
 
user_input_pro  = []
user_credit_vol = []
Credit_Vol = []
list_pro = []
list_cv = []
Student_IDs = []
student_rec = {} 
user_ID=""
 
    


def student_code():
    print("You choose student_code")


        
         
    while True :
        try:
            while True:
                try:
                    user_ID=input("Enter your student id: ")
                    PASS = int(input("Please enter your credits at pass: "))
                    if PASS not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                        continue
                    break
                except ValueError:
                    print("Integer required.")
            while True:
                try:
                    DEFER = int(input("Please enter your credits at defer: "))
                    if DEFER not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                        continue
                    break
                except ValueError:
                    print("Integer required.")
            while True:
                try:
                    FAIL = int(input("Please enter your credits at fail: "))
                    if FAIL not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                        continue
                    break
                except ValueError:
                    print("Integer required.")
        except ValueError:
            print("Integer required")
            continue
        
        total = PASS+DEFER+FAIL
        
        if total>120:
            
            print("Total incorrect")
         
        elif PASS == 120:
            print("Progress")
            
              
        elif PASS == 100 and DEFER == 20:
            print("Progress (module trailer)")
                 
        elif PASS == 100 and FAIL == 20:
            print("Progress (module trailer)")
                 
         
                 
        elif 0 <= PASS <= 80 and 0 <= DEFER <= 120 and 0 <= FAIL <= 60:
            print("Do not Progress – module retriever")
                 
        elif 0<=PASS <= 40 and 0 <= DEFER <= 40 and 80 <= FAIL <= 120:
            print("Exclude")
                 
        else:
            print("Invalid input")
                 

             
              
       
             
        print("Would you like to enter another set of data?")
        pq=input("Enter 'y' for yes or 'q' to quit and view result :")

        if pq.lower()=='y':
            
            continue
        elif pq.lower()=='q':
            break
        else:
            print("invalid input")
            break




 
pro_count=0
mt_count=0
mr_count=0
exc_count=0
total_outcomes=0     






def staff_code():
    print("You choose staff_code")
    global pro_count,mt_count,mr_count,exc_count,total_outcomes
         
     





    while True:
        try:
            while True:
                try:
                    user_ID =input("Enter student id: ")
                    PASS = int(input("Please enter your credits at pass: "))
                    if PASS not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                        continue
                    break
                except ValueError:
                    print("Integer required.")
            while True:
                try:
                    DEFER = int(input("Please enter your credits at defer: "))
                    if DEFER not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                        continue
                    break
                except ValueError:
                    print("Integer required.")
            while True:
                try:
                    FAIL = int(input("Please enter your credits at fail: "))
                    if FAIL not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                        continue
                    break
                except ValueError:
                    print("Integer required.")
        except ValueError:
            print("Integer required")
            continue
        
        total = PASS+DEFER+FAIL
        
        if total>120:
            
            print("Total incorrect")
         
        elif PASS == 120:
            print("Progress")
            pro_count= pro_count+1
            
              
        elif PASS == 100 and DEFER == 20:
            print("Progress (module trailer)")
            mt_count=mt_count+1
                 
        elif PASS == 100 and FAIL == 20:
            print("Progress (module trailer)")
            mt_count=mt_count+1
                 
         
                 
        elif 0 <= PASS <= 80 and 0 <= DEFER <= 120 and 0 <= FAIL <= 60:
            print("Do not Progress – module retriever")
            mr_count=mr_count+1
                 
        elif 0<=PASS <= 40 and 0 <= DEFER <= 40 and 80 <= FAIL <= 120:
            print("Exclude")
            exc_count=exc_count+1
            total_outcomes= pro_count+mt_count+mr_count+exc_count
                 
        else:
            print("Invalid input")
                 

 


            
            
        Credit_vol= [PASS,DEFER,FAIL]   
        credit_vol_index = Credits_levels.index(Credit_vol)
        Credit_Vol_Available = credit_vol_index in Credits_levels
        progression_type=  Progresion_outcomes[credit_vol_index] 

        
        if Credit_Vol_Available:
            progression_type =Progresion_outcomes[credit_vol_index]
            print(progression_type)
            
        
            
             
         
             


        user_input_pro.append(progression_type)
        user_credit_vol.append(Credit_vol)
        Student_IDs.append(user_ID)

 


         



        
                             
             
        print("Would you like to enter another set of data?")
        pq=input("Enter 'y' for yes or 'q' to quit and view result :")

        if pq.lower() == 'y':
            
            
            continue
        elif pq.lower() == 'q':
            break
        else:
            print("invalid input")
            break
         


def choose_function():
    while True:
        choice = input("Enter 1  student_code or 2 for staff_code : ")
        if choice == '1':
            student_code()
            break
        elif choice == '2':
             staff_code()
             break
        else:
            print("Invalid choice, please try again")

choose_function() 

 

def read_progression_file(file_Name):
    try:
        file_progression_R = open(file_Name, 'r')
        for x in file_progression_R.readlines():
            list_pro.append(x)
        file_progression_R.close()
    except Exception as e:
        print(e)


def read_credit_volume_file(file_name):
    try:
        file_Credit_Vol_R = open(file_name, "r")
        for x in file_Credit_Vol_R.readlines():
            list_cv.append(x)
        file_Credit_Vol_R.close()
    except Exception as e:
        print(e)


def write_file():
    try:
        with open('user_input_pro.txt', 'w+') as f:
            for line in user_input_pro :
                f.write('%s\n' % line)

        with open('user_credit_vol.txt', 'w+') as f:
            for line in  user_credit_vol:
                f.write('%s\n' % line)

    except Exception as e:
        print(e)


# read files
read_progression_file("user_input_pro.txt")
read_credit_volume_file("user_credit_vol.txt")


def print_details_from_file():
    try:
        print("--------------------------------------------------")
        for x in list_pro:
            print("Progresion_outcomes: ", x, "Volume of Credit: ", list_cv[list_pro.index(x)],
                  "--------------------------------------------------\n",  )
    except Exception as e:
        print(e)
 






print("---------------------------------------------------------------------------------------------------------------------")
 
pro_count_str = "*" * pro_count
mt_count_str = "*" * mt_count
mr_count_str = "*" * mr_count
exc_count_str = "*" * exc_count
total_outcomes= pro_count+ mt_count+mr_count+exc_count

print("Histogram")
print("progress",pro_count,":" ,pro_count_str )
print("Trailer",mt_count,":" ,mt_count_str )
print("Retriiver",mr_count, ":", mr_count_str  )
print("Exclude",exc_count, ":" , exc_count_str )
print("Total outcomes "," : " ,total_outcomes )


 


 

#part 2
print("---------------------part 2-------------------")
for i in range(total_outcomes):
    print(user_input_pro [i], " : ",  user_credit_vol[i])




#part 3
 
print("--------------------part 3--------------------")
write_file()
print_details_from_file()









 








