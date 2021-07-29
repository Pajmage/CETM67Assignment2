import requests
import json
import sys
import time
import random
import base64

# Installation:

# Create and activate a virtualenv
# pip install requests

# Example usage:

# python api_tester.py <url>

# python api_tester.py https://limitless-beyond-11781.herokuapp.com/

BASE_URL =  str(sys.argv[1]) # Gets the url as a command line argument
MAX_LOOP_COUNT = 100 # !IMPORTANT - This controls how many times you hit the URL Endpoint
CURRENT_LOOP_COUNT = 1
DELAY = 0
while CURRENT_LOOP_COUNT <= MAX_LOOP_COUNT:

    response = requests.post(
    BASE_URL + "/users/Bob", {"Employee_ID":"0002", "Forename":"Bob","Surname":"Bloggs", "Email":"bbloggs@dxc.com"})
#print(response.status_code)

    time.sleep(DELAY)

    response = requests.post(
    BASE_URL + "/users/John", {"Employee_ID":"0003", "Forename":"John","Surname":"Bloggs", "Email":"jbloggs@dxc.com"})
#print(response.status_code)

    time.sleep(DELAY)

    response = requests.post(
    BASE_URL + "/users/Sue", {"Employee_ID":"0004", "Forename":"Sue","Surname":"Bloggs", "Email":"sbloggs@dxc.com"})
#print(response.status_code)

    time.sleep(DELAY)

    response = requests.post(
    BASE_URL + "/users/Nicola", {"Employee_ID":"0005", "Forename":"Nicola","Surname":"Bloggs", "Email":"nbloggs@dxc.com"})
#print(response.status_code)

    time.sleep(DELAY)

    with open("0001BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0001BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0001BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
#print(response.status_code)


    with open("0002BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0002BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0002BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
#print(response.status_code)


    with open("0003BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0003BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0003BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
#print(response.status_code)


    with open("0004BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0004BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0004BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
    #print(response.status_code)


    with open("0005BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0005BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0005BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
    #print(response.status_code)


    with open("0006BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0006BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0006BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
    #print(response.status_code)


    with open("0007BPSS.docx", "rb") as f: # opens the file in the same directory as the ms2_test.py file
        file_bytes = base64.b64encode(f.read()) # encodes the file to a binary filetype
    payload = {"name": "0007BPSS.docx","bucket" : "cetm67-sec-documents", "file": file_bytes.decode("utf-8"),"Employee_ID":"0001", "Forename":"Paul","Surname":"Jones", "Email":"pjones98@dxc.com"} # construct the payload to send to the API call, including the encoded file
    response = requests.post(BASE_URL + "/file/0007BPSS.docx", data = json.dumps(payload), headers = {"Content-type": "application/json"})
    #print(response.status_code)



    # Issue a GET request to display all users in the database
    response = requests.get(BASE_URL + "/users/all")
#        print(response.status_code)

        #time.sleep(DELAY)

# Issue a POST request to the API to resize the provided image from an S3 bucket using a Lambda Function
    response = requests.post(BASE_URL + "/image/TestPic.jpg")
    response = requests.post(BASE_URL + "/image/Test2.jpg")
#        print(response.status_code)

        #time.sleep(DELAY)

    response = requests.post(BASE_URL + "/securitycheck/0001")
    response = requests.post(BASE_URL + "/securitycheck/0001")
    response = requests.post(BASE_URL + "/securitycheck/0044")
    response = requests.post(BASE_URL + "/securitycheck/0001")
    response = requests.post(BASE_URL + "/securitycheck/0088")

    response = requests.get(BASE_URL + "/file/0002BPSS.docx")
    rawfiledata = response.json() # dump the contents of the response json into a variable
    filedata = base64.b64decode(rawfiledata["body"]) # pull out the encoded binary file from the response and decode it back into its correct type
    filename = "DOWNLOAD_0002BPSS.docx" # set the filename to store the downloaded file as
    with open(filename, "wb") as f: # open the file now stored in the variable
        f.write(filedata) # write the file to the users computer using the set filename

        
    CURRENT_LOOP_COUNT += 1
