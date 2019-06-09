import requests
import json

subscription_key = '9fe3851819be4386aa5cd4566d34a4a6'
assert subscription_key

face_api_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'

#newImage = input("Please input image URL: ")

image_url = "https://media.licdn.com/dms/image/C4D03AQFRZU2NnHGICw/profile-displayphoto-shrink_200_200/0?e=1565222400&v=beta&t=ScEBVnvOpx0pe8yFPj3gwTlB97vgJ5RSqcs6NWYGwTE"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
print("Detection result:")
#print(json.dumps(response.json()))
text = json.dumps(response.json())

allWords = text.split(",")

for i in allWords:
    print(i)
