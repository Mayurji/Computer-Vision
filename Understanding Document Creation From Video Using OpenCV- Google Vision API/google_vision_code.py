import base64
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
api_key = 'AIzaSyB2CKjo7MJAD8Mv10rG7kZdzRNn2dQWS6U'
    
def make_image_data_list(image_filenames):
    """
    image_filenames is a list of filename strings
    Returns a list of dicts formatted as the Vision API
        needs them to be
    """
    img_requests = []
    with open(image_filenames, 'rb') as f:
        ctxt = base64.b64encode(f.read()).decode()
        img_requests.append({
            'image': {'content': ctxt},
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1
            }]
        })
    return img_requests


def make_image_data(image_filenames):
    """Returns the image data lists as bytes"""
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({"requests": imgdict}).encode()


def request_ocr(api_key, image_filenames):
    response = requests.post(ENDPOINT_URL,
                             data=make_image_data(image_filenames),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})
    return response
