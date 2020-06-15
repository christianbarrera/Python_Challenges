from bs4 import BeautifulSoup
# Use a locally saved html file, but I'm sure you can make a live request.  
f = open("my_meter_details.html", encoding='utf-8')
file = f.read()

# Creates a BeautifulSoup instance, indicating type.  
soup = BeautifulSoup(file, 'html.parser')
# Make an object by defining the desired class tab. 
div = soup.find('div', {'class': 'module-body sa-info'})
print(type(div))
i = 0
# What does this while loop do? 
while "Service ID:" not in div.find_all('li')[i].text.strip():
	value = div.find_all('li')[i]
	# Replace new lines and double spaces to look clean. 
	print(value.text.strip().replace("\n", " ").replace("  ", ""))
	i += 1

# Rates var finds the div tab defined by class and style.
rates = soup.find('div', {'class': 'module-body', 'style': 'padding-bottom: 60px;'})
# print out the text of the <h3></h3> element. 
print("\n" + rates.find('h3').text.strip())