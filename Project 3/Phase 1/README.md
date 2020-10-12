Phase 3 is to Install or Run the Open Source Project, also reproduce the results.
My project is VQA, I choose to do the Tensorflow 2 Detection Model Zoo, as my teammates choose the Word-level language modeling RNN.
Here is the github link. https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md.
This model needs to be run under TensorFlow2.2 and Python 3.6.
Since, I already have python 3.8, so first, I install the TensorFlow with pip. Here is the instruction link.
https://www.tensorflow.org/install/pip#windows.
I suppose to create a new virtual environment by choosing a Python interpreter and making a .\venv directory to hold it, and activate the virtual environment.
But it is not working on Windows Powershell.
So I press WindowsKey + R, and type cmd when the box comes up, it brings up the command line interface instead of powershell. Then I can install TensorFlow in it.

From COCO website, We can easily find their Dataset. 
From the dataset, we can find the github link: github.com/cocodataset/cocoapi 
COCO is a large image dataset designed for object detection, segmentation, person keypoints detection, stuff segmentation, and caption generation. This package provides Matlab, Python, and Lua APIs that assists in loading, parsing, and visualizing the annotations in COCO.
We can use the Python API. We need to download both the COCO images and annotations in order to run the demos and use the API.
Download, unzip, and place the images in: coco/images/
Download and place the annotations in: coco/annotations/
After downloading the images and annotations,  run the Pytho, "make" under coco/PythonAPI, for example usage. 
