import re
def val_name(name):
    val1=re.search('^[A-Za-z]',name)
    if val1:
        return name
    else:
        print('something went wrong - you enter wrong Name')
        print("Please enter 5 and again fill the data")

def val_rollno(rollno):
    val2=re.search("^[0-9]{2}",rollno)
    if val2:
        return rollno
    else:
        print('something went wrong - you enter wrong rollno')
        print("Please enter 5 and again fill the data")

def val_admno(admno):
    val3=re.search("[0-9]{0,9}$",admno)
    if val3:
        return admno
    else:
        print('something went wrong - you enter wrong admno')
        print("Please enter 5 and again fill the data")

def val_parentname(parentname):
    val4=re.search('[A-Za-z]',parentname)
    if val4:
        return parentname
    else:
        print('something went wrong - you enter wrong parentname')
        print("Please enter 5 and again fill the data")

def val_mobilenumber(mobilenumber):
    val5=re.search("^(\+91)?[0]?[91]?[6-9]\d{9}$",mobilenumber)
    if val5:
        return mobilenumber
    else:
        print('something went wrong - you enter wrong mobile_number')
        print("Please enter 5 and again fill the data")

def val_emailid(emailid):
    val6=re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailid)
    if val6:
        return emailid
    else:
        print('something went wrong - you enter wrong emailid')
        print("Please enter 5 and again fill the data")


#************* Marks validation *************

def val_mark1(mark1):
    val7 = re.search("^(40|[1-3][0-9]?)$",mark1)
    if val7:
        return mark1
    else:
        print('something went wrong - you enter wrong mraks in marks 1')
        print("Please enter 5 and again fill the data")

def val_mark2(mark2):
    val8 = re.search("^(40|[1-3][0-9]?)$",mark2)
    if val8:
        return mark2
    else:
        print('something went wrong - you enter wrong mraks in marks 2')
        print("Please enter 5 and again fill the data")

def val_mark3(mark3):
    val9 = re.search("^(40|[1-3][0-9]?)$",mark3)
    if val9:
        return mark3
    else:
        print('something went wrong - you enter wrong mraks in marks 3')
        print("Please enter 5 and again fill the data")

def val_mark4(mark4):
    val10 = re.search("^(40|[1-3][0-9]?)$",mark4)
    if val10:
        return mark4
    else:
        print('something went wrong - you enter wrong mraks in marks 4')
        print("Please enter 5 and again fill the data")

def val_mark5(mark5):
    val11 = re.search("^(40|[1-3][0-9]?)$",mark5)
    if val11:
        return mark5
    else:
        print('something went wrong - you enter wrong mraks in marks 5')
        print("Please enter 5 and again fill the data")
