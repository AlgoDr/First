import os,sys
import getpass
import csv
import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

 

def L_menu(L_name):
    
    print("Welcome to The Python Payments Bank Mr./Mrs.",L_name)
    print("How May I assest You")
    print("Here Are The Services We Offered To Our Customer")

    Choice = int(input("1.Deposit\n2.Withdraw\n3.check Balance\n4.LogOut\n5.Loan(procedure)\n"))
    df = pd.read_csv('bal.csv')
    df.drop('Unnamed: 0',axis =1 ,inplace =True)
    u = df['Username']
    b = df['balance']

    if Choice == 4:
        print("----------------------------------------------------")
        print("You Hit The Log Out Button There You go")
        print("----------------------------------------------------")
        Menu()
        
        
    if Choice == 3:
        for i in range(0,len(df.index)):            
            if u[i] == L_name:
                print(L_name,"Your balance is:",b[i])
                print("----------------------------------------------------")
                L_menu(L_name)
                break

    if Choice == 2:
        Amt = int(input("Enter The Amount to be Withdraw:\n")) 
        for z in range(0,len(df.index)):
            if u[z] == L_name:
                if b[z] <= 0:
                    print("Mr./Mrs",L_name)
                    print("We Are Sorry For Discarding Your Transaction")
                    if b[z] <=(-50000):
                        print("You Have Already Pending Loan Of 50,000 ")
                        print("As Per Our Bank Policy We Cannot Give You Loan More Than That")
                        print("Thank You For Choosing Python Payments Bank")
                        print("---------------------------------------------------------------------------\n")
                        print("---------------------------------------------------------------------------\n")
                        Login()
                    print("BUt Your Balance Is Empty Or Below Zero")
                    print("Do You Wanna Take A Loan For This Amount")
                    c=input('Yes Or No(Y/N)')
                    if (c=='N') or(c=='n'):
                        print("You Select No ")
                        print("That Means You Dont Require Loan Thanks You Have a Good Day Mr.Mrs",L_name)
                        L_menu(L_name)
                    if (c=='Y') or(c=='y'):
                        b[z] = b[z]-Amt                 
                        df['balance'] = b 
                        df.to_csv('bal.csv')
                        print("Your Loan Is Sention Mr./Mrs.",L_name)
                        print("The (-)Negative Sign Represnt You Have Taken Loan See Below")
                        print(L_name," Now Your new Balance is",b[z])
                        print("----------------------------------------------------")
                        L_menu(L_name)
                        break

                       
                else:
                    b[z] = b[z]-Amt                 
                    df['balance'] = b 
                    df.to_csv('bal.csv') 
                    print(L_name,"Your new Balance is",b[z])
                    print("----------------------------------------------------")
                    L_menu(L_name)
                    break
    
    if Choice ==5:
        print("For Taking The Loan Please Follow Below Steps:")
        print("1)In Order To Take Loan After This Messege You Redirect To Menu Again")
        print("2)Than After You Have To Go Through Withdraw Section")
        print("3)Enter THe Amount You Want To Take Loan As Withdraw")
        print("4)If Your Current Balance Is Below Zero Or Even If Below Zero")
        print("5)The System Will Automatically Asked You For Taking An Loan")
        print("6)Select Yes From There")
        print("7)And Your Loan Will Be Senstioned To Y")
        print("If Your Already Taken Loan More Than 50,000 Than Your Connection Will Be Discarded")
        print("Now You Will Be Redirect To Banking page")
        print("---------------------------------------------------------------------------\n")
        print("---------------------------------------------------------------------------\n")
        L_menu(L_name)



    if Choice == 1:
        Amount = int(input("Enter The Amount to be Deposit:\n"))
        for y in range(0,len(df.index)):
            if u[y] == L_name:
                b[y] = b[y]+Amount
                df['balance'] = b 
                df.to_csv('bal.csv')
                print(L_name,"Your new Balance is",b[y])
                print("----------------------------------------------------")
                L_menu(L_name)                
                break


    if (Choice>5 or Choice<0):
        print("please Choose appropriate Choice\n")
        print("Your Session Expired\n")
        Login()



def Login():
    L_name = input("Please Enter Your Registered Email:\n")
    L_pass = getpass.getpass("Enter Your Password:\n")
    df = pd.read_csv('db.csv')
    u1 = df['Username']
    p1 = df['password']
    for x in range(0,len(df.index)):
        if u1[x] == L_name:
            if p1[x] == L_pass:
                print("Credentials Found in Database\n")
                print("You Now Got Privellege to use Your Banking Services")
                L_menu(L_name)                           
                break
        

    





def Signup():

    U_name = input("Hello Sir Please Choose An Username:\n")
    
    df = pd.read_csv('db.csv')
    s1 =df['Username']
    for x in range(0,len(df.index)):
        if (s1[x] == U_name):
            print("username already taken\n")
            Signup()
            break   
            
            

    initial_balance = 0   
    U_pass = getpass.getpass("Now Select An Password For Your Account:\n")
    C_pass = getpass.getpass("Confirm Your Password:\n")
    # data for 1st db
    data ={'Username':[U_name],'password':[ str(U_pass) ]}
    df = pd.DataFrame(data)

    # data for 2nd db
    ndata ={'Username':[U_name],'balance':[initial_balance]}
    ndf = pd.DataFrame(ndata)

    if U_pass == C_pass:
        # for 1 st file
        df.to_csv('db.csv',mode ='a',header=False )
        df1 = pd.read_csv('db.csv')        
        df1.drop('Unnamed: 0', axis=1, inplace=True)
        df1.to_csv('db.csv')
        # for 2nd File
        df2 = pd.read_csv('bal.csv')        
        df2.drop('Unnamed: 0', axis=1, inplace=True)
        ndf.to_csv('bal.csv',mode ='a',header=False )
        
        print(df)
    
        print("Your Login Credentials Are Genrated Please Login Through Main Menu :")
        Menu()

    else:
        print("Your Password MisMatch Pls Try Again")
        print("-------------------------------------\n")
        Signup()
    


def Menu():
    print("-----------Welcome To Python Bank--------------------------")
    print("------Please Select One Of The Choice From Below Fields------")
    Choice = int(input("1.Login\n2.Signup\n3.exit\n"))


    if (Choice >3 or Choice<0):
        print("Please Enter An Valid Choice From One of the Above")
        Menu()
    
    if Choice == 2:
        Signup()

    if Choice == 1:
        Login()

    if Choice == 3:
        print("----------------------------------------------------")
        print("You Hit The exit Button There You go")


Menu()