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


    

 

        if total== 120:
            
            Credit_Vol = [PASS,DEFER,FAIL]
            is_Credit_Volumes_Available = Credit_Vol in  Credits_levels     
            
        

        
        if is_Credit_Volumes_Available:

                            credit_volume_id =Credits_levels.index(Credit_Vol)
                            # print("credit_volume_id ",credit_volume_id)
                            progression_type =  Progresion_outcomes[credit_volume_id]
                            print(progression_type)

                            # part 2 support >>>>
                            user_input_pro.append(progression_type)
                            user_credit_vol.append(Credit_Vol)
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



print("part 4")

print("--------- part 4---------")
for i in Student_IDs:
    student_rec[i] = str(user_input_pro[Student_IDs.index(i)]), str(
        user_credit_vol[Student_IDs.index(i)])

# get output from Dictionary
for x in student_rec:
    print(x, " : ", student_rec[x])





 






