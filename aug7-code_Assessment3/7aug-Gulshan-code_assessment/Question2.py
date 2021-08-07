import json,operator,smtplib,logging,time
import validation as val
try:
    class Student:
        def __init__(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
            self.details ={}
            self.details['name'] = name
            self.details['rollno']=rollno
            self.details['admno']=admno
            self.details['college']=college
            self.details['parentname']=parentname
            self.details['mobilenumber']=mobilenumber
            self.details['emailid']=emailid       
    class Sem1Result(Student):
        def __init__(self, name, rollno, admno, college, parentname, mobilenumber, emailid):
            super().__init__(name, rollno, admno, college, parentname, mobilenumber, emailid)        
        def student_marks(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark,current_time):
            self.details['sub1mark'] = int(sub1mark)
            self.details['sub2mark'] = int(sub2mark)
            self.details['sub3mark'] = int(sub3mark)
            self.details['sub4mark'] = int(sub4mark)
            self.details['sub5mark'] = int(sub5mark)
            self.details['addon']= current_time
            total= int(mark1)+int(mark2)+int(mark3)+int(mark4)+int(mark5)
            self.details['total']= total
            percentage = (total/200)*100
            self.details['percentage']= percentage
        def print_details(self):
            print(self.details)
    student_li=[]
    while(True):
        print("*****MENU*****")
        print('Press 1 for Add Student details with mark')
        print('Press 2 for Generate JSON file and display the API to view all student details with marks')
        print('Press 3 for Generate JSON file and display the API to view all student details based on ranking')
        print('Press 4 for Send an email to all the parents if the total percentage of marks is less than 50% ')
        print('Press 5 for Exit - ')
        choice = int(input('enter your choice - '))
        if(choice==1):
            name = input('enter student name-')
            rollno =input('enter student rollno-')
            admno = input('enter student admno -')
            college = input('enter student college_name-')
            parentname = input('enter student parent_name-')
            mobilenumber = input('enter student mobile_number-')
            emailid = input('enter student emailID-')
            mark1 = input('enter the sub1marks - ')
            mark2 = input('enter the sub2marks - ')
            mark3 = input('enter the sub3marks - ')
            mark4 = input('enter the sub4marks - ')
            mark5 = input('enter the sub5marks - ')
            current_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
            result = Sem1Result(val.val_name(name),val.val_rollno(rollno),val.val_admno(admno),college,val.val_parentname(parentname),val.val_mobilenumber(mobilenumber),val.val_emailid(emailid))
            result.student_marks(val.val_mark1(mark1),val.val_mark2(mark2),val.val_mark3(mark3),val.val_mark4(mark4),val.val_mark5(mark5),current_time)
            student_li.append(result.details)
        elif(choice==2):
            print(student_li)
            myjson=json.dumps(student_li)
            with open("API_Type.json","w",encoding="utf-8") as f:
                f.write(myjson)
        elif(choice==3):
            student_li.sort(key=operator.itemgetter('total'))
            rev = student_li[::-1]
            myjson=json.dumps(rev)
            with open("Ranking.json","w",encoding="utf-8") as f:
                f.write(myjson)
        elif(choice==4):
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("gulshan062132@gmail.com","Gullu@2132")
            new_li=[x for x in student_li if x["percentage"]<50]
            for x in new_li:
                message='your Son/Daughter percentage less - '+str(x['percentage'])
                connection.sendmail("gulshan062132@gmail.com",x['emailid'], message)
            connection.quit()
        elif(choice==5):
            break
except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfuly")
finally:
    print("Thank you!!")

