# CTI-110 
# P2T1 - Sales Prediction 
# Brandon Wilson
# 6 June 2018

#Get projected total sales

totalSales = float(input('Enter Projected annual sales: '))

#Calculate profit as 23% of projected total sales

annualProfit = 0.23 * totalSales

#display profit

print('Annual profit is $', format(annualProfit, ',.2f'))


