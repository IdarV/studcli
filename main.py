from ConfigParser import SafeConfigParser
from splinter import Browser


parser = SafeConfigParser()
parser.read('config.ini')

browser = Browser(parser.get('Config', 'Browser'))
browser.driver.maximize_window()

browser.visit('https://fsweb.no/studentweb/login.jsf?inst=' +  parser.get('Config', 'Institution'))
browser.find_by_text('Norwegian ID number and PIN').first.click()

browser.find_by_id('login-box')
browser.fill('j_idt129:j_idt131:fodselsnummer', parser.get('Config', 'Fodselsnummer'))
browser.fill('j_idt129:j_idt131:pincode',  parser.get('Config', 'Pin'))
browser.find_by_text('Log in').first.click()

browser.click_link_by_href('/studentweb/resultater.jsf')

tags = browser.find_by_tag('tr')

chars = []

for tag in tags:
	if tag.has_class('resultatTop') or tag.has_class('none'):
		inner_tags = tag.find_by_tag('td')
		course_id = inner_tags[1].text.split("\n")[0]
		course_name = inner_tags[1].text.split("\n")[1]
		grade = inner_tags[5].text
		if grade != 'Passed':
			chars.append(grade) 
			print "%s\t%-30s\t%s" % (course_id, course_name, grade)

total = 0.0
for char in chars:
	if char == 'A':
		total += 6
	elif char == 'B':
		total += 5
	elif char == 'C':
		total += 4
	elif char == 'D':
		total += 3
	elif char == 'E':
		total += 2
	elif char == 'F':
		total += 1



finalChar = total/len(chars)

print ('----------------------------------')
print ('Din naavaerende karakter er: ' + str(finalChar))
print ('----------------------------------')

browser.cookies.delete()
browser.quit()
