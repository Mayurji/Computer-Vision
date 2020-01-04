### Image Captioning

Image Captioning is one of the biggest challenges in Computer Vision, as it revolves around a couple of crucial ideas.
First, understanding the image and then secondly, presenting it through utterances like humans do. The idea is a CNN-RNN model, where CNN is considered as Encoder of the network, while the RNN is considered as Decoder of the Network.

### Understanding COCO Dataset

The dataset consists of train2014, val2014 and test2014. Both the train2014 and val2014 folder contains images, annotations,
Person Keypoints, Captions etc. Each image has 5 captions mapped to it. For more details, check the url below

**Dataset URL** http://cocodataset.org/#download

#### Note
    There are some inherent issue with images in train2014. So i have developed a script "missingFile_cocodataset", 
    which will clear the image details which are mapped to images, which are not present in train2014.

### Models:

  **To understand and extract feature of the image, we use pretrained, ResNet model for extracting the feature. (Try different models if required.)**
  
  **The captions are tokenized using NLTK, and then a vocabulary is created. Each caption is turned into word embedding.
  Word Embedding along with Image Feature acts as input size to the RNN.**
