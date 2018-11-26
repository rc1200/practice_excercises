a = "1234567"

print (a)
print (a[0])
print (a[2])
print (a[-1])
print (a[:-1])
print (a[2:-2])


a = "Xbox 360 | 99.99 | New"



print (a.index('|'))
print (a[0:a.index('|')])

# [Start: stop: step]

a = "1234|5678|90AB|CDE"
print (a[1:-1:1])
print (a[1:-1:2])

# Split or Parse by character
print(a.split('|'))


# List
groceries = ['apple','banana','Orange','Squash']
print(groceries)
print(groceries[0])
print(groceries[2])
print(groceries[-1])

# List [Start: stop: step]
print(groceries[::-1])



greeting1 = 'how are you today?'.split(' ')
greeting2 = 'how-are-you-today?'.split('-')

print(greeting1[2])
print(greeting2[2])
print(greeting2[2:4])
print(greeting2[::-1])

oneString = "Reverse the letters 1234"
print(oneString[::-1])


ItemForSale = "xbox 360 | $100 | New"
print(ItemForSale)

detailData = ItemForSale.split('|')
Item = detailData[0]
price = detailData[1]
condition = detailData[2]

print(Item)
print(price)
print(condition)


Item2, price2, condition2 = ItemForSale.split('|')
print(Item2)
print(price2)
print(condition2)

