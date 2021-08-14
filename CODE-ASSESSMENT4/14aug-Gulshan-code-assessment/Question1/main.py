import validation as val
import logging,pymongo,smtplib,time
donorlst=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['BloodbankmgtDb'] #database
    collection_name=mydatabase['Blood']
    class BloodBankMgt:   # class
        def donor(self,name,address,blood_group,pincode,mobile_number,emailid,last_donate_date,place):   # doner function 
            current_time=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            dict1={"name":name,"address":address,"blood_group":blood_group,"pincode":pincode,"mobile_number":mobile_number,"emailid":emailid,"last_donate_date":last_donate_date,"place":place,"AddOn":current_time,"delflag":0} 
            donorlst.append(dict1)
    obj=BloodBankMgt()
    while True:
        print("****** BloodBank Management System ********")
        print("1.Add Donor Details")
        print("2.Search Donors based on blood group ") 
        print("3.Search Donors based on blood group AND place ")
        print("4.Update all the details based on mobile number ")
        print("5.Delete the donor based mobile number ")
        print("6.Display the total number of donors on each blood group ")
        print("7.Notification to all Donor via email ")
        print("8.View all the Doner")
        print("9.Exit")
        choice=int(input("Enter your option : "))
        if choice==1:
            name=input("Enter the Donor - ") 
            address=input("Enter the Donor Address - ") 
            blood_group=input("Enter the Donor Blood group - ") 
            pincode=input("Enter the Doner Pincode - ")
            mobile_number=input("Enter the Donor Mobile Number - ")
            emailid= input("Enter your emailid - ")
            last_donate_date=input("Enter the Donor Last Donate Date - ")
            place=input("Enter the Donor Place - ")
            data=obj.donor(val.val_name(name),address,blood_group,val.val_pincode(pincode),val.val_mobilenumber(mobile_number),val.val_emailid(emailid),last_donate_date,place) 
            result=collection_name.insert_many(donorlst)
            print(result.inserted_ids)
        elif choice==2:
            a = input('enter the blood group')
            result = collection_name.find({"blood_group":a})
            l = []
            for i in result:
                l.append(i)
                print(l)  
        elif choice==3:
            blood_group=input("enter the blood_group - ")
            place=input("enter the place - ")
            result=collection_name.find({"$and":[{"blood_group":blood_group},{"place":place}]},{"delflag":0})
            for i in result:
                print(i)  
        elif choice==4:
            t=input("enter the doner mobile no - ")
            print("***enter the updated details***")
            a = input("enter the updated address - ")
            b = input("enter the updated pincode - ")
            c = input("enter the last donate date - ")
            d = input("enter the  updated place - ")
            e = input("enter the updated name - ")
            f = input("enter the updated emailid - ")
            g = input("enter the updated blood group - ")
            result=collection_name.update_many({'mobile_number':t},{"$set":{"address":a ,"pincode":b,"last_donate_date":c,"place":d,"name":e,"emailid":f,"blood_group":g}})
            print("data updated")
        elif choice==5:
            mobile_number = input('enter mobile number -')
            result=collection_name.update_one({"$and":[{"mobile_number":mobile_number}]},{"$set": {'delflag':1}})
        elif choice==6:
            result= collection_name.aggregate([{'$group':{'_id':"$blood_group","no_of_Doner":{'$sum':1}}}])
            for i in result:
                print(i)
        elif choice==7:
            result=collection_name.find()
            hos = input("enter the hospital name ")
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("gulshan062132@gmail.com","Gullu@2132")
            for x in result:
                message="Immediately want A+ blood group in "+ hos +' Hospital . \n THANK YOU!!'
                connection.sendmail("gulshan062132@gmail.com",x['emailid'], message)
            connection.quit()
            print("Message sended")  
        elif choice==8:
            result=collection_name.find()
            for i in result:
                print(i)
        elif choice==9:
            break 
except:
    logging.error("Something is wrong You enter wrong input ") 

else:
    print("your program completed successfuly")   
finally:
    print("Thank you")