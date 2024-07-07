from PIL import Image
import io
import folium
import pandas as pd
import os

def DrawMap(id):		
	print(id)
	file_path = f'data/{id}.txt'
	df = pd.read_csv(file_path, sep='\\s+', header=None, names=['latitude', 'longitude'])

	# Create a map centered around Moscow
	m = folium.Map(location=[55.7522, 37.6156], zoom_start=11)

	# Plot each point on the map
	for index, row in df.iterrows():
	    folium.CircleMarker(
	        location=[row['latitude'], row['longitude']],
	        radius=5,  # Adjust the size of the circle
	        color='black',  # Border color of the circle
	        fill=True,
	        fill_color='yellow',  # Fill color of the circle
	        fill_opacity=0.8  # Opacity of the fill color
	    ).add_to(m)
	    # print(str(row['latitude']) +" "+str(row['longitude']))

	# Save map to HTML file
	m.save(f'html/{id}.html')


	img_data = m._to_png(5)
	img = Image.open(io.BytesIO(img_data))
	img.save(f'img/{id}.png')
	print(f'{id}.png')
	m

def get_txt_files(folder_path):
    
    files_and_dirs = os.listdir(folder_path)
    # txt_files = [file for file in files_and_dirs if file.endswith('.txt')]
    txt_files = [os.path.splitext(file)[0] for file in files_and_dirs if file.endswith('.txt')]

    return txt_files

# for id in get_txt_files('data'):
# 	DrawMap(id)
	# break


# Directory containing the images
directory = 'D:/Downloads/img1/output_images'

# Get list of files in the directory
files = os.listdir(directory)

# Sort files alphabetically to ensure sequential renaming
files.sort()

# Counter for renaming
counter = 1

def Attempt(Funct, arr, num): #making num threads to do Funct() with len(arr) elements 
    pos = 0
    global MinDiff
    last=time.time()
    for j in range(1):
        for pos in range(0, len(arr), num):
            threads = []
            for i in range(0, num):
                # if(time.time()-last>=MinDiff):
                #     return
                var = i+pos
                # print(var)
                if(var >=len(arr)):
                    break
                thread = threading.Thread(target=Funct, args=(arr[var],))
                thread.start()
            threads.append(thread)
            
            for thread in threads:
                thread.join()

#     print(f"{num} {(time.time()-last)/10}")
#     MinDiff = time.time()-last
# done_drive = set()
# printed_positions = set()

# Iterate over sorted files and rename them
# for filename in files:
#     if filename.endswith('.png'):  # Assuming all files are PNGs
#         # Generate new filename
#         new_filename = f'{counter:04d}.png'
        
#         # Construct full paths
#         old_path = os.path.join(directory, filename)
#         new_path = os.path.join(directory, new_filename)
        
#         # Rename file
#         os.rename(old_path, new_path)
        
#         # Increment counter for the next file
#         counter += 1
# from PIL import Image, ImageDraw, ImageFont
# import os
# from datetime import datetime
# import pytz

# def convert_filename_to_timestamp(filename):
#     # Extract the timestamp part from the filename
#     timestamp_str = filename.split('.')[0]
#     ts = datetime.fromtimestamp(int(timestamp_str)).strftime('%Y-%m-%d %H:%M:%S')

#     return ts

# folder_path = 'D:/Downloads/img1/img'

# # Iterate through each file in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith(".jpg") or filename.endswith(".png"):  # Add more extensions if necessary
#         image_path = os.path.join(folder_path, filename)
#         print(image_path)
#         img = Image.open(image_path)
#         draw = ImageDraw.Draw(img)
#         font = ImageFont.truetype("s.ttf", 48)
#         draw.text((80, 50),convert_filename_to_timestamp(filename),(0,0,0),font=font)
#         img.save(os.path.join('D:/Downloads/img1/output_images', filename))