from PIL import Image, ImageDraw, ImageFont

f=open('guests.txt','r')
guests=f.readlines()
for i in range(len(guests)):
    guests[i]=guests[i].rstrip()

flowers=Image.open('4317423.jpg').convert("RGBA")
logoWidth,logoHeight=flowers.size

im=Image.new('RGBA',(361,289+300*len(guests)),'white')
draw=ImageDraw.Draw(im)
for i in range(len(guests)):
    draw.text((180,145+300*i),str(guests[i]),fill='black')
    draw.rectangle((0,289*i,360,288),outline='black')
    im.paste(flowers,(360 - logoWidth, 288*i -logoHeight),flowers)
    
    
    
    
im.save('drawing.png')




