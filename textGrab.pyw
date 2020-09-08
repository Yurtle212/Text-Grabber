import pytesseract
import tkinter as tk
from tkinter.filedialog import askopenfilename

try:
    from PIL import Image
except ImportError:
    import Image

window = tk.Tk()
window.title('OCR')

buttonFile = tk.Button(text="Select File")
buttonFile.pack()

file = tk.StringVar()
file.set("Null")
fileLabel = tk.Label(textvariable=file)
fileLabel.pack()

button = tk.Button(text="Go")
button.pack()

outputLabel = tk.Label(text="Output:")
outputLabel.pack()
textBox = tk.Text()
textBox.pack()

img = " "

pytesseract.pytesseract.tesseract_cmd = r'Tesseract\Tesseract\tesseract.exe'

def onGo(event):
    #img = input("Enter path to file: ")
    #img = entry.get()
    
    textBox.delete("1.0", tk.END)
    textBox.insert("1.0", pytesseract.image_to_string(Image.open(img)))
    
    #print(pytesseract.image_to_string(Image.open(img)))
def chooseFile(event):
    global img
    img = askopenfilename()
    file.set(img)

buttonFile.bind("<Button-1>", chooseFile)
button.bind("<Button-1>", onGo)
window.mainloop()
