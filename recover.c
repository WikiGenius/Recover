/********************************************************

recover file

Author: Muhammed El-Yamani
muhammedelyamani92@gmail.com
March 2020


********************************************************/
#include "jpg.h"

int main(int argc, char *argv[])
{
    //Check for invalid usage
    if (argc < 2)
    {
        fprintf(stderr, "Usage: ./recover card.raw\n");
        return 1;
    }
    path_card = argv[1];
    //1 open card file
    card = fopen(path_card, "r");
    if (card == NULL)
    {
        fprintf(stderr, "Couldn't open card file for reading.\n");
        return 2;
    }
    while (1)
    {
        //2 read block 512 byte
        n_bytes = fread(block, sizeof(BYTE), 512, card);
        //3 check end file card
        if (n_bytes < 512)
        {
            return 0;
        }
        //4 the header block
        b1 = block[0], b2 = block[1], b3 = block[2], b4 = block[3];
        //5 check the header with signature jpg
        if ((b1 == 0xff) && (b2 == 0xd8) && (b3 == 0xff) && ((b4 & 0xf0) == 0xe0))
        {
            count += 1;
            printf("recovering image%03d.jpg ...\n", count);
            //6 yes -> open new image jpg
loop:
            sprintf(path_image, "%s%03i.jpg", dir_image, count);
            image = fopen(path_image, "a");
            if (image == NULL)
            {
                fprintf(stderr, "Couldn't open image file for writing.\n");
                return 3;
            }
            //7 write into image
            fwrite(block, sizeof(BYTE), 512, image);
            fclose(image);
        }
        else
        {
            if (count > 0)
            {
                //go to step 6
                goto loop;
            }
        }
    }
    fclose(card);
    return 0;
}