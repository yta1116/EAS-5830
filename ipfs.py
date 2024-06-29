import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# Convert the dictionary to JSON
  json_data = json.dumps(data)

  # Define the headers and URL for Pinata API
  headers = {
    "Authorization": "Bearer 4d893dd87a50c3236bf0",
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
