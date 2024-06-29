import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	api_key = "73feb8f6272c73bf972a"
	api_secret = "a6c1890d357fcec346491c20f439bcd292ee896155ea41151ba0610936a38c62"
	
	# Convert the dictionary to JSON
	json_data = json.dumps(data)

	# Define the headers and URL for Pinata API
	headers = {
		"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJkMDcyMDBiYi04ODU0LTQwZmUtOTVlZS0wOWVkOWUxZTUxYzYiLCJlbWFpbCI6Inl1bmZlaXRhQGJlcmtlbGV5LmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiI3M2ZlYjhmNjI3MmM3M2JmOTcyYSIsInNjb3BlZEtleVNlY3JldCI6ImE2YzE4OTBkMzU3ZmNlYzM0NjQ5MWMyMGY0MzliY2QyOTJlZTg5NjE1NWVhNDExNTFiYTA2MTA5MzZhMzhjNjIiLCJleHAiOjE3NTEyMjgxMTl9.w3EYpH4Ep4YH4HjKGUn1dbi_hPK-bA_FWWYAsq6v5KA",
		"Content-Type": "application/json"
	}
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
	# Send the request to Pinata
	response = requests.request("POST", url, json=json_data, headers=headers, auth=(api_key, api_secret))
    
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
