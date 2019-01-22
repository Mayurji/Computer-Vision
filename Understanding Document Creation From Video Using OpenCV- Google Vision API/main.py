from os import makedirs
from os.path import join, basename
#from sys import argv
import sys
sys.path.append('/ Users/mayurjain/anaconda/lib/python3.6/site-packages')
import cv2
import time
import numpy as np
from PIL import Image
from google_vision_code import request_ocr,json
from read_json import read_json

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
api_key = 'AIzaSyB2CKjo7MJAD8Mv10rG7kZdzRNn2dQWS6U'
RESULTS_DIR = '/Users/mayurjain/Documents/video_to_document'
vidcap = cv2.VideoCapture('/Users/mayurjain/Documents/video_to_document/59seconds.mp4')
print(vidcap.get(cv2.CAP_PROP_FPS))
makedirs(RESULTS_DIR, exist_ok=True)
request_list = []
count = 0
total_frames = 1800 # 60 seconds video and 30 fps i.e. 1800 frames in 60 seconds
fetch_frame = 2500 # 2000 ms capture frame after every 2 seconds
success = 600
'''
while success != 0:
    vidcap.set(0, fetch_frame*(count+1))
    success, image = vidcap.read()
    print(success)
    cv2.imwrite(RESULTS_DIR+"/frame"+str(count)+".jpg", image)
    response = request_ocr(api_key, RESULTS_DIR+'/frame'+str(count)+'.jpg')
    print("response generated")
    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
        break
    else:
        for idx, resp in enumerate(response.json()['responses']):
            # save to JSON file
            image_filenames = ["frame"]
            imgname = image_filenames[idx]
            jpath = join(RESULTS_DIR, basename(imgname)+str(count) + '.json')
            with open(jpath, 'w') as f:
                datatxt = json.dumps(resp, indent=2)
                print("Wrote", len(datatxt), "bytes to", jpath)
                f.write(datatxt)
                #print(read_json(jpath))
                count += 1
                #time.sleep(10)
                
    success -= 60
    
'''

