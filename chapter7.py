import re,pyperclip

#Date Detection

def date_detection():

	dateRegex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9]{3})')        

	text = str(pyperclip.paste())
	monthsWitch30Days = ['04', '06', '09', '11']
	date19 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	matches= []

	for dayMonthYear in dateRegex.findall(text):
		valid = True
		
		date = {'day':1, 'month':2, 'year':3}
		for k, v in date.items():
			date[k] = dayMonthYear[v]
		
		if date['day'] in date19:
			date['day'] = '0' + date['day']
		if date['month'] in date19:
			date['month'] = '0' + date['month']

		if date['day'] in ['29', '30', '31']:
			if date['day'] == '29' and date['month'] == '02':
				if (int(date['year']) % 4 == 0 and \
					int(date['year']) % 100 != 0) or \
					(int(date['year']) % 400 == 0 and \
					int(date['year']) % 100 != 0):
					valid = True
				else:
					valid = False
			if date['day'] == '30' and date['month'] != '02':
				if date['month'] in monthsWitch30Days:
					valid = True
				else:
					valid = False
			if date['day'] == '31' and date['month'] != '02':
				if date['month'] not in monthsWitch30Days:
					valid = True
				else:
					valid = False       
		
		if valid:
			matches.append(date)

	print(matches)
        

#Strong Password Detection
length_regex = re.compile('.{8,}')
lower_case_regex = re.compile('[a-z]+')
upper_case_regex = re.compile('[A-Z]+')
digit_regex = re.compile('[\d]+')
regex_list = [length_regex,
              lower_case_regex,
              upper_case_regex,
              digit_regex]
def strong_password(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print('Not Strong')
            break
        else:
            regex_count =+ 1
            continue
    if regex_count == 4:
        print('Nice')
    
if __name__=='__main__':
    pw = input('Type Pass:')
    
    strong_password(pw)