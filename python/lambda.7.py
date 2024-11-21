numbers=[5,10,15,20,24,30]

odd_numbers=filter(lambda x: x%5!=0,numbers)

print(list(odd_numbers))