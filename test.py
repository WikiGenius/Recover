from goto import with_goto

# variables
path = "card.raw"
count = 0
byte_list = []


def fill_byte_list(card, byte_list):
    byte_list.clear()
    for _ in range(4):
        byte = card.read(1)
        byte_list.append(byte)


def write_header_file(image, byte_list):
    for i in range(4):
        image.write(byte_list[i])


def add_element_byte_list(card, byte_list):
    byte_list.reverse()
    byte_list.pop()
    byte_list.reverse()
    byte = card.read(1)
    byte_list.append(byte)
    # print(byte.hex())
    # print(int.from_bytes(byte,'big'))


@with_goto
def test(count):
    # 1 open card file
    with open(path, "rb") as card:
        # print("step1")
        # 2 read 4 bytes into byte_list
        # print("step2")

        fill_byte_list(card, byte_list)
        # 3 compare with signature
        label .trig
        # print("step3")
        (byte1, byte2, byte3, byte4) = (int.from_bytes(byte_list[0], 'big'), int.from_bytes(
            byte_list[1], 'big'), int.from_bytes(byte_list[2], 'big'), int.from_bytes(byte_list[3], 'big'))
        if byte1 == 0xff and byte2 == 0xd8 and byte3 == 0xff and byte4 & 0xf0 == 0xe0:
            # 4if yes
            # print("step4")

            label .new_image

            # 5open new image jpg
            # global count
            with open("{:03d}.jpg".format(count), "wb") as image:
                # print("step5")
                # print(count)
                count += 1
                write_header_file(image, byte_list)
                # print(byte_list)
                # 6clear byte_list

                # byte_list.clear()
                # print("step6")
                # x = 0
                label .continue_write
                # x +=1
                # 7write 512 bytes into image
                # print(x)
                image.write(card.read(508))
                padding = (4 - (512 * 24 % 4) % 4)

                for _ in range(padding):
                    # fputc(0x00, outptr);
                    image.write(bytes(0x00) )
                
                # print("step7")

                # 8 read 4 bytes into byte_list

                fill_byte_list(card, byte_list)
                # print(byte_list)
                # print("step8")
                # 9check end card file

                if byte_list[0] == b'':
                    # goto .end
                    return
                # print("step9")

                # 10 compare with signature

                (byte1, byte2, byte3, byte4) = (int.from_bytes(byte_list[0], 'big'), int.from_bytes(
                    byte_list[1], 'big'), int.from_bytes(byte_list[2], 'big'), int.from_bytes(byte_list[3], 'big'))
                if byte1 == 0xff and byte2 == 0xd8 and byte3 == 0xff and byte4 & 0xf0 == 0xe0:
                    # print("step10")
                    # 11 if yes go to step 5
                    goto .new_image
                else:
                    # 12 if no go to step 7
                    goto .continue_write
        else:
            # 13 if no
            # 14 check end card file
            if byte_list[0] == b'':
                # goto .end
                return
            # print(byte_list)
            # print("step14")
            # 15 drop first byte and append new byte (overlap)
            add_element_byte_list(card, byte_list)
            # print("step15")
            # goto step 3
            goto .trig
        # label .end


test(count)
