def calculate_monthly_payments(median_price,interest_rate=.05,down_payment=.2,term=30):
	# median home price for single family homes = 947260. per SF Chronicle 2013-06-27
	# Fixed monthly payment formula P = L[c(1 + c)n]/[(1 + c)n - 1]
	# P = payment, L = loan amount, c = interest rate, n = months
	L = median_price - (median_price * down_payment)
	r = ((interest_rate * 100)/12)/100
	n = term * 12
	#
	P = L*r*(1+r)**n / (1+r)**n -1
	return P

def calculate_typical_annual_income(monthly_payments):
	return (monthly_payments * 12) * 4