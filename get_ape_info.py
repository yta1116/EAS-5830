from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
import requests
import json
import time

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_address = Web3.to_checksum_address(bayc_address)

#You will need the ABI to connect to the contract
#The file 'abi.json' has the ABI for the bored ape contract
#In general, you can get contract ABIs from etherscan
#https://api.etherscan.io/api?module=contract&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('/home/codio/workspace/abi.json', 'r') as f:
	abi = json.load(f) 

############################
#Connect to an Ethereum node
api_url = "https://eth-mainnet.g.alchemy.com/v2/tJGaOnSQCMic80c0V37Wj50-Sk0p-c5N" #YOU WILL NEED TO TO PROVIDE THE URL OF AN ETHEREUM NODE
provider = HTTPProvider(api_url)
web3 = Web3(provider)

def get_ape_info(apeID):
	assert isinstance(apeID,int), f"{apeID} is not an int"
	assert 1 <= apeID, f"{apeID} must be at least 1"

	data = {'owner': "", 'image': "", 'eyes': "" }
	
	#YOUR CODE HERE	
	contract = web3.eth.contract(address=contract_address, abi=abi)

	owner = contract.functions.ownerOf(apeID).call()
	data['owner'] = owner

	token_uri = contract.functions.tokenURI(apeID).call()
	substring = token_uri.split("//")[1]

	ipfs_gateway_url = f"https://gateway.pinata.cloud/ipfs/{substring}"

	response = requests.get(ipfs_gateway_url)
	if response.status_code == 200:
		metadata = response.json()
		data['image'] = metadata.get('image', '')

		# Fetch traits to find 'eyes'
		attributes = metadata.get('attributes', [])
		for attribute in attributes:
			if attribute.get('trait_type') == 'Eyes':
				data['eyes'] = attribute.get('value', '')

	assert isinstance(data,dict), f'get_ape_info{apeID} should return a dict' 
	assert all( [a in data.keys() for a in ['owner','image','eyes']] ), f"return value should include the keys 'owner','image' and 'eyes'"
	return data

