# Explanation

```bash
./recover card.raw
```

## first three bytes of JPEGs are

_____________________________________________________________________

0xff 0xd8 0xff

The fourth byte, meanwhile, is either

0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed,

0xee, or 0xef

Put another way, the fourth byte’s first four bits are 1110

_____________________________________________________________________

digital cameras often initialize cards with a FAT file system whose **“block size” is 512 bytes (B)**
