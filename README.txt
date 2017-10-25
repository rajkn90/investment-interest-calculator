This script calculates Return of Investment(ROI) for an investment account with multiple deposits and withdrawals made at different times. This calculation considers both the amount of money invested and the time it was invested for, in order to find an equivalent daily compounded interest rate. It also provides Annualized compounded interest based on this daily interest rate and interest rate until current date. 

sample.txt is the input and it has the following format:

<Number of deposits (withdrawals are also considered as deposits, but with a negative amount)>
Deposit_1_Date in <Year Month Date> format and <Deposit_1_Amount> 
Deposit_2_Date in <Year Month Date> format and <Deposit_2_Amount> 
Deposit_3_Date in <Year Month Date> format and <Deposit_3_Amount> 
..
..
..
Deposit_N_Date in <Year Month Date> format and <Deposit_N_Amount>
Current_Date in <Year Month Date> format and <Current_Value_In_Account>

To run: 
>> python calc_interest.py sample.txt

Sample output looks like this:

Deposit Date   Amount 
2017-04-21      10.0
2017-05-01      100.0
2017-05-04      3000.0
2017-06-02      980.0
2017-06-30      990.0
2017-09-08      1500.0
2017-09-25      420.0
2017-10-13      500.0

Current Date   Current Value 
2017-10-14      8161.6 

Daily Compounded Interest =  0.07768487600818738 %
Annualized Compounded Interest =  32.76888405463409 %
Interest Until 2017-10-14 is  14.645239656015118 %
