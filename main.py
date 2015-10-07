from ConfigParser import SafeConfigParser
from splinter import Browser


parser = SafeConfigParser()
parser.read('config.ini')

browser = Browser('phantomjs')
browser.cookies.delete()
browser.driver.set_window_size(1920,1080)

browser.visit('http://fsweb.no/studentweb/login.jsf?inst=FSWACT') 
browser.find_by_xpath("//div[@id='login-box']/div[@id='login-flaps']/div[@class='login-flap login-name-pin']").click()

browser.fill('j_idt129:j_idt131:fodselsnummer', parser.get('Config', 'Fodselsnummer'))
browser.fill('j_idt129:j_idt131:pincode',  parser.get('Config', 'Pin'))

browser.find_by_xpath("//button[@id='j_idt129:j_idt131:login']").click()
browser.find_by_xpath("//nav[@id='menuBarLeft']/ul[@class='mainmenu']/li/a[@title='Resultater']").click()

grades = []
tags = browser.find_by_tag('tr')

for tag in tags:
	if tag.has_class('resultatTop') or tag.has_class('none'):
		inner_tags = tag.find_by_tag('td')
		course_id = inner_tags[1].text.split("\n")[0]
		course_name = inner_tags[1].text.split("\n")[1]
		grade = inner_tags[5].text
		if grade != 'Passed':
			grades.append(grade) 
			print "%s\t%-30s\t%s" % (course_id, course_name, grade)

total = 0.0
for char in grades:
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



finalChar = total/len(grades)

print ('----------------------------------')
print ('Din naavaerende karakter er: ' + str(finalChar))
print ('----------------------------------')

browser.cookies.delete()
browser.quit()
