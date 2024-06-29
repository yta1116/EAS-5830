import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# Convert the dictionary to JSON
	json_data = json.dumps(data)

	# Define the headers and URL for Pinata API
	headers = {
		"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJkMDcyMDBiYi04ODU0LTQwZmUtOTVlZS0wOWVkOWUxZTUxYzYiLCJlbWFpbCI6Inl1bmZlaXRhQGJlcmtlbGV5LmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiRlJBMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfSx7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJmYTliNWE0NThlNmJjOTExNTAyNSIsInNjb3BlZEtleVNlY3JldCI6ImRlOGU1ODZlYjVhZDk0YzcwNzM5ZTg1NGRlODI2ODM3NGM1MmQ4N2NlODFkNzcwN2QwYmZlZjA0Y2RkNWY3NDQiLCJpYXQiOjE3MTk2OTIwMDZ9.2hU0DVUAprCs-HgVghLzhxVdN3u8YTjwowaVD_XK6VE",
		"Content-Type": "application/json"
	}
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
	# Send the request to Pinata
	response = requests.request("POST", url, json=json_data, headers=headers)
    
	# Check if the request was successful
	if response.status_code == 200:
		# Extract and return the CID
		return response.json()["IpfsHash"]
	else:
		# Raise an error with the response text
		response.raise_for_status()

	#return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
