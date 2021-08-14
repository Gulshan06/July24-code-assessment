import re
def val_name(name):
    val4=re.search('[A-Za-z]',name)
    if val4:
        return name
    else:
        print('something went wrong - you enter wrong name')

def val_mobilenumber(mobile_number):
    val5=re.search("^(\+91)?[0]?[91]?[6-9]\d{9}$",mobile_number)
    if val5:
        return mobile_number
    else:
        print('something went wrong - you enter wrong mobile_number')


def val_emailid(emailid):
    val6=re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailid)
    if val6:
        return emailid
    else:
        print('something went wrong - you enter wrong emailid')


def val_pincode(pincode):       
    val7=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
    if val7:
        return pincode
    else:
        print("something went wrong - you enter wrong pincode")



