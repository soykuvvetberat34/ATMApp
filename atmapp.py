#ATM application 


check_user=input("Are you user?(y/n):")

if check_user =="n":
    print("registiration")
    userName=input("what's your name?:")
    userSurname=input("What's your surname?:")
    GGmoney=int(input("the amount you want to deposit"))
else:
    print("Welcome")
    userName="user0101010101"
    userSurname="none"
    GGmoney="None"
        
    
    
user1={
    "user name":"Berat",
    "user surname":"SOYKUVVET",
    "user money":20000    
}

user2={
    "user name":userName,
    "user surname":userSurname,
    "user money":1000   
}
    
    
    
    
def GiveMoney(amount=user2["user money"],username1=userName,usersurname1=userSurname):
    print(f"{username1} {usersurname1} please enter the amount you want to deposit ")
    moneyAmount=int(input("enter:"))
    user2["user money"]+=moneyAmount
    print("your budget:",user2["user money"])
    
def GetMoney(monyleft=0,username2=userName,usersurname2=userSurname):
    print("please enter the amount you want to withdraw")
    GetMoney2=int(input("enter:"))
    if user2["user money"]>=GetMoney2:
        user2["user money"]-=GetMoney2
        print("your budget:",user2["user money"])
    else:
        print("you don't have money enough")

actions=input("please select your action(getmoney/givemoney):")    
if actions=="getmoney":
    GetMoney()    
else:
    check=input("you mean givemoney(y/n):")
    if  check=="y":
        GiveMoney()
    else:
        GetMoney()
    



