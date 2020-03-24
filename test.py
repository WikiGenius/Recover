from goto import with_goto
path = "card.raw"
count = 0

# 1 open card file
@with_goto
def test(count):
    with open(path, "rb") as card:
        while True:
            # 2 read block 512 byte
            block = card.read(512)
            # 3 check end file card
            if(len(block) == 0):
                break
            # 4 the header block
            (b1, b2, b3, b4) = (block[0], block[1], block[2], block[3])
            # 5 check the header with signature jpg
            if b1 == 0xff and b2 == 0xd8 and b3 == 0xff and b4 & 0xf0 == 0xe0:
                count += 1
                # 6 yes -> open new image jpg
                label .loop
                with open("{:03d}.jpg".format(count),"ab") as image:
                    #7 write into image
                    image.write(block)
            else:
                if count > 0:
                    # go to step 6
                    goto .loop
test(count)
