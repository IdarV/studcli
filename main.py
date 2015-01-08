from splinter import Browser
browser = Browser('firefox')

browser.visit('https://www.studweb.no/as/WebObjects/studentweb2?inst=FSWACT')
browser.fill('fodselsnr', 'xxxxxxxxxxx')
browser.fill('pinkode', 'xxxx')
browser.find_by_name('login').first.click()

browser.click_link_by_href('/as/WebObjects/studentweb2.woa/wo/0.0.23.24.6.4.1.1')
browser.click_link_by_href('/as/WebObjects/studentweb2.woa/wo/2.0.23.24.6.6.1.1')

tags = browser.find_by_tag('tr')

chars = []

for tag in tags:
	if tag.outer_html.startswith('<tr class='):
		cells = tag.find_by_tag('td')
		
		if cells[2].text != "":
			print cells[1].text + '\t' + cells[2].text

		print '\t' + cells[7].text + '\t' + cells[4].text,
		if cells[3].text != "":
			print "(" + cells[3].text + ")",
		else:
			print "",

		if cells[8].text != "":
			print "*"
			if cells[7].text != 'Passed':
				chars.append(cells[7].text)
		else:
			print ""

total = 0.0
for char in chars:
	if char == 'A':
		total += 6
	if char == 'B':
		total += 5
	if char == 'C':
		total += 4

finalChar = total/len(chars)

print '----------------------------------'
print 'Din naavaerende karakter er: ' + str(finalChar)
print '----------------------------------'

browser.quit()