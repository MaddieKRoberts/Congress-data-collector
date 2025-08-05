import requests

n = 949
m = 99
o = 9


for k in range(o):
	url = "https://clerk.house.gov/evs/2011/roll00{}.xml".format(k)
	local_filename = "2011houseroll00{}.xml".format(k)

	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()
	
		with open(local_filename, 'wb') as f:
			for chunk in response.iter_content(chunk_size=8192):
				f.write(chunk)
		print(f"file '{local_filename}' downloaded successfully.")
			
	except requests.exceptions.RequestException as e:
		print (f"Error downloading file: {e}")




for j in range(m):
	url = "https://clerk.house.gov/evs/2011/roll0{}.xml".format(j)
	local_filename = "2011houseroll0{}.xml".format(j)

	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()
	
		with open(local_filename, 'wb') as f:
			for chunk in response.iter_content(chunk_size=8192):
				f.write(chunk)
		print(f"file '{local_filename}' downloaded successfully.")
			
	except requests.exceptions.RequestException as e:
		print (f"Error downloading file: {e}")
	




for i in range(n):
	url = "https://clerk.house.gov/evs/2011/roll{}.xml".format(i)
	local_filename = "2011houseroll{}.xml".format(i)

	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()
	
		with open(local_filename, 'wb') as f:
			for chunk in response.iter_content(chunk_size=8192):
				f.write(chunk)
		print(f"file '{local_filename}' downloaded successfully.")
			
	except requests.exceptions.RequestException as e:
		print (f"Error downloading file: {e}")
	
	