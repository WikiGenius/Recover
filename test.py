path = "card.raw"
byte_list = []


def look_sig_jpg(card, byte_list):
    n = len(byte_list)
    for _ in range(4 - n):
        byte_list.append(card.read(1))
    return byte_list


def sig_beg_jpg(byte_list):
    if len(byte_list == 4):
        pass
    return


def open_new_jpeg():
    # write byte_list?
    # write 512 bytes
    # byte_list = look_sig_jpg()
    return False


with open(path, "rb") as card:
    byte_list = look_sig_jpg(card, byte_list)
    if sig_beg_jpg(byte_list):
        # open new jpeg file
        while True:
            end_flag = open_new_jpeg()
            if end_flag:
                break
    else:
        # pop last byte in byte list
        # and loop again
        pass
