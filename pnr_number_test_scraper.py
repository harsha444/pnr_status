
import bs4
import requests

for i in range(6411078143, 6411078190):
	res = requests.get('http://www.railyatri.in/pnr-status/' + str(i))
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	# print(soup)
	booked_time_stats = []
	current_stats = []
	temp_booked = soup.select('#status > div:nth-of-type(2) > div:nth-of-type(1) > p')
	temp_current = soup.select('#status > div:nth-of-type(2) > div:nth-of-type(2) > p')
	if(len(temp_booked) != 0):
		with open("test_pnr.txt", "a") as myFile:
			myFile.write(str(i) + '\n')