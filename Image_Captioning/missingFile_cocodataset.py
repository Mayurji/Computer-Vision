import json
import os
train_files = "/Users/mayurjain/cocoapi/images/train2014/"
instances_train = "/Users/mayurjain/cocoapi/annotations/instances_train2014.json"
captions_train = "/Users/mayurjain/cocoapi/annotations/captions_train2014.json"
person_KP_train = "/Users/mayurjain/cocoapi/annotations/person_keypoints_train2014.json"


"""
Annotations for Images are mapped based on Image Ids and Images names.
jpg_file_name  contains all file names present in train2014.
img_id_files contains all the file ids present in train2014
"""
jpg_file_name = []
img_id_files = []
for files in os.listdir(train_files):
    if files.endswith(".jpg"):
        jpg_file_name.append(files.strip(".jpg").split("_")[2])
        img_id_files.append(int(files.strip(".jpg").split("_")[2]))


"""
load_json - It loads the json files for processing.
"""

def load_json(file_name):
    with open(file_name) as json_file:
        jsonFile = json.load(json_file)
    return jsonFile


instances = load_json(instances_train)
captions = load_json(captions_train)
pkp = load_json(person_KP_train)

"""
file_names - There are some images files which are missing in train2014, but the filenames are mapped in "instances_train2014.json", "captions_train2014.json", 
"person_keypoints_train2014.json". So the method "file_names" will collect all the filenames under each json file as mentioned before.
"""

def file_names(json_file):
    filename = []
    for i in range(len(json_file["images"])):
        filename.append(json_file["images"][i]
                        ["file_name"].strip(".jpg").split("_")[2])
    
    return filename


"""
invalid_files_names - It takes all the image file names from train2014 folder and  file names mapped in json files. The method finds the invalid filenames, which are present 
in the json files but not present in train2014.
"""

def invalid_files_names(jpg_file_name, instances):
    invalid_file_name = []
    for i in instances:
        if i not in jpg_file_name:
            invalid_file_name.append("COCO_train2014_"+i+".jpg")
    
    return invalid_file_name

"""
pop_file_names - It takes invalid files names present in json file and remove that from the json file.
"""

def pop_file_names(invalidFiles,data):
    for file in invalidFiles:
        for i, fileName in enumerate(data["images"]):
            if fileName["file_name"] == file:
                data["images"].pop(i)
    return data


"""
img_ids - There are some images files which are missing in train2014, but the image id's are mapped in "instances_train2014.json", "captions_train2014.json", 
"person_keypoints_train2014.json" in annotations. So the method "img_ids" will collect all the image ids under each json file as mentioned before.
"""

def img_ids(json_file):
    img_ids = []
    for i in range(len(json_file["annotations"])):
        img_ids.append(json_file["annotations"][i]["image_id"])

    return img_ids


"""
invalid_img_ids - It takes all the image ids from train2014 folder and img_ids mapped in json files. The method finds the invalid image ids, which are present 
in the json files but not present in train2014.
"""

def invalid_img_ids(img_ids):
    img_invalid = []
    for i in img_ids:
        if i not in img_id_files:
            img_invalid.append(i)

    return img_invalid


"""
pop_img_ids - It takes invalid image ids present in json file and remove that from the json file.
"""

def pop_img_ids(img_ids,json_file):
    for file in img_id_files:
        for i, fileName in enumerate(json_file["annotations"]):
            if fileName["image_id"] == file:
                json_file["annotations"].pop(i)

    return json_file

def write_json(json_file):
    return open("/Users/mayurjain/cocoapi/annotations/instances_train2014.json", "w").write(json.dumps(data))

instances = file_names(instances)
invalid_files = invalid_files_names(jpg_file_name,instances)
instance_train = pop_file_names(invalid_files,instances)
caption_train = pop_file_names(invalid_files, captions)
pkp_train = pop_file_names(invalid_files, pkp)
instance_annotations_img_id = img_ids(instance_train)
caption_annotations_img_id = img_ids(caption_train)
pkp_annotations_img_id = img_ids(pkp_train)
inst_ann_invalidIds = invalid_img_ids(instance_annotations_img_id)
capt_ann_invalidIds = invalid_img_ids(caption_annotations_img_id)
pkp_ann_invalidIds = invalid_img_ids(pkp_annotations_img_id)
inst_json = pop_img_ids(inst_ann_invalidIds, instance_train)
capt_json = pop_img_ids(capt_ann_invalidIds,caption_train)
pkp_json = pop_img_ids(pkp_ann_invalidIds,pkp_train)
#write_json(inst_json)
#write_json(capt_json)
#write_json(pkp_json)
