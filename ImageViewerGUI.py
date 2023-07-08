from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import OptionMenu
from tkinter import ttk
import numpy as np
import cv2
import os

tex = ""
origimg = None

def fileClick(clicked, captioner, classifier):
    # Define the function you want to call when the file browser button (Open) is clicked.
    # This function should pop up a dialog for the user to select an input image file.
    # To have a better clarity, please check out the sample video.
    # Allowing only jpg type file selection
    imgTypes = [('jpg Images', '*.jpg')]
    # File Dialog
    global imgName  # will use this for checking a condition in process(), so declaring globally
    imgName = filedialog.askopenfilename(title='Select Image', initialdir='data/img/', filetypes=imgTypes)
    if len(imgName) == 0:  # If no image is selected
        return
    # deleting previously written text in Entry widget
    e.delete(0, END)
    # writing name of current image, Assuming images are numbered from 0-9(single digit)
    e.insert(0, "Image: " + imgName[-5:])
    global output
    output = 'data/imgs/' + imgName[-5:]

    # Getting the predictions from the caption generator
    global captions
    global classification
    captions = str(captioner(output, 3))
    classification = str(classifier(output, 3))
    global origimg
    origimg = Image.open(imgName)
    # Adjust image size to fit the window
    origimg.thumbnail((500, 500))
    # Converting to Tkinter Images
    origimg = ImageTk.PhotoImage(origimg)
    panelorigimg.config(image=origimg)
    panelorigimg.image = origimg

def process(clicked):
    # This function will produce the required output when the 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.
    try:
        if len(imgName) == 0:
            print("Choose an image first!")
    except:
        print("Choose an image first!")
        return
    global tex

    if clicked.get() == "Image Captioning":  # If segmentation is chosen from the drop-down
        l.config(text=captions, font=("Courier", 14), fg="blue")  # Adding blue color to the text
    else:  # If bounded-box is chosen from the drop-down
        l.config(text=classification, font=("Courier", 14), fg="green")  # Adding green color to the text

if __name__ == '__main__':
    # Complete the main function preferably in this order:
    # Instantiate the root window
    root = Tk()
    # Provide a title to the root window.
    root.title("Shivam Sourav's Assignment Window")
    root.configure(bg="light yellow")  # Adding light yellow background color to the window

    # Instantiate the captioner and classifier models.
    captioner = ImageCaptioningModel()
    classifier = ImageClassificationModel()

    # Declare the file browsing button.
    options = ["Image Captioning", "Image Classification"]
    clicked = StringVar()
    clicked.set(options[0])

    e = Entry(root, width=70)
    e.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    fileButton = Button(root, text="Choose Image", command=partial(fileClick, clicked, captioner, classifier),
                        bg="light blue", fg="black")  # Adding light blue background color and black text color
    fileButton.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # Aligning the button to the left

    l = Label(root, text="")
    l.config(font=("Courier", 14), pady=20, wraplength=500)
    l.grid(row=3, column=0, sticky="w")

    panelorigimg = Label(root, image="", relief="solid", borderwidth=2)
    panelorigimg.grid(row=2, column=0, padx=10, pady=10, sticky="w")  # Aligning the image box to the left

    # Declare the drop-down button.
    dropDown = OptionMenu(root, clicked, *options)
    dropDown.config(bg="light green", fg="black")  # Adding light green background color and black text color
    dropDown.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    # Declare the process button.
    myButton = Button(root, text="Process", padx=10, command=partial(process, clicked),
                      bg="orange", fg="white")  # Adding orange background color and white text color
    myButton.grid(row=1, column=1, padx=10, pady=10, sticky="w")  # Aligning the button to the left

    # Declare the output label.
    root.mainloop()
