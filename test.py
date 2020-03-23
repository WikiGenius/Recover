from goto import with_goto

# variables
path = "card.raw"
count = 0
byte_list = []



def fill_byte_list(card, byte_list):
    for _ in range(4):
        byte_list.append(card.read(1))


def write_header_file(image, byte_list):
    for i in range(4):
        image.write(byte_list[i])


def add_element_byte_list(card, byte_list):
    byte_list.reverse()
    byte_list.pop()
    byte_list.reverse()
    byte_list.append(card.read(1))


@with_goto
def test():
    # 1 open card file
    with open(path, "rb") as card:
        print("step1")
        # 2 read 4 bytes into byte_list
        print("step2")

        fill_byte_list(card, byte_list)
        # 3 compare with signature
        print("step3")

        label .trig
        if int(byte_list[0].hex()) == 0xff and int(byte_list[1].hex()) == 0xd8 and int(byte_list[2].hex()) == 0xff and int(byte_list[3].hex()) & 0xf0 == 0xe0:
            # 4if yes
            print("step4")

            label .new_image

            # 5open new image jpg
            with open("{:3d}.jpg".format(count), "wb") as image:
                print("step5")

                count += 1
                write_header_file(image, byte_list)
                # 6clear byte_list

                byte_list.clear()
                print("step6")

                label .continue_write
                # 7write 512 bytes into image
                image.write(card.read(512))
                print("step7")

                # 8 read 4 bytes into byte_list

                fill_byte_list(card, byte_list)
                print("step8")
                # 9check end card file

                if byte_list[0] == b'':
                    goto .end
                print("step9")
                
                # 10 compare with signature
                if int(byte_list[0].hex()) == 0xff and int(byte_list[1].hex()) == 0xd8 and int(byte_list[2].hex()) == 0xff and int(byte_list[3].hex()) & 0xf0 == 0xe0:
                    # 11 if yes go to step 5
                    goto .new_image
                else:
                    # 12 if no go to step 7
                    goto .continue_write
        else:
            # 13 if no
            # 14 check end card file
            if byte_list[0] == b'':
                goto .end
            # 15 drop first byte and append new byte (overlap)
            add_element_byte_list(card, byte_list)
            # goto step 3
            goto .trig
    label .end


test()
