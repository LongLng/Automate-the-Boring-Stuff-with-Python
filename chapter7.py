import re

def date_detection():
    dateRegex = re.compile(r'''(
		(3[01]|[12][0-9]|0?[1-9])
		
        )''')