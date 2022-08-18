import json

student_id = 0  

list = [] 

#creating the class student from where we access its methods and attributes
class Student():
    first_name = ''
    last_name = ''  
    school_name = ''
    stud_class = ''
    std_id = 0

#Adding details

    def add_data(self): 
        globals()['student_id'] = globals()['student_id'] + 1
        self.std_id = globals()['student_id']
        self.first_name = input("enter your firstname\n")
        self.last_name = input("enter your lastname\n")
        self.school_name = input("enter your school name\n")
        self.stud_class = input("enter your class\n")

        dict = {"firstname": self.first_name, 
        "lastname": self.last_name, 
        "school": self.school_name,
        "student_id": self.std_id, 
        "student_class": self.stud_class}  
        list.append(dict)  

#Opening and storing file in json
        file = open('data1.json', 'w')  
        file.write(json.dumps(list)) 
        print("Data Recorded\n")

#This functon will display data.
    def display(self):
        std_id = int(input("Enter student Id\n"))
        file = open('data1.json', 'r')  #Retrieving and opening data
        record = json.loads(file.read())  # converting the json  data into python list
        count = 0
        for obj in record:   
            if obj['student_id'] == std_id:
                print(obj)
                count = 1
                break
        if count == 0:
            print("record is not available with this id\n")



#This function will delete the data from the record
    def delete_record(self):
        std_id = int(input("please enter the Id of the student\n"))
        file = open('data1.json', 'r')
        record = json.loads(file.read()) 
        flag = 0
        for obj in record:  
            if obj['student_id'] == std_id:
                record.remove(obj)
                file2 = open('data1.json', 'w')
                file2.write(json.dumps(record))
                count = 1
                break
        if count == 0:
            print("record is not available with this id\n")



class school_student(Student):
    def get_school_details(self,s_id):
        
        with open('data1.json','r') as f:
            Data = json.load(f)
        for i in Data:
            if i['student_id'] == s_id:
                print(i['school'])
    def strength(self):
        with open('data1.json','r') as f:
            Data = json.load(f)
        count = 0
        for i in Data:
            count += 1
        print(count)   
    

class college_student(Student):
    def get_college_details(self,c_name):
        pass