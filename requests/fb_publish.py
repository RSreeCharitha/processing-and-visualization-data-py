import os
import json
import requests

class Facebook:
    @staticmethod
    def get_access_token(token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()

        return 'Not found'

    def __init__(self):
        self.page_id = Facebook.get_access_token('FACEBOOK_PAGE_ID')
        self.page_access_token = Facebook.get_access_token('FACEBOOK_PAGE_ACCESS_TOKEN')

    # Tasks:
    # 1) Complete the publish_photo_msg() function.
    #    - This function should publish a post with the given message and photo.
    #    - The post should be published to the QEats Facebook Page.
    #
    # 2) Don't hardcode any values.
    #    - Our assessment servers might use your `publish_photo_msg` function
    #      to post to a different FB page.
    #    - If you hardcode the page ID or access token, the assessment might
    #      fail.
    #    - Tip: use self.page_id and self.page_access_token
    #
    # 3) Wondering which Facebook REST API endpoint to use? Check this:
    #    - https://developers.facebook.com/docs/graph-api/reference/page/photos/#publish
    # 
    # 4) Want to learn more about making HTTP API requests using Python?
    #    - https://forum.crio.do/t/how-can-i-make-http-requests-using-python/12659

    # Parameters
    # ----------
    # message : string (message to be posted)
    # image_url : string (publicly accessible URL of the image to be posted)
    # Return Type: None
    
    def publish_photo_msg(self, message, image_url):
        # write your code here
        data = {
            'url': image_url,
            'message': message,
            'published': 'true',
            'access_token': self.page_access_token
        }
        response = requests.post('https://graph.facebook.com/'+self.page_id+'/photos', data=data)
        print(response.status_code)
        return None

if __name__ == '__main__':
    facebook = Facebook()

    # Tasks:
    # 1) Search for your favorite ice-cream picture on images.google.com
    # 2) Copy the URL of the image and assign it to the 'image_url' variable
    #    Eg: image_url = 'https://assetsds.cdnedge.bluemix.net/sites/default/files/styles/very_big_1/public/feature/images/ice_cream_1.jpg'
    # 3) Set the 'my_name' variable to your name so you can identify your posts.
    
    image_url = 'https://res.cloudinary.com/grohealth/image/upload/$wpsize_!_cld_full!,w_2560,h_1770,c_scale/v1588091874/iStock-180258510-scaled.jpg'
    my_name = 'Charitha'

    message = my_name + ' likes burgers but they\'re not healthy'
    facebook.publish_photo_msg(message, image_url)
