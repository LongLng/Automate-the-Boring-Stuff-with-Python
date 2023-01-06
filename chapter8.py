import pyinputplus as pyip, re


prices = {'wheat': 2, 'white': 1, 'sour dough': 3, 'chicken': 2, 'turkey': 3, 'ham': 2, 'tofu': 1,
          'cheddar': 1, 'swiss': 2, 'mozzarella': 3, 'mayo': 1, 'mustard': 1, 'lettuce': 1,
          'ketchup': 1}

while True:
    bread=[]
    bread.append(pyip.inputMenu(['wheat','white','sour dough'],prompt='What type of bread would you like ? \n* WHITE \n* BROWN \n* SOURDOUGH \n',numbered=True))
    bread.append(pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt='What type of bread would you like ? \n* CHICKEN \n* TURKEY \n* HAM \n* TOFU \n',numbered=True))
    if pyip.inputYesNo('Do you want Cheese in your sandwich?(Y/N)\n')== 'yes':
        bread.append(pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True))
    if pyip.inputYesNo('Do you want mayo?(Y/N) \n') == 'yes':
        bread.append('mayo')
    if pyip.inputYesNo('Do you want mustard?(Y/N) \n') == 'yes':
        bread.append('mustard')
    if pyip.inputYesNo('Do you want lettuce?(Y/N) \n') == 'yes':
        bread.append('lettuce')
    if pyip.inputYesNo('Do you want tomato ketchup?(Y/N) \n') == 'yes':
        bread.append('ketchup')
        
    quantity = pyip.inputInt('How much sandwiches you would like to order?\n',
                              allowRegexes=['^[0-9]*$'])
    
    amount = 0
    print('Your Sandwich have:')
    for i in bread:
        price = prices[i]
        print(f'{i}')
        amount += price
        
    print(f'the amount you need to pay is:{amount} x{quantity} ={amount * quantity}')
    
    if pyip.inputYesNo('Confirm your Order (Y/N)\n') == 'yes':
        print('Thanks kiuu')
        break
        
    