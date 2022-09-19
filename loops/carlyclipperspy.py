hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Prices and Cuts:

total_price = 0

for price in prices:
  total_price += price
  #print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))
#print('Average Price: ${0} '.format(average_price))

#Carly wanted all prices on list reduced by 5
new_prices = [price - 5 for price in prices]
print(new_prices)

#Revenue:

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total revenue: $' + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $" + str(average_daily_revenue))

#Cuts under $30:
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)

