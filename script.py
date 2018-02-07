# import urllib.request
# import urllib.parse
# # import urllib2
# pnr_number = input("Enter the pnr number: ")
# url = 'http://www.railyatri.in/pnr-status/' + pnr_number
# # URL test
# # print(url)
# req = urllib.request.Request(url)
# resp = urllib.request.urlopen(req)
# resp_data = resp.read()
#
# print(resp_data)
import bs4
import requests
pnr_number = input("Enter the pnr number: ")
res = requests.get('http://www.railyatri.in/pnr-status/' + str(pnr_number))
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup)
booked_time_stats = []
current_stats = []
i=2
# To check the status at the booking time
while(1):
	# temp_booked = soup.select('#result > ul > table:nth-of-type(2)  > tr:nth-of-type('+str(i)+') > td:nth-of-type(2)')
	# temp_current = soup.select('#result > ul > table:nth-of-type(2)  > tr:nth-of-type('+str(i)+') > td:nth-of-type(3)')
	temp_booked = soup.select('#status > div:nth-of-type('+str(i)+') > div:nth-of-type(1) > p')
	temp_current = soup.select('#status > div:nth-of-type('+str(i)+') > div:nth-of-type(2) > p')
	if(temp_booked != []):
		booked_time_stats.append(temp_booked[0].text.strip())
		current_stats.append(temp_current[0].text.strip())
		i+=1
	else:
		break

# If pnr nummber is invalid
if(booked_time_stats == []):
	print("Enter a valid pnr number")
for i in range(len(booked_time_stats)):
	print('Passenger '+str(i+1)+' booking time status : ' + booked_time_stats[i] + ' and current status: ' + current_stats[i])