from operator import itemgetter

with open("8.txt", 'r') as f:
    pixels = f.readline()

#pixels = 



layer_size = 25 * 6

print("Expected laters", len(pixels) / layer_size)




image = {}

new = []

layer = 0

for i in range(0, len(pixels), layer_size):
    
    print(pixels[i:i+layer_size])

    image[str(layer)] = pixels[i:i+layer_size]

    layer +=1

print(len(pixels))

print(image)

lowest = []

for key in image.keys():
    lowest.append((key, image[key].count("0")))

#print(lowest)

print(sorted(lowest, key=itemgetter(1))[0][0])


print(image["14"].count("1") * image["14"].count("2"))





final_image = []



# 0 is black, 1 is white, and 2 is transparent

for p in range(0, layer_size):
    
    final_image.append("")
    
    for i in range(0, len(image.keys())):
        if image[str(i)][p] == "0":
            final_image[p] = " "
            break
        elif image[str(i)][p] == "1":
            final_image[p] = "1"
            break
        elif image[str(i)][p] == "2":
            final_image[p] = "2"
        

            



#print(final_image)

for i in range(0, len(final_image), 25):
    #print(i)
    a = ''
    print(a.join(final_image[i:i+25]))

a = ''

#print(a.join(final_image))
        