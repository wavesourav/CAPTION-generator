# CAPTION-generator
This is a caption generator and image classifier software
#CAPTION GENERATOR AND IMAGE CLASSIFIER SOFTWARE

## Python GUI caption-classification (tkinter)
 GUI using `tkinter` which would have the following overall functionality:

* The GUI would provide the user to select a file from the computer.
* It will have a dropdown menu to toggle between two output options: `Image Captioning` and `Image Classification`
* If `Image Captioning` is selected then it should show the caption for the selected image file along with the original image file side-by-side.
* For `Image Classification` it should display the classification class instead of the captions.
* We will obtain the captions by taking help from the previous assignment (which you have already done).
* While for classification, we use Image Classification Model (updated in model.py)

## Installation procedure 
* Note: To install the dependencies you need to run the following commands:

* pip install -r requirements.txt
* python3 -m spacy download en_core_web_sm
* Download LAVIS zip into the project directory from https://github.com/salesforce/LAVIS, Unzip LAVIS-main.zip and install lavis using the following commands
cd LAVIS-main/
* pip install .

* then install tkinter and functools.

and you are ready to go

