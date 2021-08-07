import multiprocessing,time,logging
try:
    def even_num(myli):
        for i in myli:
            if(i % 2 == 0):
                time.sleep(1)
                print(i)

#******odd Number*****

    def odd_num(myli):
        for i in myli:
            if(i %2 != 0):
                time.sleep(1)
                print(i)

    if(__name__=="__main__"):

        myli=list(map(int,input("Enter element of list- ").split()))
        p1=multiprocessing.Process(target=even_num,args=(myli,))  #create a thread
        p2=multiprocessing.Process(target=odd_num,args=(myli,))
        p1.start()
        p1.join()
        print(".......")
        p2.start()
        p2.join()
        print(".......")
except Exception:
    logging.error("Something went error")
finally:
    print("Thank You!!")