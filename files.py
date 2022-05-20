# import os

# directory = "C:/Users/baller/Downloads/photos_3/"

# print()
c = 23
co = 0
while c > 0:
    if co % 7 == 0:
        print('<div class="column">')
    for i in range(7):
        print(f'<img src="img/image{c + 1}.jpg" style="width:100%">')
        c -= 1
    co += 1
    if co % 7 == 0:
        print('</div>')
# counter = 0
# for filename in os.listdir(directory):
#     print(f'<img src="w3images/{filename}">')