from PIL import Image, ImageDraw, ImageFont
import io
import folium
import pandas as pd
import os
from datetime import datetime
import concurrent.futures
import time 

def convert_filename_to_timestamp(filename):
    timestamp_str = filename.split('.')[0]
    ts = datetime.fromtimestamp(int(timestamp_str)).strftime('%H:%M:%S')

    return ts

counter=1

def TextToImg(img, id):
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("s.ttf", 48)
	position = (60, 30)
	text_color = (0,0,0)
	shadow_offset = (2, 2)
	text = convert_filename_to_timestamp(id)

	box_position = [position[0], position[1], position[0] + 48*3.5, position[1] + 48]

	draw.rectangle(box_position, fill=(255, 255, 255, 255))

	draw.text(position,text,(0,0,0),font=font)

	return img


def DrawMap(id):
	global counter
	print(id)

	file_path = f'data/{id}.txt'
	df = pd.read_csv(file_path, sep='\\s+', header=None, names=['latitude', 'longitude'])

	m = folium.Map(location=[55.7522, 37.6156], zoom_start=10.5)

	for index, row in df.iterrows():
	    folium.CircleMarker(
	        location=[row['latitude'], row['longitude']],
	        radius=5,  # Adjust the size of the circle
	        color='black',  # Border color of the circle
	        fill=True,
	        fill_color='yellow',  # Fill color of the circle
	        fill_opacity=0.8  # Opacity of the fill color
	    ).add_to(m)
	
	m.save(f'html/{id}.html')


	print(f'html/{id}.html')
	img_data = m._to_png(5)
	img = Image.open(io.BytesIO(img_data))
	
	new_filename = f'img/{counter:04d}.png'

	TextToImg(img, id).save(new_filename)

	print(new_filename)
	m
	counter += 1

def get_txt_files(folder_path):
    files_and_dirs = os.listdir(folder_path)
    txt_files = [os.path.splitext(file)[0] for file in files_and_dirs if file.endswith('.txt')]

    return txt_files

for id in get_txt_files('data'):
	DrawMap(id)