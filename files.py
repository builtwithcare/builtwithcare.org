import os

directory = "C:/Users/baller/Downloads/photos_3/"

print()

counter = 0
for filename in os.listdir(directory):
    print(f'<img src="w3images/{filename}">')