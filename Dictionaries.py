
#Dictionary

phone_book =['1111', '2222','3333']

print(phone_book[0])
print(phone_book[1])


#  dictionaires
#  DICT[key] --> value
# {key1: value1, key2: value2, ...}


phone_book = {
    'ron': '111-1111',
    'bob': '2222-2222',
    'sam': '3333-3333'
    }

print(phone_book['sam'])
print(phone_book['bob'])
print(phone_book['ron'])


phone_book = {
    'ron': ['111-1111','aaa@abc.com'],
    'bob': ['2222-2222','bbb@bbb.com','only extra text'],
    'sam': ['3333-3333','ccc@ccc.com']
    }

print(phone_book['bob'][1])
print(phone_book['bob'][0])
print(phone_book['bob'][2])
