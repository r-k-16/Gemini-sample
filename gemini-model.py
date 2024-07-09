from geminiAPI import gemini_apikey
import google.generativeai as genai
import PIL.Image, os, readline
import tkinter as tk
from tkinter import filedialog

genai.configure(api_key=gemini_apikey)

model = genai.GenerativeModel('gemini-1.5-flash')

print('"exit" to leave')
print('"image" to use image to search')

while True:

	query = input('Enter your question: ')

	while query == '':
		query = input('Enter your question: ')

	if query == 'exit':
		print('Byee')
		break

	if query == 'image':

		root = tk.Tk()
		root.withdraw()

		img_path = filedialog.askopenfilename()

		img = PIL.Image.open(img_path)
		
		#img.show()		#View the selected image

		query = img

	response = model.generate_content(query)

	print(response.text)
