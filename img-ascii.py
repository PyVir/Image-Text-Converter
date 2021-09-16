from PIL import Image
import os, time

def convertArray(img : list):
	return [[img.getpixel((j, i)) for j in range(img.height)] for i in range(img.width)]

def getNearest(number : int, number_list : list):
	index = 0
	for i in range(len(number_list)):
		if abs(number - number_list[i]) < abs(number - number_list[index]): index = i
	return index

def convertAscii(data : list, pallete : list):
	ratio_list = assignN(pallete)
	for j in range(len(data)):
		for i in range(len(data[j])):
			data[j][i] = pallete[getNearest(sum([data[j][i][k] for k in range(3)]) / 3 / 255, ratio_list)]
	return data

def assignN(pallete : list):	
	return [i / len(pallete) for i in range(len(pallete))]

def convertImg(img_name : str, main_pallete : list): 
	return convertAscii(convertArray(Image.open(img_name).convert("RGB")), main_pallete)

if __name__ == "__main__":
	first = time.time()
	img = convertImg("Image.png", [" ", "^", "*", ">", "+", "/", "!", "O", "#"])
	last = time.time()
	length = last - first

	final = ""
	for j in range(len(img)):
		line = ""
		for i in range(len(img[j])):
			line += img[j][i]
		final += line + "\n"

	print(final)

	print("Length : " + str(length))