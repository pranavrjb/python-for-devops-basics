def myFunc():
    print('Hello world')
    
    if __name__=="__main__":
    #if this code is directyly executed by running the file its present in 
        print("We are directly running this code")    
        myFunc()
        print(__name__)