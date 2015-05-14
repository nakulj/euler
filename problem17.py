units = [
	'zero', 'one', 'two', 'three', 'four',
	'five', 'six', 'seven', 'eight', 'nine'
]

teens = [
	'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
	'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
	
tens = [
	'ten', 'twenty', 'thirty', 'forty', 'fifty',
	'sixty', 'seventy', 'eighty', 'ninety'
]

hundred = 'hundred'
thousand = 'thousand'

def toWords(n):
	if n < 10:
		return units[n]
	if 10 < n < 20:
		return teens[n%10 - 1]
	if n < 100:
		if n%10 == 0:
			return tens[n/10 - 1]
		return tens[n/10 - 1] + units[n%10]
	if n<1000:
		if n%100 == 0:
			return units[n//100] + hundred
		return (units[n//100] + hundred) + 'and' + toWords(n%100)
	return 'onethousand'

print sum(len(toWords(i)) for i in range(1, 1001))
