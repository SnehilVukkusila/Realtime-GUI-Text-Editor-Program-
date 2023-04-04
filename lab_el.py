import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# Create the main window
root = tk.Tk()
root.title("ProEditor")
root.attributes("-fullscreen", True)

# Create the left frame for the first program
left_frame = tk.Frame(root, bg='gray10')
left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the title for the first program
title_left = tk.Label(left_frame, text='Word Counter', font=('Arial', 36), fg='sky blue', bg='gray10')
title_left.pack(pady=10)

# Create the input box for the paragraph
paragraph_input = tk.Text(left_frame, bg='gray30', fg='white', height=10)
paragraph_input.pack(pady=10)

# Create the button to count the words and frequency
def count_words():
    # Get the text from the input box
    text = paragraph_input.get("1.0", "end-1c")

    # Count the total number of words
    word_list = text.split()
    word_count = len(word_list)

    # Count the frequency of each word
    frequency_dict = {}
    for word in word_list:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    # Create a message box with the word count and frequency
    message = f'Total number of words: {word_count}\n\n'
    message += 'Frequency of each word:\n\n'
    for word, frequency in frequency_dict.items():
        message += f'{word}: {frequency}\n'
    messagebox.showinfo(title='Word Count', message=message)

# Create the button to search for a specific word
def search_word():
    # Get the text from the input box
    text = paragraph_input.get("1.0", "end-1c")

    # Get the word to search for from a message box
    word = messagebox.askstring(title='Search for Word', prompt='Enter a word to search for:')

    # Search for the word in the text
    if word in text:
        messagebox.showinfo(title='Search Result', message=f'The word "{word}" was found in the paragraph.')
    else:
        messagebox.showinfo(title='Search Result', message=f'The word "{word}" was not found in the paragraph.')

# Create the button to count the words and search for a specific word
button_frame = tk.Frame(left_frame, bg='gray10')
button_frame.pack(pady=10)
word_count_button = tk.Button(button_frame, text='Count Words and Frequency', command=count_words, bg='gray30', fg='white', padx=10, pady=5)
word_count_button.pack(side=tk.LEFT, padx=10)
search_word_button = tk.Button(button_frame, text='Search for Word', command=search_word, bg='gray30', fg='white', padx=10, pady=5)
search_word_button.pack(side=tk.LEFT, padx=10)

# Create the right frame for the second program
right_frame = tk.Frame(root, bg='gray10')
right_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the title for the second program
title_right = tk.Label(right_frame, text='Text File Editor', font=('Arial', 36), fg='sky blue', bg='gray10')
title_right.pack(pady=10)