import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	
	# Convert the dictionary to JSON
	#json_data = json.dumps(data, indent=4)

	# Define the headers and URL for Pinata API
	headers = {
		"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJkMDcyMDBiYi04ODU0LTQwZmUtOTVlZS0wOWVkOWUxZTUxYzYiLCJlbWFpbCI6Inl1bmZlaXRhQGJlcmtlbGV5LmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJjZDUxZDA1ZmMxZTM4ZDVhYTRhNSIsInNjb3BlZEtleVNlY3JldCI6ImEzZDVjMTlkYTA1MzQ2ZmFhYTllM2VjOWQyMTBjNzRlZmU5ZDM3MWE5MDgxZmZkN2ZkZDE2MTVlN2RlZmE2ZDkiLCJleHAiOjE3NTEyMjg2MjZ9.gm_4cz2VXiY7KGXBxTyqRLbOEstoEgfsfH0vn-ZcP1M",
		"Content-Type": "application/json"
	}
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
	# Send the request to Pinata
	response = requests.request("POST", url, json=data, headers=headers)
    
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
