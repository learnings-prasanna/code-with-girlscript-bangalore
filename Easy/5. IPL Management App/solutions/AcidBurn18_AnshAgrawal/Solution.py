while(True):
    
    x=input("Enter the Numbers of Team Playing:- ")
    if(x.isnumeric()):
        temp=[]
        count=1
        x=int(x)
        while(x!=0):
            
            print("Team",count,"details")
            name=input("Enter Name of the Team:- ")
            captain=input("Name of Captain of the team:- ")
            franc=input("Franchise of The Team:- ")
            home=input("Home Ground of the Team:- ")
            store={"1":name,"2":captain,"3":franc,"4":home,"5":count}
            temp.append(store)
            count+=1
            x-=1
        print("Want to see the details of all teams press enter")
        en=input()
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("Sr.No.","Team Name","Captain","Franchise","Home Ground"))
        for j in range(len(temp)):
            print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(temp[j]["5"],temp[j]["1"],temp[j]["2"],temp[j]["3"],temp[j]["4"]))
    
        break
    else:
        print("Please Enter in Numeric form")
