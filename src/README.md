![Python](https://miro.medium.com/max/2000/1*DID7M5LN6--mf7sXAKVZ-g.png)
## An CLI Based Banking App Made With Pandas 

>Execute 1.py And

You Will Get Menu Of Basic Services Of Bank Application Like New Customer,Already A Customer And Once You Choose Them They Validate Your Credentials From The Database Or Add Your Data Logs Into Database It Directly Depends Onto What Choice You Made,But Like For In Genral You Must Have Credentials In Order To Login Through Existing Customer

Now Suppose If Your Choice Is New Customer The Script Will Now Ask You To Enter Your Credentials One By One As Per User Favourable And Once All The Entry Wore Made Correctly Along With Validation For Exceptions(Like If The Username Got Already Taken Or You Mismatch Entered Password And Confirm Password Or If You Enetered Empty Entry Field).Our Programe Will Show You The Credentilas You Genrated Onto Screen With No Asterisk ' * '(As Confirmation Because The Default Entry You Entered In Passord Is Encrypted Using Getpass Method)And This Credentials Will Goes To Our CSV Database(Using Pandas) So They Can Be Use You To Recognize That User In Future.

Now Once You Have Registered For New User You Can Use Your Credentials To Login And Use Your Banking Services We Offered Like Debit(Deposit),Credit(Withdraw),Check Your Current Balance,Applying For Loan. You Can Choose Any Service .This Will Update Your Current Balance At Run Time Based On What You Choose.Our System Gets Updated Automatically Means If You Choose For Deposit .The Deposit Amount Will Be Updated To Your Current Balance Using Pandas Dataframe Approch Similarly For Withdraw Same Rule Apply .But If Your Balance IS Zero Or Below The Sytem Will Suggest You For The Loan Based On That If You Choose Yes For Loan That Much Amount Will Be Sentioned As Loan But There Is Some Exceptions For Taking Loan(Read Next Paragraph)

Now If You Wish To Apply For Loan The Sytem Will Show You The Procedure To Take The Loan And You Will Redirect Automatically To The Loan Section Of Code Where You Can Make A Choice For Taking Loan Then System Will Check For You Have Been Taken Loan Already Or Not And Based On Your Previous Transaction It Will Acknowledge You About To Give Loan Or Not.If Your Total Of Loan Amount Exceeds The Bank Loan Policy Limit Your Transaction Will Be Discarded And You Will Be Redirect To The Login Page Again

Note:-So This App Is An Simpler Approch To The Code ,short and easy to understand with minimalistic numbers of lines. The beckend Mechanism followed By The Code Is PANDAS as I Am Currently Lerning Data Science ,This library Offer Great Range OF Commands Over Full Advantages By Which data handling ,modifiacation,And Manupulation Can Be Done In Easier Way.

I Know The Above Explanation Is To Childish For any IT guy .But This Is Me And Its My Way To Represent Documenatation So Easily That Even a Non-Tech Guy Gets An Basic Idea About What Actually Happening In Backend And How The Mechanism Is Implemented.
