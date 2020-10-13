import json
import requests

# Complete the get_tags_suggestions() function
# Tasks:
# 1) You need to register as Clarifai developer to obtain an API Key to the Food Model
#    The Food model can be found here:https://github.com/RSreeCharitha/python-specialization-coursera
#    https://www.clarifai.com/models/food-image-recognition-model-bd367be194cf45149e75f01d59f77ba7
#    A sample request and response can be found in the above link
# 2) Use the food model to get implement tag suggestions

# Parameters
# ----------
# api_key : string
#     API Key for Clarifai
# image_url : string
#     publicly accessible URL of the image to get tag suggestions
# Return Type: list()
#   return a list of tags provided by the Clarifai API
def get_tags_suggestions(api_key, image_url):
    headers = {'Authorization': 'Key '+api_key,'Content-Type': 'application/json'}

    data = '{"inputs": [{"data": {"image": {"url": \"'+image_url+'\" }}}]}'
    #print(data)
    response = requests.post('https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs', headers=headers, data=data)
    print(response.status_code)

    l = []
    info = json.loads(response.text)
    n = (len(info['outputs'][0]['data']['concepts']))
    for i in range(n):
        l.append(info['outputs'][0]['data']['concepts'][i]['name'])
    
    return l

def get_access_token(token_name):
    file_handle = open('access_tokens.sh', 'r+')
    lines = file_handle.readlines()
    file_handle.close()
    for line in lines:
        tokens = line.strip().split('=')
        if tokens[0] == token_name:
            return tokens[1].strip()
    return 'Not found'

if __name__ == '__main__':
    clarify_api_key = get_access_token('CLARIFAI_API_KEY')
    test_image_url = 'https://i.imgur.com/dlMjqQe.jpg'
    tags_suggessted = get_tags_suggestions(clarify_api_key, test_image_url)
    print(tags_suggessted)