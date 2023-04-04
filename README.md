# Text-Editor-Program-With-Python-TKINTER

This code is a program that creates a GUI (graphical user interface) with
two different programs. The first program is a word counter, in which the
user can enter a paragraph or any text into the input box, and by utlising
the button operations provided, he can press Count Words, this will count
the total number of words entered, and also provide an ouput box beneath
with a list containing the count of each specific word , and similarly
provide a dialog box with this output as well. By entering a searchword
into the input box, the user can also press the Search Word operation
button, this will provide an output telling whether that specific word is
present in the text or not.
The second program is a text file editor, in which the user can make use
of the Open operation button, which will provide an interactive file
explorer dashboard, in which only text files will be present, on choosing a
text file to open, the text in that file will be outputted in the text box
above. The user can then make any changes he wants, add new text,
remove text, change length, and make edits. Further the user can use the
Save operation button to again be prompted with an interactive file
explorer dashboard , the user can save a textfile of whatever name he
chooses, or he may replace an existing textfile and override the save with
the text he has entered in the text box provided in the GUI program.

pg. 8
The GUI is using the TKINTER library and other modules related to
TKINTER, such as frames, file accessing, boxes, Titles, Logos,
RadioButtons, Interactive user entry boxes in which text can be entered to
be operated upon, scrollable textbox when large text files are opened in
the text editor box and many more features.
The program imports several modules from the tkinter library, including
the main module, messagebox, and filedialog. The program also imports
the ScrolledText module to create a scrolling text box.
The GUI window is created with the title "ProEditor," and the attribute "-
fullscreen" set to True, which means that the window will open in full
screen. The canvas is created with a gradient background and is packed
to fill the entire window.
The first program is located in the left frame of the canvas. It includes a
title label, an input label, and a text box for users to enter a paragraph. A
button labeled "Count Words" is also present to count the total number of
words and frequency of each word in the paragraph.
pg. 9
A search box and search button are also present to search for a specific
word in the paragraph. An output label is included to display the results
of the word count and frequency or search.
pg. 10
The second program is located in the right frame of the canvas. It
includes a title label, an input label, and a text box for users to input or
edit text. Buttons labeled "Open File," "Save File," and "Clear Text" are also
present to perform actions on the text box.
pg. 11
Another scrolling text box is also present to display the contents of a
selected file.
Overall, the code creates a user-friendly interface for users to perform
word counting, frequency checking, text editing, and file manipulation. 
