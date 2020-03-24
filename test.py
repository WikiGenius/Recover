from goto import with_goto

# variables
path = "card.raw"
count = 0


def read_block(card):
    block = card.read(512)
    return block


@with_goto
def test(count):
    # 1 open card file
    with open(path, "rb") as card:
        # 2 read 512 bytes into block
        block = read_block(card)
        # 3 compare with signature
        label .trig
        (byte1, byte2, byte3, byte4) = (block[0], block[1], block[2], block[3])
        if byte1 == 0xff and byte2 == 0xd8 and byte3 == 0xff and byte4 & 0xf0 == 0xe0:
            # 4if yes
            label .new_image

            # 5open new image jpg
            with open("images/{:03d}.jpg".format(count), "wb") as image:
                count += 1
                label .continue_write
                # 6write 512 bytes into image
                image.write(block)
                # 7 read 512 bytes into block
                block = read_block(card)
                # 9check end card file
                if len(block) < 512:
                    # goto .end
                    return

                # 10 compare with signature
                (byte1, byte2, byte3, byte4) = (
                    block[0], block[1], block[2], block[3])
                if byte1 == 0xff and byte2 == 0xd8 and byte3 == 0xff and byte4 & 0xf0 == 0xe0:
                    # 11 if yes go to step 5
                    goto .new_image
                else:
                    # 12 if no go to step 7
                    goto .continue_write
        else:
            block = read_block(card)
            # 13 if no
            # 14 check end card file
            if block[0] == b'':
                # goto .end
                return
            # go to step 3
            goto .trig
        # label .end


test(count)
