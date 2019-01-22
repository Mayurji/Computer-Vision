import json
import os
from collections import defaultdict
videoContent = defaultdict(list)
text_content = defaultdict(list)
files_folder = '/Users/mayurjain/Documents/video_to_document/'
def read_json(files_folder):
    count = 0
    for file in os.listdir(files_folder):
        if file.endswith('.json'):
            #count +=1
            print(file)
            with open(file) as jsonFile:
                jsonFile = json.load(jsonFile)
                #videoContent.append("Start")
                if jsonFile['textAnnotations'][0]['description'] not in videoContent:
                    videoContent[str(jsonFile['textAnnotations'][0]['description'][0:10])].append(len(jsonFile['textAnnotations'][0]['description']))
                    text_content[str(jsonFile['textAnnotations'][0]['description'][0:10])].append(jsonFile['textAnnotations'][0]['description'])
                    
    for k,v in videoContent.items():
        indexValue = videoContent[k].index(max(v))
        print(text_content[k][indexValue])     

    return videoContent

print(read_json(files_folder))

#videoContent.append(jsonFile['textAnnotations'][0]['description'][0:10])
#if jsonFile['textAnnotations'][0]['description'][0:10] == videoContent:
#print(len(jsonFile['textAnnotations'][0]['description']))
#print(videoContent.append(len(jsonFile['textAnnotations'][0]['description'])))
#print('\n')
#videoContent.append(jsonFile['textAnnotations'][0]['description'].split('\n'))