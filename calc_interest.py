import sys
import datetime as date
from datetime import *

class Interest_Calculator():
	def __init__(self, depositDates, depositAmounts, currentDate, currentAmount):
		self.setDepositDates(depositDates, currentDate)
		self.setDepositAmounts(depositAmounts)

		self.currentAmount = currentAmount
		
		self.dailyCompoundedInterestRate = 0.0
		self.annualizedInterestRate = ((1+self.dailyCompoundedInterestRate)**365)-1.0

		self.init_k = 0.0
		self.maxIterations = 100
		self.epsilon = 0.000001
		self.tolerance = 0.000000001
		self.solutionFound = False

	def setDepositDates(self, dates, currentDate):
		self.depositDates = dates
		self.currentDate = currentDate
		self.tDays = [(self.currentDate-date).days for date in self.depositDates]
		#print(self.tDays)

	def setDepositAmounts(self, amounts):
		self.depositAmounts = amounts
		#print(self.depositAmounts)

	def runCalculator(self):
		k = self.init_k
		for i in range(self.maxIterations):
			y, yprime = self.get_funcValues(k)
			#print(k)
			if(abs(yprime) < self.epsilon):
				break

			new_k = k - (y/yprime) #Do Newton's computation
			if(abs(new_k - k) <= self.tolerance): #If the result is within the desired tolerance
				self.solutionFound = True
				break #Done, so leave the loop

			k = new_k #Update k to start the process again

		if (self.solutionFound): #x1 is a solution within tolerance and maximum number of iterations
			self.dailyCompoundedInterestRate =  k
			self.annualizedInterestRate = ((1+self.dailyCompoundedInterestRate)**365)-1.0
		else:
			self.dailyCompoundedInterestRate = 0.0

		return self.solutionFound

	def get_funcValues(self, x):
		func_value = -self.currentAmount;
		diff_func_value = 0.0;
		for i in range(len(self.tDays)):
			func_value += ((1+x)**self.tDays[i])*self.depositAmounts[i]
			diff_func_value += ((1+x)**(self.tDays[i]-1))*self.tDays[i]*self.depositAmounts[i]

		return func_value, diff_func_value

	def getDailyCompoundedInterestRate(self):
		return self.dailyCompoundedInterestRate

	def getAnnualizedInterestRate(self):
		return self.annualizedInterestRate

	def getCurrentInterestRate(self):
		return ((1+self.dailyCompoundedInterestRate)**self.tDays[0])-1.0

if __name__ == '__main__':
	input_filename = sys.argv[1]
	f = open(input_filename, 'r')
	# Read number of deposits
	no_of_deposits = int(f.readline())
	print("\nDeposit Date   Amount ")
	
	depositDates=[]
	depositAmounts=[]
	for i in range(no_of_deposits):
		line = f.readline()
		line = ' '.join(line.split())
		line = line.split(' ')[:4]
		deposit_date = date(int(line[0]), int(line[1]), int(line[2]))
		amount = float(line[3])
		depositDates.append(deposit_date)
		depositAmounts.append(amount)
		print(deposit_date, "    ", amount)
	line = f.readline()
	line = ' '.join(line.split())
	line = line.split(' ')[:4]
	currentDate = date(int(line[0]), int(line[1]), int(line[2]))
	currentAmount = float(line[3])

	print("\nCurrent Date   Current Value ")
	print(currentDate, "    ", currentAmount, "\n")

	calc = Interest_Calculator(depositDates, depositAmounts, currentDate, currentAmount)
	if(calc.runCalculator()):
		print("Daily Compounded Interest = ", calc.getDailyCompoundedInterestRate()*100, "%")
		print("Annualized Compounded Interest = ", calc.getAnnualizedInterestRate()*100, "%")
		print("Interest Until ", currentDate, "is ", calc.getCurrentInterestRate()*100, "%")
		print("")
	else:
		print("Interest couldn't be calculated. Newton's method failed to converge")