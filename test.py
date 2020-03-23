path = "card.raw"
byte1 = 'ff'
byte2 = 'd8'
byte3 = 'ff'
byte4 = ['e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6',
         'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed',
         'ee',  'ef']
byte_list = []
sig = byte1+byte2+byte3+'e'
start = 0
count = 0
flags = []
txt = ""
with open(path, "rb") as card:
    txt = str(card.read().hex())
    # print(txt)
    while True:
        flag = txt[start:].find(sig)
        if flag == -1:
            break
        start += flag + 1
        flags.append(flag)

with open("{:03d}.jpg".format(count),"wb") as image:
    image.write(bytes( txt[flags[0]:flags[1]]))
