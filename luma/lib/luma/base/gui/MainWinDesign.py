# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/base/gui/MainWinDesign.ui'
#
# Created: Mon Jan 31 21:41:17 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\xcb\x49\x44\x41\x54\x38\x8d\xad\x94\x4b\x48\x94" \
    "\x51\x14\x80\xbf\x79\x39\x63\x63\x36\x2a\x3d\x48" \
    "\xb0\x5f\x22\x70\x55\x63\x9b\xd0\x8c\x71\xa2\xa8" \
    "\xa5\x9b\x56\x15\x59\xb4\x0d\x95\xac\xa0\x4d\xb8" \
    "\xaa\x5d\xd2\x03\xda\xd9\x3e\x08\x83\xe8\x01\x91" \
    "\x96\x90\x9b\x8a\x31\x92\x9e\xe4\x68\x69\x0f\xb2" \
    "\xff\xd7\x19\x67\xc6\x99\x7b\xee\x6d\xe1\x94\x95" \
    "\xd3\x38\x50\x07\xee\xe6\xde\x73\x3e\xbe\x7b\x38" \
    "\xf7\x42\x89\x91\x39\x45\x5f\xf2\x04\x7d\xa5\xe6" \
    "\xbb\x4a\x49\x4a\x9d\x24\x84\xc1\x56\x0a\x44\xa8" \
    "\xaa\xba\x80\xb3\x5c\x8d\xbb\x44\x81\x4e\x4f\x43" \
    "\x0d\xde\x86\x1a\x8c\xa6\xb3\x94\x82\x92\xc0\x5a" \
    "\x73\xa8\x2c\xb2\x8b\x40\x74\x17\x4a\x71\xe8\xbf" \
    "\x80\x93\xdd\xb4\x51\x89\xc5\xc6\x97\xb8\x36\x39" \
    "\xb8\x2b\xb1\x26\x8f\xd2\xf6\xcf\x60\x6d\xe8\x28" \
    "\x6f\x69\x02\x9e\x03\xf7\xa8\xd8\xb9\x1b\x9d\xa3" \
    "\xe3\x9f\xc0\xb3\xc7\xb1\x28\xa3\xd5\xbd\x63\x2d" \
    "\x20\x80\xe0\x8f\x06\x31\x7e\x5a\xc7\xf6\x63\x15" \
    "\xab\x75\x01\x98\x73\x58\x08\x96\x51\x84\x24\x47" \
    "\x58\x04\x94\x22\x22\x0a\xcb\xdf\x58\x67\xf9\x0f" \
    "\x4e\x03\x73\xf9\x92\x5a\xa6\x2f\x7b\x70\x86\x26" \
    "\xe2\x22\xc4\x55\x8e\x07\x22\x20\x42\x4c\x04\x47" \
    "\x34\xf1\x6d\xf7\x88\xbb\xcc\x39\x0c\x06\x58\x1f" \
    "\xc4\x08\xb0\x7a\x03\xf8\x57\x62\xfc\x95\xb8\x6b" \
    "\xb7\xc0\x86\x0c\x78\x2f\xfd\xae\x33\x7f\x1a\xf5" \
    "\x36\x4b\xea\xf5\x08\xb9\xc4\x2c\xb9\x99\x04\x89" \
    "\xb7\xe3\x18\xd1\x7c\x1b\x4d\x23\x02\x2e\x73\x96" \
    "\x76\xbc\xf4\xb1\xaf\x1b\xea\xde\x81\x19\xce\x37" \
    "\xf7\x13\x60\x96\x6b\xe5\xc2\xa5\xdd\xeb\x20\x19" \
    "\x60\xee\x7e\x86\xd1\x2b\x1f\xc9\xa6\x38\xec\x02" \
    "\xd0\x3d\xb4\x4b\x8e\x3e\xef\xde\x10\x34\x2c\x3b" \
    "\xfb\xbf\x87\x00\x09\x0f\xf6\x1d\xe1\xc5\x35\x30" \
    "\x9a\xc3\x2d\x43\x5c\xfd\xf9\xf2\xe6\x4f\xd3\x2e" \
    "\x8a\xf3\x81\x3d\xa1\x90\xcb\x2a\x11\xae\x00\x27" \
    "\x80\x3d\x9c\xe1\xd5\x0d\x1c\x11\xba\x5a\x1e\x72" \
    "\x35\x7f\x8f\xc5\x48\x76\x13\x16\xc5\x40\x45\xd4" \
    "\x1f\x72\xd7\xcd\x17\x87\x66\x81\x64\x39\xf6\xd3" \
    "\x34\x6f\x6e\xe1\x28\x43\x74\xfb\x20\xb1\x1f\xc7" \
    "\x4b\xfe\x8a\x6f\xc7\x08\x6b\xc5\x40\x55\x33\x21" \
    "\x77\x5d\x11\xf0\x3c\x24\x46\xe0\xc5\x5d\x1c\x2d" \
    "\x44\x9b\x06\x16\xa1\x50\x60\x8e\xab\x2f\x12\x13" \
    "\xa1\x3f\xf7\x15\x98\x2d\xb2\xd2\x90\xf9\x0c\x5a" \
    "\xe8\xff\x13\x0a\xe0\x2d\x24\xa3\x0d\x61\x9f\x0f" \
    "\x48\x14\x31\x06\x56\x04\x40\x6b\xc2\x85\xce\x0a" \
    "\x83\x85\xb0\xfb\x57\x70\x0a\xc8\x01\x15\x80\x67" \
    "\x31\x2f\xb8\x6a\x21\xb7\x10\x63\x49\x2b\x26\x8f" \
    "\xd0\xea\x2b\xcb\x43\x67\x81\x0f\x60\xa6\xe0\xfd" \
    "\x33\x18\x1f\x02\x33\x91\xdf\x4f\x00\x69\x08\x96" \
    "\xc3\x60\x13\xad\xcb\x1a\x6b\x21\xec\xf3\x00\x0e" \
    "\x90\x04\x7b\x06\xbe\xd8\x90\x55\xf4\x2a\x01\xfb" \
    "\x09\x9d\x6b\xaa\x61\xbd\x95\xb7\xf6\x81\xbd\x60" \
    "\x3d\x58\xd4\x58\x34\x11\x5f\x1a\xb2\x93\xf0\x6e" \
    "\x0a\x3e\xda\xc4\x94\x26\xba\xf9\x26\x5d\x5b\x6f" \
    "\xd3\x95\x55\x44\xe3\x93\xc4\x1e\x0f\x43\x62\x1c" \
    "\x56\x78\x40\x2b\x22\x7f\x72\x96\x8c\xdb\xd8\x01" \
    "\xc6\xbc\x82\x95\x56\x38\x5a\xe8\x69\xb8\x4e\x6f" \
    "\xa1\x1e\x3e\x68\xa6\x53\x84\x33\x41\x2f\x21\x7b" \
    "\x8e\xf8\xde\x18\xf5\x45\x8d\xb5\xc6\x4a\x0b\xfd" \
    "\x06\xea\xff\x06\x05\x88\x3c\xa2\xd7\x18\x1a\x67" \
    "\x52\xf4\x6b\xbd\xf4\x0b\xfd\x0e\x38\x9a\x3f\xdc" \
    "\xe9\x05\x08\x10\x00\x00\x00\x00\x49\x45\x4e\x44" \
    "\xae\x42\x60\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x18\x00\x00\x00\x18" \
    "\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\x00\x00\x05" \
    "\x2f\x49\x44\x41\x54\x48\x89\x95\x95\x4b\x6c\x5c" \
    "\xd5\x19\xc7\x7f\xe7\x3e\xe6\x69\xcf\x8c\xe3\xcc" \
    "\xd8\xc1\x8f\xd8\xa1\x09\xc1\x0d\x19\x95\xb6\xa4" \
    "\x04\x02\x02\x55\x3c\x56\x50\x65\x81\x84\x94\x8a" \
    "\x02\x0b\x68\x4a\x81\x05\xa8\x62\x87\xd4\x45\x29" \
    "\x94\x05\x05\xda\x8a\x20\xe8\xa2\x40\x40\x56\x22" \
    "\xa4\x62\x08\x54\x05\x35\x60\x09\x21\x68\x48\x62" \
    "\xc0\x76\x32\x7e\x8c\xed\x79\x78\xde\x77\xee\xdc" \
    "\x99\xfb\x38\x5d\x24\xe3\xc6\x89\x27\x12\xff\xd5" \
    "\x77\xcf\x39\xdf\xf7\x3b\xe7\xfb\x4b\xdf\x15\x74" \
    "\xd0\xbd\x2f\xdf\xbf\xbb\xb1\x29\xf3\x78\x36\xa3" \
    "\xde\x57\x6b\xde\x80\x1e\xdb\x83\xeb\xd8\x78\xa6" \
    "\x4b\xb0\x95\x49\x9d\x6a\x1c\x7e\x75\xcc\xda\xde" \
    "\xf8\xe2\xb9\x3f\xbf\x08\xd8\x80\xdc\xa8\x8e\xb8" \
    "\x78\xe1\xb9\xa3\x0f\xec\xfb\x6e\x69\xfa\xf0\xd9" \
    "\x72\x35\xdc\xd3\x3b\x1a\xe9\xfb\xf1\xd3\x54\x87" \
    "\x46\xa9\x18\xdd\xe4\xdc\x34\x56\xab\xc1\x74\xe6" \
    "\x6f\xb8\x33\x79\xf4\xb9\xb2\x0c\x17\xad\x42\xb4" \
    "\xd0\xf8\xd5\xf4\x91\xff\x1c\x03\x5a\x97\x05\x3c" \
    "\xf0\xfc\xc1\x5b\xcd\xb0\xf3\x76\xff\x0d\x4f\xf7" \
    "\xf6\xf8\x54\xb4\xc0\x1c\x2a\x1f\x32\x97\x9b\xa4" \
    "\x1e\xbb\x93\x89\xe2\x24\x8d\x7a\x02\x27\xb5\x88" \
    "\xd2\x0c\x22\x5d\x0d\xa7\x56\x60\xf0\xdb\x72\x75" \
    "\xa7\xed\x3b\x3a\xf1\xc6\xb1\xdf\x00\x75\xc0\x6b" \
    "\xd7\x54\xdb\xc1\xa1\x4f\x3f\xb9\x35\x17\xbc\xee" \
    "\xcd\xb1\x9b\x1e\x8c\xff\xec\x8a\xf7\xd1\x9c\x1a" \
    "\xc2\xfa\x14\x23\x57\xa7\x50\x3e\x41\x21\x77\x92" \
    "\x72\xa6\x8e\x51\xaa\xa0\xd8\x61\x84\x54\xc0\x15" \
    "\xa0\xfb\x19\xee\x95\x7e\x77\xb9\x32\xb2\x63\x68" \
    "\x74\x2c\x35\x3b\xff\xd1\xf9\x97\xc8\x35\xc0\x13" \
    "\xaf\xfd\x45\x5b\xd0\x06\xc6\x47\x76\x5f\x77\xe5" \
    "\x48\x4f\x91\x9f\x04\x9f\x24\xec\xbd\x89\x54\xbe" \
    "\x01\x6d\x99\x72\xd9\xc1\x74\xfc\x54\x1c\x85\x0a" \
    "\x3e\x3c\xa9\x21\x3c\x15\x3c\x81\x94\x82\xa8\xe3" \
    "\xb0\x3d\x1a\x0c\xcc\xa5\x56\xb7\x46\xc2\x9b\x16" \
    "\x8a\xb9\xfc\x4c\xbb\x5d\x0a\x40\xb0\x7b\xf4\x50" \
    "\x7c\xeb\x55\xc9\x1f\xc5\x8e\x32\x74\x66\x33\x6f" \
    "\x7f\xb0\x8b\x37\xde\x09\x32\x3d\xd5\xe0\xf4\xf1" \
    "\x5e\xaa\xf3\xbd\x08\x3c\xc2\xaa\x07\xae\x06\xc2" \
    "\x3b\x97\x2a\x00\xcf\xa5\x21\x05\x9a\x4f\x67\xb0" \
    "\x7f\x4b\x77\xda\xe2\x97\x40\x02\xd0\x00\xd4\xa7" \
    "\xde\x3b\xb4\x7b\x45\xdf\xf5\xc7\xe4\xae\x21\xff" \
    "\xb5\x5d\xef\x20\xb4\x04\xfd\x63\xbf\xc3\xf3\xef" \
    "\xc2\xb2\xa6\x88\x0c\x45\xd8\xbe\x77\x0b\x99\x52" \
    "\x81\xb4\x21\x28\xa1\x23\x5d\x1d\xe1\xea\xe7\x5e" \
    "\xe0\x41\x17\x0e\xc3\x2d\xd8\x12\x8c\xa0\x36\xec" \
    "\xe1\x60\x38\xa8\x16\x72\xab\x9f\x01\x4d\x2d\xf5" \
    "\x8d\xef\xf6\xa1\x9f\xc7\x22\x3f\xed\x7a\x9e\xd5" \
    "\xec\xb3\x64\xab\x0e\xb5\xf4\x59\x92\xc9\x49\x32" \
    "\x85\x9d\xa4\x73\xff\xe2\xab\x13\xaf\x63\xd4\x34" \
    "\x5a\xc2\x87\xe7\x69\x28\xa8\xe7\x6f\x2f\x40\x4a" \
    "\xc2\x76\x0d\x21\x03\x48\xa5\x89\xae\xd8\x22\x63" \
    "\xa8\x49\x60\x18\x30\xb5\x68\x6f\xcf\x43\x3f\x18" \
    "\xc8\x33\x9d\x7e\x8b\x6a\x3e\x8c\x27\x82\x34\x9d" \
    "\x0c\x8b\x4b\x77\x50\x74\xbb\xc8\x7b\x0a\xa6\xa5" \
    "\x60\x95\x2c\x7c\xad\x1f\xa2\x9a\x2b\xb8\x8e\x8d" \
    "\xd0\x5d\xa4\x1a\x42\x0a\x08\xc9\x10\xc2\x05\xd7" \
    "\x72\x29\xc5\xae\x26\x14\x3b\xb5\xaf\x02\x71\xe0" \
    "\x8c\x56\x51\x83\xdb\x7c\xfa\xdf\xf9\x6e\xb9\x86" \
    "\xe2\xf6\xe2\x57\x24\x86\xa3\xb0\x32\x9b\xa3\x6a" \
    "\xaf\x52\x5c\x4a\xe2\xc5\xee\x64\xc5\xff\x1e\x3d" \
    "\x3b\xf7\x91\x2c\xc5\x28\xe7\xfc\x14\x32\x27\x28" \
    "\x29\x9f\x83\xf0\x68\xa4\x03\x94\x7d\x4d\x36\x07" \
    "\x22\xf8\xfb\x76\x10\x9e\xf9\x9a\xf3\x3e\xe8\x5a" \
    "\x55\x09\x31\x33\xff\x5f\x1c\xc3\x87\x50\x75\x90" \
    "\x20\xa5\xc0\x74\x55\xea\x52\x60\x75\x97\xf1\x16" \
    "\xb6\x30\x3b\x57\xa4\x76\xfc\x19\xa2\x99\x28\x83" \
    "\xd7\x3f\x42\x54\x6e\xc3\x3c\xf9\x39\x5e\xf1\x5b" \
    "\x96\xe3\xf7\x50\xcd\xcd\xe2\x99\xb3\x04\x44\x86" \
    "\xa5\xd5\x3a\xc0\x5e\xe0\x1f\x9a\x6d\x9b\x2c\xa6" \
    "\xf7\x63\xa4\xfe\x44\xb4\xaf\x0b\xb5\x2b\x80\x27" \
    "\x35\x9a\xb6\xa0\xe1\xc2\xb2\x97\xa5\xba\xf8\x2e" \
    "\x67\x9e\xfa\x6c\x83\x41\x70\xf3\x46\xd3\xa1\xad" \
    "\x83\x89\x44\x02\xcd\x75\x20\x74\xf5\xaf\xe9\xe9" \
    "\xbf\x9b\x5a\xfa\x9f\x2c\xe6\x5f\x81\x2e\x05\xd3" \
    "\x16\x54\x84\xca\x8a\x17\xa2\xea\xac\x02\x10\x8f" \
    "\xc7\x11\x42\x20\xe5\x86\x63\x67\x9d\xf2\xf9\x3c" \
    "\x00\x9a\x6b\xd8\xa9\xac\xe5\x8d\xc6\x7b\xae\xc0" \
    "\x17\x3e\x40\xf6\xf4\x24\x05\x2b\x45\x0b\x1d\xc3" \
    "\xf5\xe3\x7a\x3a\x5e\xbd\xd0\xb1\xd0\xfe\xfd\xfb" \
    "\xd7\x62\xd3\x34\x99\x98\x98\x58\xb7\xaf\x2d\xa7" \
    "\xd3\xaf\xb6\xd2\xb9\xdf\x8b\x6d\xfd\x04\xd4\x00" \
    "\x8d\xc0\x5e\xb2\xd5\x15\x14\x11\x42\x78\x2a\x4a" \
    "\x0b\xb4\x4a\xf8\xb2\xb7\x1d\x1f\x1f\xc7\xc8\xcf" \
    "\xd3\x9d\x18\xb9\x64\x4f\x19\x50\x1b\xc7\x0a\x4b" \
    "\xcb\x46\xc1\x86\x82\x03\x83\x7d\x77\x81\xad\xa1" \
    "\xb6\x82\x88\x56\x08\x1c\x95\x50\xcf\xd8\xba\x24" \
    "\x21\x04\x42\xfc\x7f\x4e\x1a\xf9\x79\xaa\xa9\x8f" \
    "\x37\x84\x2b\xff\x7e\xe6\xb7\x5f\x69\x53\x5f\xbe" \
    "\x5f\x3e\x93\xc5\x68\x41\xd5\x51\x10\x2e\x78\x2d" \
    "\x3f\xd2\x51\x71\x9b\x1e\x96\x91\x59\x97\x24\xa5" \
    "\x5c\xf3\xc1\x34\x4d\xba\x13\x23\x0c\xec\xb9\x6f" \
    "\x63\x00\xe0\xec\x90\xf5\x97\x8c\xc9\x8f\x2b\xa5" \
    "\x8c\x4d\xcb\x88\xa1\x97\xc3\x48\xd7\x45\x7a\x0e" \
    "\xe1\x52\x80\x48\xe2\xfa\x8e\xed\x99\x98\x98\x58" \
    "\x03\x6e\x64\xbe\x06\x70\xe4\xd9\xc7\x8e\x0f\xfe" \
    "\xe2\xa1\x83\x86\xf0\xbd\x14\xb8\xe6\xa6\xe8\xe6" \
    "\xfe\x47\x28\xae\xfc\x01\xdd\x92\x44\x94\x6b\x69" \
    "\xb1\xa9\x23\xa0\x6d\xb2\x69\x9a\x6b\xc0\x4b\x00" \
    "\x80\x93\x3e\xf2\xd7\xf1\xbe\x7a\x53\xaf\xa7\x67" \
    "\x5e\xd0\x93\xb7\x75\xf7\xd5\x93\xa8\x75\x97\xf2" \
    "\xc0\x2d\x98\x0b\x5f\x76\x04\xc0\xe5\x4d\xd6\x2e" \
    "\x88\xad\xec\xb1\xd7\x0e\x0f\xdd\x38\x66\xe6\x17" \
    "\xce\x3e\x5c\x8a\x6f\xdd\x23\x06\xb7\x07\x65\xa9" \
    "\x89\x52\x5e\xef\x41\xdb\xe0\x76\x4b\x2e\x67\xb2" \
    "\x76\xd1\x77\x63\xf1\xf8\xd4\xbb\x30\xf5\x85\x6f" \
    "\x24\x79\x4b\xa0\x3b\x76\x40\x6e\x1e\xb9\xb9\xb9" \
    "\x92\x5a\x3b\x70\x71\x9f\xdb\x26\x77\xd2\x25\x3f" \
    "\xfd\x0b\xc0\x41\xce\x4d\xc4\x61\xe0\xee\x5c\x2e" \
    "\xf7\x68\xc7\x2a\x1d\x94\x48\x24\x3a\x02\x2e\x04" \
    "\xf9\x01\xe3\xfb\x16\x6f\xeb\x7f\xa7\x1a\x74\xbf" \
    "\x7b\xca\x6c\xf9\x00\x00\x00\x00\x49\x45\x4e\x44" \
    "\xae\x42\x60\x82"
image2_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x05" \
    "\x06\x49\x44\x41\x54\x38\x8d\xad\x95\x5d\x68\x65" \
    "\x57\x15\xc7\x7f\x6b\xef\x7d\xce\xb9\xe7\x7e\xe4" \
    "\x26\xcd\x35\x9d\x26\x99\x4c\x6f\x66\x9a\x4c\x3b" \
    "\x13\xd4\x01\x0b\x5a\x2b\x05\x5f\x2a\xda\x5a\x68" \
    "\x29\x3e\x94\x0a\xa1\x50\x90\x3e\xf8\xe2\x07\xf8" \
    "\x30\x53\xea\xa0\xf8\x2a\x14\xfa\x30\x52\x0b\x56" \
    "\x41\xf4\x41\x51\x94\x3a\x58\x29\x83\x58\xe9\x30" \
    "\x16\xe9\xa4\xb5\xd3\x4c\x32\x1f\xb9\x37\x93\x4c" \
    "\x32\x37\xb9\x1f\xe7\x9e\x73\xf6\xf2\xe1\xde\x64" \
    "\x82\xcf\xee\x97\xbd\x1f\xf6\xfe\xb1\xf6\x5a\xff" \
    "\xb5\xfe\x00\x08\x88\x03\xcb\xff\x61\x39\xb0\x02" \
    "\x22\x7b\x60\x44\x74\xb1\x1a\x3c\x72\x38\x72\x2f" \
    "\x6a\xb9\x5c\x37\xc6\xa4\xaa\x08\xe8\xdd\x57\xaa" \
    "\x07\x8e\xba\x7f\xf2\x5e\x03\xd7\x4b\x96\x57\x93" \
    "\xec\xb5\x9f\x6d\xf7\x2e\xa0\x03\xb0\x88\x88\x7e" \
    "\x67\x2c\x3c\xfd\xb5\x13\xb3\x67\xaa\x8f\x3d\xaa" \
    "\xf1\xf8\x08\x3e\x4d\xc4\x7b\x05\x3c\x82\x02\x82" \
    "\xe2\x41\x3d\x9a\xe7\xa8\xf7\xa8\x7a\x40\x51\x55" \
    "\xed\x34\x36\xe8\x5e\x5c\x92\x3f\x5d\x69\x9c\xf9" \
    "\xc9\x66\xf7\x65\x01\x78\x61\x34\xfc\xe2\xf3\x0b" \
    "\x47\xdf\x29\x3e\xf3\xa4\x4f\x1a\x57\xb5\xbb\x76" \
    "\x13\x45\x11\x67\x31\xce\xe1\xf3\x14\x9f\x66\x20" \
    "\x8a\x09\x02\x5c\x5c\xc4\x06\x21\x2a\x20\xc6\x20" \
    "\xc6\x10\x8c\x94\xe9\xed\x24\xe2\xdf\x7a\xd7\xbc" \
    "\xf9\xf1\xda\xa3\x16\xe0\xc9\x6a\xf4\xca\x67\x9e" \
    "\x7e\xe2\xd3\xdd\x56\xd3\x6f\x5f\xba\x68\x45\x10" \
    "\x04\xa3\x69\x62\xd2\x9d\x2d\x53\x1c\xad\x99\xf1" \
    "\xd9\x07\xcd\xe8\xfd\x73\x26\xae\x8c\x9a\xbc\xd3" \
    "\x32\x49\x6b\xcb\x38\x17\x1a\x11\x31\xa8\x8a\x4f" \
    "\xfa\x26\xaa\x96\xbc\x38\x67\x36\x96\xd7\x9c\x03" \
    "\xd0\x72\x79\x26\x1e\x1f\xe1\xd6\xa5\xcb\xb8\x72" \
    "\x59\x4d\x5c\x10\x9f\x26\x94\x0f\x4d\x73\xec\xa9" \
    "\x45\x2a\xf3\x9f\x25\x9e\x38\x8c\x8a\x80\xcf\xe9" \
    "\x34\x56\xd8\x59\xfa\x27\xcb\x7f\xf9\x35\x79\xd6" \
    "\xc7\x86\x91\x20\xa2\x79\x92\x12\xd7\x2a\x64\x51" \
    "\x30\xe3\x00\x8c\x31\xea\xd3\x64\xf0\xfd\x30\x10" \
    "\x9f\xf6\x18\x9f\x5b\xe0\xe4\x4b\x3f\x22\xaa\x4d" \
    "\x42\xd6\x67\x67\x65\x89\xf6\xc6\x1a\x95\xc9\x3a" \
    "\xa5\xc9\x59\x4a\x93\xb3\x54\x8e\x7f\x8e\xa5\x37" \
    "\xce\x92\xec\xde\xc1\xb8\x48\xb0\x16\x86\x15\x77" \
    "\xc3\x62\x8b\xf7\x83\x9c\xfa\x24\xa3\x7a\xf8\x18" \
    "\x27\xbe\x75\x96\xa8\x36\xc9\xce\x47\x17\xb9\xfa" \
    "\x87\x37\xd8\xbd\xf1\x09\x36\x2e\x81\xcf\xa8\x1e" \
    "\x5b\xe0\xc8\x13\x8b\x94\x26\x67\x99\x7f\xee\x7b" \
    "\x5c\x7e\xfd\x87\xe4\xea\x11\x67\xd0\xdc\x83\x22" \
    "\x66\x28\x19\x04\x8f\xb1\x16\xcd\x53\x66\x9f\x7e" \
    "\x81\xc2\xc4\x34\xad\x0f\xde\xe5\xfd\x57\x7f\x40" \
    "\xf3\x5f\x17\x98\x7e\xec\x29\x1e\x7e\xe5\x97\x94" \
    "\xeb\x27\xb8\xf1\x8f\xb7\x58\xfa\xf9\x59\xfa\x77" \
    "\x9a\x94\xa7\xe7\x98\xfa\xc2\x57\xf0\x59\x1f\xb1" \
    "\x6e\x5f\x29\xe6\xa0\xb8\xf3\xb4\xcf\x58\xfd\x38" \
    "\x63\x73\xa7\xc0\xe7\x7c\xfc\xbb\x73\x24\x9d\x5d" \
    "\xa2\xb1\x1a\xc5\xf1\x09\x00\xe2\x7b\x6a\x14\xc6" \
    "\x27\xd8\x6d\x5e\xe7\xfa\x9f\x7f\x01\x40\xf5\xf8" \
    "\xc3\x44\x95\xd1\x81\xb6\x55\x41\x39\x00\x16\xf0" \
    "\x59\x4a\x69\xaa\x8e\x1b\xad\x71\xfb\xf2\x7b\xb4" \
    "\x96\x97\x08\xab\x63\xa0\x1e\xef\xfd\xde\xe7\x40" \
    "\x15\x1b\x97\x69\x5d\xff\x0f\xfd\xad\x26\xa5\x4f" \
    "\x4d\x51\xaa\x4d\xee\x43\x75\x3f\x62\x55\x54\x15" \
    "\x11\x45\xe2\xf2\x7e\xf4\xde\xa7\x18\x6b\x41\x0c" \
    "\xb2\x97\x35\x6b\xc0\x18\x4c\xe0\xf0\x3e\x27\x4b" \
    "\xfb\x60\x06\x7a\x17\xeb\x60\x90\xe3\x03\x11\xab" \
    "\x47\x82\x00\xb2\xde\xe0\x7d\x14\xe1\x0a\xc5\x01" \
    "\xd4\xda\xfd\x9b\x22\x66\x00\x30\x06\x17\xc5\xb8" \
    "\x30\x02\xef\x11\xeb\x30\x36\x40\xfd\xff\xe4\x58" \
    "\x7d\x8e\x0d\x23\xfa\x5b\xeb\xf8\x6e\x8b\x7b\xe6" \
    "\x4f\x51\x3d\x7a\x92\xac\xd7\xc6\x16\x0a\x18\x1b" \
    "\x0c\xc0\xd6\x62\xa3\x90\x3c\x4d\x28\x4f\x1d\x25" \
    "\x1c\x9d\xa0\xb3\xb9\x46\xb2\xb3\x8d\x2b\xc4\x03" \
    "\xf0\x5e\xc4\xaa\x8a\xe6\x39\xae\x58\x66\x7b\xf5" \
    "\x23\xb6\xaf\x7c\x00\xc6\x72\xf4\xab\xcf\x13\x55" \
    "\x46\x48\x3b\xbb\xa4\x49\x1b\x80\x2c\xe9\xd2\x6f" \
    "\xb7\xa8\xdc\x77\x84\xe9\x2f\x7f\x03\x80\x5e\xe3" \
    "\x0a\x59\xbf\x87\x09\x22\xd4\x2b\xa0\xb8\xbb\xd3" \
    "\xca\x23\x46\x30\x61\x81\x95\x3f\xbe\x4e\xf5\xc8" \
    "\x3c\xe5\x07\x4e\xf1\xd0\x73\xdf\xe7\xea\xf9\x5f" \
    "\x71\xed\x9d\xdf\xb3\xfe\xfe\x05\xd2\x4e\x8b\x89" \
    "\x93\x9f\xe7\xc8\xe3\xdf\x24\xac\x4e\xd0\x6d\xae" \
    "\xd0\x78\xef\xaf\x04\xc5\x11\xbc\x57\x34\xf7\xa8" \
    "\xb2\x07\x1e\x96\x53\x04\x1b\xc5\xec\x36\x57\xb9" \
    "\xf2\x9b\x9f\x72\xec\xd9\x6f\x53\x99\x3b\xc5\x43" \
    "\x33\xf3\xb4\xd7\xae\x92\x74\x5a\x14\xc7\x26\x28" \
    "\xdd\x3b\x03\x36\x20\xd9\x6a\x72\xed\xfc\x9b\xe4" \
    "\x79\x8e\x2d\x14\x90\x3c\x1f\x8e\x56\x1d\x74\x9e" \
    "\xf7\x2a\xaa\x8a\x18\x03\x9a\xab\x2b\x96\xe5\xd6" \
    "\x87\x17\xe9\x9d\x3b\xcd\xf4\x97\xbe\x4e\xa5\xbe" \
    "\xc0\x48\xfd\xc4\x50\x39\xd0\xdf\xde\xa0\xbd\xf2" \
    "\x6f\x1a\x97\xfe\x46\xd6\x4f\x30\x61\x01\xe3\x02" \
    "\xf5\xb9\x92\xb5\xbb\x28\x22\x0e\xc0\xf5\x92\xd5" \
    "\x4e\x63\x83\x60\xa6\x46\xba\xbd\x23\x88\xa8\x2b" \
    "\x94\xa4\xbd\xd9\xe0\xc3\xdf\xbe\x4a\xf9\xde\xc3" \
    "\x94\xee\xbb\x1f\x71\x01\x06\xa5\xbb\xd9\xa0\xb7" \
    "\x7b\x07\x17\x57\xb0\x51\x09\xe3\x02\xb5\x71\x59" \
    "\xba\xb7\x3e\xa1\x7d\x73\x9d\x10\x59\xb5\x00\x0f" \
    "\x04\x66\xe3\xc1\x7e\xb2\x98\x4f\x1d\x22\xaa\x96" \
    "\xbc\x7a\x55\xac\x55\x13\x86\x6a\x0a\xb1\xf6\xbb" \
    "\x6d\x6d\xaf\xdf\xd0\xce\xe6\x9a\x76\x6e\x6f\xa8" \
    "\x47\xd5\x46\x45\x05\x51\x10\xf5\xb9\xd7\xde\xfa" \
    "\x9a\xde\x7c\xfb\x6d\x09\x6e\x6c\xca\xdf\x5b\xbd" \
    "\x97\x86\x0e\x82\x7e\x77\x3c\x3e\xfd\x78\xfd\xd0" \
    "\x99\x70\x61\x56\xe3\x5a\x05\x54\x65\x50\x08\xbf" \
    "\xdf\x6d\x78\x1d\x38\x87\xcf\xd1\x5c\x87\x03\x47" \
    "\xc9\xda\x5d\x6d\xdf\x5c\xc7\xdc\x6e\xcb\xf9\x8d" \
    "\xce\x99\x1f\x37\x77\x5f\x3e\xe0\x79\xe8\xe2\x68" \
    "\xe1\x91\x99\xc8\xbd\x98\x45\x41\x5d\x20\x65\xcf" \
    "\xf3\x86\x6d\x3a\xb0\xbf\xbb\xfb\xc0\xf6\x54\x15" \
    "\x09\x42\x64\xf9\x5a\x92\xbd\x76\x6e\xb3\x73\x01" \
    "\x90\xff\x02\xca\x66\x7e\x61\xf1\x24\xad\xf5\x00" \
    "\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
image3_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x03" \
    "\xb3\x49\x44\x41\x54\x38\x8d\xa5\xd2\x4f\x4c\x14" \
    "\x57\x1c\x07\xf0\xef\x9b\xd9\xbf\x2c\xec\x0e\xb8" \
    "\x65\x41\xa4\x25\x36\x28\xfd\x13\x9d\xd4\x36\x2d" \
    "\x5a\xe3\x6e\x7a\x70\x21\x1e\x9a\xb4\x34\xc6\x78" \
    "\xe0\xe0\xb5\xc7\x46\x2f\xa6\x90\xf6\xb0\x3d\xb1" \
    "\x4d\x63\x22\x35\xe9\x12\x4d\x88\x1a\x2b\x29\x89" \
    "\x46\xea\x36\x6b\x0d\xb6\xa5\x87\x75\xaa\x54\x28" \
    "\xa4\x65\xad\x82\x55\x16\x3b\xcb\xe2\xce\xbe\x37" \
    "\x33\xef\xf5\xb0\x48\x81\x6e\xc2\xc6\x7e\x93\x5f" \
    "\x32\xc9\xfc\x7e\x9f\x99\xf7\x9b\x21\x58\x97\x2b" \
    "\x57\x7e\xbc\x19\x08\xf8\xd4\xba\xba\x00\x0c\x83" \
    "\x62\x71\xf1\x09\x0a\x05\x63\x80\x73\xd1\xdb\xd9" \
    "\xb9\x27\xb3\xbe\xbf\xe2\x0c\x0f\x5f\x4f\xa4\xd3" \
    "\x93\x62\x75\xb2\x59\x5d\x5c\xbd\x3a\x26\x86\x86" \
    "\xae\x75\x3f\x33\x0c\x00\xe7\xcf\x27\x13\x63\x63" \
    "\xe3\x6b\x70\xc6\x4c\x31\x32\xf2\x93\x38\x7b\xf6" \
    "\xdb\xf0\xff\xc2\xcf\x9c\xb9\x9c\x18\x1d\xd5\xd6" \
    "\xe0\xb9\xdc\x92\x38\x7d\xfa\xd2\x4c\x45\x40\x7f" \
    "\xff\xc5\xc4\xc9\x93\x5f\xab\xe5\xee\x9d\x3a\x35" \
    "\x34\xa4\x69\x53\x2b\x30\xe7\x5c\x24\x93\x63\xa2" \
    "\xbf\xff\x62\xd9\xfe\xd5\x91\x5c\x2e\x67\x37\x21" \
    "\x24\x15\x8f\x0f\xae\x69\x8e\xc7\x07\xd5\xaa\x2a" \
    "\x6f\x78\xeb\xd6\x26\x58\x96\x0d\xcb\xb2\x61\xdb" \
    "\x1c\xb5\xb5\x7e\x50\xca\xc2\x15\xc0\x0e\x44\xa3" \
    "\xed\x0a\x21\x24\x15\x8b\x0d\xa8\x00\x10\x8b\x0d" \
    "\xa8\x7e\xbf\x2f\xb5\x7f\xff\x5b\x8a\x2c\x4b\x60" \
    "\xcc\x04\xa5\x0c\x94\x32\x38\x1c\x32\x8a\x45\xa6" \
    "\x6c\x08\x17\x8b\x0c\x7e\xbf\x0f\x1d\x1d\xbb\x15" \
    "\x42\x48\xaa\xa7\xe7\xcb\xee\x12\xda\xae\x48\x92" \
    "\x04\x4a\x4d\x50\x6a\x82\x31\x0b\x8c\x59\x98\x9d" \
    "\x9d\x07\xa5\x2c\xb3\x21\x9c\xcd\xea\x7a\x09\xaf" \
    "\x46\x47\xc7\x6e\xa5\xb1\x31\x98\x88\x46\xdb\x15" \
    "\x59\x96\xc1\x98\xf9\x9f\x9a\x99\x99\x83\x61\xd0" \
    "\x0d\x61\x79\xc7\x8e\x7d\x6d\x5e\xaf\x5b\x0d\x06" \
    "\x15\x78\x3c\x6e\xb4\xb6\x36\x43\x92\x24\xd8\xb6" \
    "\xbd\xa6\x28\x35\x31\x3b\xfb\x08\xf5\xf5\xb5\x98" \
    "\x9e\xbe\xa7\x7e\x75\xf0\xae\xf7\xc3\xce\xfa\xc9" \
    "\x2f\x2e\xcf\x17\xcb\xbe\x31\x63\x66\x6f\x32\xf9" \
    "\xb3\x9e\xcd\xfe\xbd\x72\xec\x52\x59\x2b\x65\x18" \
    "\x0c\x99\xcc\x1c\xf2\xf9\x02\x84\x10\xf8\xe0\x95" \
    "\x71\xd5\x15\x72\xf6\x99\x16\x52\xb7\xfb\x5e\x5e" \
    "\xb3\x6f\x21\x84\x02\x00\x04\x00\x8e\x1c\xf9\x54" \
    "\xad\xaa\xf2\xa4\xf6\xee\x55\x95\x6d\xdb\x9e\x87" \
    "\xc3\xe1\x78\xda\x06\x00\x30\x0c\x0a\xd3\xb4\xe0" \
    "\x74\x3a\x40\x26\x4e\xc0\xcf\xbe\x83\xfb\xf1\x5f" \
    "\x70\xbe\xba\x05\x0f\xc6\xb9\xc6\x39\x22\xaf\x1f" \
    "\xbd\xa3\xaf\x7e\x00\x79\x7a\x71\xf8\xf0\x71\x55" \
    "\x08\xd1\x57\x57\x17\x08\x87\x42\x75\xa8\xae\xf6" \
    "\x22\x97\x5b\x02\x63\x16\x0e\x1c\x78\x1b\x81\x40" \
    "\x35\x8c\x74\x1c\xbe\xc2\x08\x6a\x0b\x0f\x11\x94" \
    "\x4d\xe4\xe0\x84\xd1\xd2\x84\x3f\x6f\x09\x8d\x73" \
    "\x44\xf6\x1c\xff\x17\x27\x58\x97\xae\xae\x63\x2d" \
    "\x00\x5a\x00\x84\x01\x5c\x03\xa0\x84\x42\x9b\x12" \
    "\x07\xd5\x8c\xa2\x98\x49\x34\xba\x16\xa0\xb8\x00" \
    "\x69\x79\x72\xd1\x22\xc8\x07\x82\x98\xd6\x88\xc6" \
    "\xb9\x88\xbc\xf3\xc9\x84\x5e\x16\x2e\x97\x0b\x1f" \
    "\xed\xea\x79\x61\x8b\xf1\x71\x5b\x93\x0e\x9f\x4b" \
    "\x06\x59\x37\x55\xa0\x36\x16\x44\x0d\xee\xdc\x94" \
    "\x34\xce\x11\xe9\x8c\x4d\xe8\x15\xc1\x97\x8e\xbe" \
    "\xa4\x70\x8e\xd4\xce\x5d\x5c\x6d\xde\x2c\x96\xcf" \
    "\xba\x3c\xca\x6c\x00\x02\xb6\xcd\xf1\x20\xeb\x44" \
    "\x3a\x2d\x6b\x9c\x23\x22\x57\x02\x0f\xde\xc8\x16" \
    "\xdf\x7f\xf3\xb9\x73\xf7\xef\x91\x68\x55\x8d\x68" \
    "\x50\x9a\x3d\x80\xd7\x05\x50\x0b\x28\x30\x60\x61" \
    "\x09\x52\xce\x80\x5f\x21\x90\xdc\xa4\x61\xee\xa1" \
    "\xdc\x26\x55\x02\x03\xc0\x7b\x7d\x13\xba\x69\x89" \
    "\xc8\x8d\x51\x49\xfb\xfd\x97\x22\x50\xed\x06\xf2" \
    "\x45\x60\x89\x02\xf3\x79\xc0\xe4\xc0\xdd\x05\xb4" \
    "\x36\x18\x70\x3a\xec\x77\x2b\x86\x01\xe0\xd0\x89" \
    "\x49\xdd\xb4\x10\xf9\xfe\xba\xa4\x4d\xa5\x1e\x03" \
    "\x36\x07\x7c\x2e\xa0\x68\x01\x05\x5a\xfa\x3b\x0d" \
    "\x06\x97\xcc\x51\xd1\x2a\x56\xe7\x9b\x74\xb6\xd8" \
    "\xb9\x33\x78\xee\x8f\x8c\x14\xad\x11\x46\x43\xd0" \
    "\x4d\x81\x37\x5a\x4a\x6b\x21\x00\x65\xc0\x0f\x53" \
    "\xbe\xca\x3e\x5e\xb9\xc4\x0f\x6d\x57\x38\x47\x6a" \
    "\xdf\x8b\x39\xf5\xb5\xcd\xf9\x12\x6a\x4b\x18\xfe" \
    "\x75\x13\xee\xe7\xdc\xbd\xcf\x0c\x03\xc0\x67\x5d" \
    "\xdb\x15\xce\x31\xe4\x77\x5b\xe1\x80\xc7\xc2\xa3" \
    "\x27\x2e\x9d\xd9\xd2\xe7\xc7\x2e\xfc\xd6\xf3\x0f" \
    "\x73\xdc\xfe\x36\x28\xf8\xc9\xbd\x00\x00\x00\x00" \
    "\x49\x45\x4e\x44\xae\x42\x60\x82"
image4_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x03" \
    "\x69\x49\x44\x41\x54\x38\x8d\xb5\x95\xcf\x6f\xd3" \
    "\x66\x18\xc7\x3f\xa9\x13\x37\xa4\xa5\x75\x55\xe8" \
    "\x0f\x14\x81\xa3\x82\x44\x33\xa9\x87\x4d\x8a\x76" \
    "\xa0\x6a\x77\x80\xc3\x0e\x6d\x86\x98\x06\x8a\xa6" \
    "\x4e\x65\x13\xd7\x56\x48\xf9\x0b\x40\x42\x5c\x82" \
    "\xc4\x3f\x80\x34\xe5\x50\x71\xa0\xbb\x20\x81\xa0" \
    "\x0a\x4c\x74\x2b\x12\xa3\x39\xb4\xab\xd4\xaa\x71" \
    "\x58\x12\x36\x3a\xba\xe0\xc4\xf9\x59\xe7\xdd\xc1" \
    "\x69\x48\x9a\x04\x6d\x07\xbe\xd6\x63\x5b\x7e\xfd" \
    "\x7e\x9e\xc7\xef\x8f\xaf\x6d\x42\x08\x3e\x86\xec" \
    "\x00\x36\x9b\xad\x75\xeb\x65\xfc\x54\x98\xc6\x44" \
    "\xa5\xc2\x24\x56\x0d\x11\x40\x03\x7e\x22\xcc\x62" \
    "\xab\x6e\x42\x08\x6c\x42\x88\x66\xf0\x0f\xf8\xa9" \
    "\x10\x42\x42\xc5\x0d\x0c\xc2\x84\x7b\x02\x80\xe8" \
    "\xeb\x28\xe9\x44\x1a\xe2\x40\x09\x0d\x98\x3f\x98" \
    "\x40\x08\x51\x3d\xd5\xeb\x7b\x42\xcc\x22\x08\x21" \
    "\x2e\xfe\x76\x51\x3c\x4d\x3f\x15\xe9\xbd\x74\x43" \
    "\x44\xb3\x51\x11\x5c\x0f\x8a\xde\x5b\xbd\x82\x00" \
    "\x82\x00\xa1\x0f\x57\x7c\x99\x10\x12\x73\xa7\xbf" \
    "\x3c\xcd\x8d\x33\x37\xf0\x76\x79\x3f\x34\x8c\xe8" \
    "\x7b\x3a\xc1\x9f\x83\x2c\xdd\x5d\x82\x12\xb7\x08" \
    "\x33\xdf\x0c\xfe\x0e\x3f\x82\x7b\x23\xfe\x11\x6e" \
    "\x4f\xdc\xe6\xb0\x74\x18\x80\xb5\xd8\x1a\xdd\xb6" \
    "\x6e\xd4\x7e\x15\xed\x6f\x8d\xa1\xe1\x21\x3a\x9d" \
    "\x9d\x0d\x09\xae\xfd\x72\x8d\x07\x3f\x3e\x00\xf8" \
    "\x8a\x30\x8b\x8d\xe0\x6f\x89\xb9\x3e\x75\xa9\x37" \
    "\xbf\xb9\xc9\xa0\x3c\x48\xfc\x75\x9c\x53\x1d\xa7" \
    "\x98\xf2\x4e\x35\x40\xca\xa2\xcc\xa3\x77\x8f\x30" \
    "\x4c\xa3\xf6\x2c\x6b\x66\x09\x2e\x04\xd9\x59\xd9" \
    "\xd1\x08\xe3\x11\x42\xd0\x01\x40\x00\x3f\x76\xd4" \
    "\xf1\x33\xe3\x98\x98\x6c\xeb\xdb\x8c\xf7\x8c\x37" \
    "\x41\x01\x1c\x36\x07\x79\x33\x4f\xaa\x94\xaa\x85" \
    "\x6e\xea\x4c\x7d\x31\x05\x32\x2a\x01\xfc\x50\x5d" \
    "\x6e\xc0\x34\x27\x40\x55\x54\x52\xa5\x14\x03\xbb" \
    "\x03\xf8\x3e\xf3\xd5\x60\x4f\xf4\x27\xc4\x0a\x31" \
    "\x86\xe5\x61\xf2\x95\x3c\xcf\xb3\xcf\x6b\x6d\xeb" \
    "\xd9\x75\x36\x8d\x4d\xb4\x9c\x06\x27\x80\x4d\xa6" \
    "\x81\xc5\x7d\xb0\xda\x77\xbc\x0f\x43\x18\x18\x25" \
    "\x83\x19\xf7\x4c\xad\xe3\xf5\xc4\x75\x36\xf2\x1b" \
    "\x0d\x55\xe7\xd2\x39\x7a\xf7\x7a\x39\xaa\x1c\x25" \
    "\x93\xc9\xb0\x91\xab\xb6\x0f\x01\x9b\xa8\xf5\x15" \
    "\x4f\x8a\x6e\x41\xb2\x94\x04\x60\x74\x70\x14\x80" \
    "\xad\xc2\x16\x8f\xdf\x3d\xb6\x86\x20\xeb\xe0\xec" \
    "\xa1\xb3\x8c\xb9\xc6\xf0\x7d\xe2\x43\x71\x29\xb5" \
    "\x44\xb6\xa5\xea\xaa\xb2\xe6\x7b\xb2\x1e\x4c\x51" \
    "\x14\x49\x94\x12\x0d\x95\xed\xee\xed\xd6\x9e\x5d" \
    "\x39\x74\x85\xab\x63\x57\x9b\xc6\xbc\x9d\x3a\xaa" \
    "\xd7\x48\x31\x53\x24\x59\x4c\x92\x2c\x26\x89\x17" \
    "\xe3\x00\xf8\xba\x7d\x1c\xb1\x1f\xe1\x55\xe1\x15" \
    "\x49\x39\xd9\x9e\xe2\xa8\x46\xce\x62\xd5\x83\xb5" \
    "\xca\x9f\x15\xf2\xd5\xe3\xce\xce\x9d\x5a\x9f\xfb" \
    "\x23\xf7\xb9\x64\xbb\xc4\xcb\x3f\x5e\xa2\xe9\x5a" \
    "\x13\x33\xa2\x47\x40\xc6\x8a\xbf\x2c\x16\x50\xdd" \
    "\xd2\x01\xfc\xcc\x22\xa4\x65\x49\x48\x2f\x24\xd1" \
    "\x1f\xed\x17\xab\xb9\x55\xf1\x5f\x14\xc9\x44\x84" \
    "\xf4\x42\x12\xd2\xb2\x24\x98\x45\x10\xc0\xff\x7e" \
    "\x1d\x87\x59\xa4\x88\x26\xaf\xca\x28\x76\x6b\x52" \
    "\xce\x6f\x9f\x67\xd9\x58\x6e\xf9\xe5\x6b\x85\xb5" \
    "\xda\xfd\x8a\xb1\x82\x62\x57\x90\x57\x65\x28\xa2" \
    "\xed\x1b\x92\xbd\xee\xfd\xf9\xfc\xb3\xfc\xbd\x3e" \
    "\xb5\x0f\xd7\x71\x17\x00\x33\xda\x0c\x5e\xa7\x97" \
    "\x73\x3d\xe7\x00\xd0\x4d\x9d\x87\x99\x87\x24\x4a" \
    "\x09\x2e\x28\x17\x70\xcb\x6e\x16\xfe\x59\xa0\x33" \
    "\xd9\xc9\xdb\x67\x6f\x01\xcb\x2b\x80\x03\x26\x14" \
    "\x20\x24\x39\xa5\xb9\x93\x5f\x9f\xa4\x47\xed\x69" \
    "\x3d\x51\x07\xa4\x6b\x3a\x5b\x77\xb7\x30\x0b\x66" \
    "\x1b\x13\xda\x97\x65\x81\x73\x9e\x49\x0f\x9e\xcf" \
    "\x3d\x38\x9c\x8e\x96\xc0\x72\xa1\x4c\xec\xd7\x18" \
    "\xb1\x48\x0c\x78\xef\x6c\xed\xc1\x16\xdc\x0f\x84" \
    "\x1c\x4e\x87\x7a\x6c\xf4\x18\x03\x9e\x01\xba\x94" \
    "\x2e\x00\x8c\xb4\xc1\x9b\xd8\x1b\x52\xbf\xa7\x28" \
    "\x17\xca\x1a\x6d\x8c\xbe\x35\xb8\x31\xc1\x34\xa0" \
    "\x52\xdd\x51\xfc\x9f\x5f\xd3\xc7\xd0\xbf\x81\xd0" \
    "\xcc\x10\xc8\x90\x7f\x4a\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image5_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x18\x00\x00\x00\x18" \
    "\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\x00\x00\x04" \
    "\x59\x49\x44\x41\x54\x48\x89\x9d\x95\x6d\x4c\x5b" \
    "\x55\x18\xc7\x7f\xe7\xf6\xb6\x40\x81\x52\xc0\x01" \
    "\xc2\x10\x0d\x64\xbe\x20\x81\x40\x27\xc8\x44\xfd" \
    "\x00\x99\x31\x23\x59\x34\xa8\x8b\xce\xf8\x36\x20" \
    "\x7e\x70\xc6\xf9\x92\xf8\xc1\xc4\x64\x71\x26\xcb" \
    "\xbe\x68\x62\x34\xd1\x2f\xcb\xa6\xb8\xc4\x18\x30" \
    "\x4e\xa3\x71\x33\xd1\x90\xb0\x49\x22\x51\x47\xbb" \
    "\x52\x06\x03\x79\x69\x68\xe9\x6d\xa1\xaf\xdc\x5e" \
    "\x3f\xdc\x7b\xe1\xca\x18\x9b\x3e\xc9\xcd\x69\x7b" \
    "\xce\xf9\xfd\x9f\x9e\xe7\xff\xdc\x03\xdb\x87\x00" \
    "\x64\x40\xb3\x3c\xb7\x00\x39\xc6\x1c\x80\x94\xe7" \
    "\x6e\x32\xe7\x76\x00\xb9\x96\xb9\x1b\xc2\x35\x40" \
    "\x93\xe5\x62\x0d\xd8\x03\xb4\x02\xbb\x00\x17\x20" \
    "\x01\x22\xb7\xf8\x4e\xab\xf8\xfd\x40\x19\x60\x33" \
    "\x21\xd2\x36\x02\xeb\x8b\x8a\x0a\x5b\x31\x32\x4f" \
    "\x01\x0a\x90\x36\x80\xb6\xe4\xb2\xcf\xba\xe7\x9a" \
    "\x7f\x70\x3d\x01\x01\x64\xcc\x2f\xa1\xe5\xef\x41" \
    "\x3f\xaa\x55\x60\x05\x50\x01\xb9\xaa\xab\x37\x53" \
    "\xd5\xd5\x6b\xdd\x67\x37\x12\x13\x56\xd0\x56\x21" \
    "\xcb\xf9\xc5\x19\x35\x1e\xc1\xed\x76\x93\x97\x97" \
    "\x87\xa8\xdf\xc7\xad\xbb\xeb\xd7\x17\xcc\x5f\xfc" \
    "\x8b\xaa\xdd\x2d\xb4\x95\xdc\xce\x07\xaf\xef\xb5" \
    "\xee\x6d\x04\xa6\x80\x38\xa0\x6e\x25\x20\x39\xaa" \
    "\xef\x50\x1b\x3b\x7a\x10\xb2\xe0\x95\x23\xaf\x51" \
    "\xe0\x90\x98\x8c\xa6\xc9\x11\x82\x50\x52\xc5\x17" \
    "\x4e\x11\x5c\x9a\xa0\x51\xe4\x73\xfc\x85\x07\x10" \
    "\x62\xcb\x3c\x2b\x00\x65\xf3\x8c\x54\xd5\xd5\xab" \
    "\x3e\xd4\x7b\x84\x67\x9b\x4a\xc8\x97\x05\x17\x16" \
    "\x93\x78\x83\x71\x26\xa2\x59\xd0\xb2\xfc\xfd\xc7" \
    "\x08\x95\x52\x2e\xe7\x8f\x3d\x05\xc0\xe7\x9d\x9d" \
    "\x8c\x5f\xbe\xcc\x87\x73\x73\x28\xaa\x6a\x72\xba" \
    "\x81\x69\xe0\xaa\x6c\x85\x97\x94\x56\xaa\xfd\x6f" \
    "\xbe\xcc\x13\xbb\x4a\x38\x1b\xb8\xc2\x39\xef\x24" \
    "\xbe\xa0\x8a\x96\x16\x94\xde\xd5\x40\xd6\x3b\x4c" \
    "\xb3\xad\x8c\x2f\xde\xdb\x0f\xc0\x78\x4b\x0b\x2b" \
    "\x8a\xc2\xd1\x99\x99\x7e\x20\x86\x6e\x82\x35\xf4" \
    "\x3a\xad\x02\x69\x53\x40\x38\x1c\x0e\xf5\xd5\xc3" \
    "\x87\x79\xb2\xa6\x90\x53\x27\x4f\x71\xf2\xeb\x1f" \
    "\x58\x0e\xae\xe2\x7a\xf8\x51\x5c\x4e\x37\x79\x92" \
    "\x9d\x72\x4d\x87\x6b\x9a\x86\xd7\xe3\x61\x38\x99" \
    "\xa0\x2f\x10\xe8\x07\xe6\x8c\x8c\x63\xe8\x06\x48" \
    "\x99\x82\xa6\x80\xad\xb3\xb3\x93\xf6\xf6\xfb\x38" \
    "\x71\xe2\x23\x06\x07\x07\x88\x44\x42\x48\xa9\x34" \
    "\x35\x43\x3e\x0e\xee\x28\x80\x85\x0b\xf4\x0e\x7e" \
    "\x06\x80\xd7\xe3\x01\x40\x4d\xa5\x41\xb7\xed\xb4" \
    "\x51\xd8\x04\x1b\x3d\x91\x05\x34\x09\x10\x4e\xa7" \
    "\x33\x53\x57\x5b\x4b\x20\x30\xc1\xd9\x6f\xbe\x45" \
    "\x56\xc2\x3c\x58\x50\x40\x5c\xcb\xf2\x76\x53\x39" \
    "\xcf\x1c\xec\xa0\xbb\xbb\x15\xe5\xb7\x11\xb4\x6c" \
    "\x1a\x80\x5f\x14\x85\xbe\x40\xa0\x0f\x08\x01\x4b" \
    "\x06\x5c\xb5\x3c\x1a\xe8\xde\x96\x5c\x2e\x17\x76" \
    "\x87\x83\x33\x67\x06\x98\x99\xf3\x02\x30\x9b\x48" \
    "\xf0\x49\xf7\xf3\xec\x29\x9b\xc2\x51\x5b\x47\xea" \
    "\xe7\x9f\x48\x14\x7d\xc5\xdc\xaf\x3e\xfc\x75\x2e" \
    "\x18\x05\x20\x0a\x2c\x18\xc7\x91\x46\xef\xf0\x14" \
    "\x7a\x0f\x6d\x08\x64\x33\x19\x46\x86\x87\xf9\x73" \
    "\x7c\x1c\x4f\x51\x11\x17\x23\x11\xb4\x6c\x16\xc9" \
    "\x66\x63\xa9\xae\x9a\x03\xbe\x30\x71\xc9\x49\x7e" \
    "\xf7\x22\x00\x0b\xa3\x71\xf3\xec\x23\x86\x48\x14" \
    "\xd8\x09\x14\x03\xcb\x46\xa1\x75\x81\x4f\xef\xb9" \
    "\x3b\xbd\xb7\xa9\x8e\x9c\xca\x52\x5e\x9c\x9c\x60" \
    "\x68\x21\xa8\x5b\xca\x66\x43\xd3\x34\x84\x10\xec" \
    "\x77\x97\xe3\x7c\x6c\x27\x65\xf7\xaa\xf8\x63\x33" \
    "\xbc\xb1\x38\x0b\xf0\xf1\x26\x8b\x97\x03\x61\x2b" \
    "\x1c\x40\xce\x71\xbb\x29\x7b\xa4\x0d\x29\x19\xc3" \
    "\x69\x59\xad\x69\xeb\x6b\x10\x40\x71\x8f\x40\x5a" \
    "\x5b\xe1\xb9\x63\x31\xa2\x2b\x2a\x9b\x62\x1f\xfa" \
    "\x1b\x36\x61\x3d\x1e\x00\x79\x62\x31\xc8\xd2\xef" \
    "\xb3\xa4\x02\x7e\x8e\x56\x97\x23\x84\x58\x87\x0b" \
    "\x21\xb8\xd4\xd1\x8c\xdd\x93\x87\x9a\x1c\x43\x5d" \
    "\x9b\x62\x29\xfc\x2f\xf0\x4b\xe8\x2e\x8a\x03\x41" \
    "\x36\x6c\xba\x1e\xb2\x96\xcd\xa2\xd8\x24\x88\x6b" \
    "\x08\x39\x17\x5f\x5b\x0b\xf9\x76\x1b\x09\x55\xe3" \
    "\x92\xa7\x05\x7b\xbb\xc0\xf5\xf4\x18\x31\x45\xe6" \
    "\x9d\xd3\x6e\x1a\x1a\x32\xcc\x2e\xa4\xfa\x0d\x70" \
    "\x08\x98\x37\x46\x05\x48\x5a\xb3\x07\x90\xc7\x9b" \
    "\x15\x6a\x0e\xf9\x89\xbe\xef\x42\xc6\x01\xae\x52" \
    "\xfc\x8d\xf5\x94\xbe\x35\x46\x32\xb6\x82\xdd\x7e" \
    "\x85\x68\x3a\x97\xe3\xa7\xed\x78\xbd\x71\xce\x9d" \
    "\x8f\xf5\x1a\xd0\x69\x74\x7b\x46\xd1\x9d\xa3\x6e" \
    "\x86\x83\xee\x22\x84\x3a\x43\xf1\xbb\x32\x64\x40" \
    "\xcb\xfa\x11\x39\xa5\xa4\x96\x13\x44\x56\x43\x8c" \
    "\xfa\xcb\x18\x18\x8a\xb3\x12\xcd\x98\xf0\x39\x60" \
    "\xc2\x18\x13\xd7\x03\x5b\xeb\x57\xd1\xf3\x78\xc9" \
    "\xbc\xf5\xc7\x50\xd8\xb8\x0a\xd6\x24\x72\x72\xf5" \
    "\x7b\xe7\xbb\x1f\xc3\x87\x8c\xcc\xfd\x06\x3c\x8e" \
    "\xde\xad\xdb\x86\x00\x9c\x40\x15\x70\x1b\x7a\xa3" \
    "\xd8\x81\x2f\xdd\x6e\x07\x91\x48\x1a\xa0\xcf\x38" \
    "\x86\x25\xe0\xea\x7f\x81\x9b\x02\x12\xfa\x35\xe7" \
    "\x32\x32\x34\xe3\x80\x01\x59\xe6\xda\x42\xde\x14" \
    "\xdc\x14\x30\x47\x9b\x21\x52\x81\xde\x91\xc2\x80" \
    "\x87\xb9\x41\x21\x6f\x46\xc0\xfc\xec\x00\x0a\x8d" \
    "\x71\x0d\xfd\x9d\xfe\xbf\xc0\x66\xfc\x03\xa8\xd9" \
    "\xc0\xef\x1b\x40\x07\x9f\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"

class MainWinDesign(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        self.image2 = QPixmap()
        self.image2.loadFromData(image2_data,"PNG")
        self.image3 = QPixmap()
        self.image3.loadFromData(image3_data,"PNG")
        self.image4 = QPixmap()
        self.image4.loadFromData(image4_data,"PNG")
        self.image5 = QPixmap()
        self.image5.loadFromData(image5_data,"PNG")
        if not name:
            self.setName("MainWinDesign")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        MainWinDesignLayout = QGridLayout(self.centralWidget(),1,1,11,6,"MainWinDesignLayout")

        self.taskStack = QWidgetStack(self.centralWidget(),"taskStack")
        self.taskStack.setSizePolicy(QSizePolicy(5,7,0,0,self.taskStack.sizePolicy().hasHeightForWidth()))

        self.page = QWidget(self.taskStack,"page")
        self.taskStack.addWidget(self.page,0)

        MainWinDesignLayout.addWidget(self.taskStack,0,0)

        self.about = QAction(self,"about")
        self.about.setIconSet(QIconSet(self.image0))
        self.editServerList = QAction(self,"editServerList")
        self.editServerList.setIconSet(QIconSet(self.image1))
        self.exitItem = QAction(self,"exitItem")
        self.exitItem.setIconSet(QIconSet(self.image2))
        self.menuConfigurePlugins = QAction(self,"menuConfigurePlugins")
        self.menuConfigurePlugins.setIconSet(QIconSet(self.image3))
        self.reload = QAction(self,"reload")
        self.reload.setIconSet(QIconSet(self.image4))
        self.selectLanguage = QAction(self,"selectLanguage")
        self.selectLanguage.setIconSet(QIconSet(self.image5))
        self.togglePluginList = QAction(self,"togglePluginList")
        self.togglePluginList.setToggleAction(1)
        self.togglePluginList.setOn(0)
        self.togglePluginList.setEnabled(1)




        self.menubar = QMenuBar(self,"menubar")


        self.PopupMenu_3 = QPopupMenu(self)
        self.reload.addTo(self.PopupMenu_3)
        self.PopupMenu_3.insertSeparator()
        self.exitItem.addTo(self.PopupMenu_3)
        self.PopupMenu_3.insertSeparator()
        self.menubar.insertItem(QString(""),self.PopupMenu_3,1)

        self.PopupMenu = QPopupMenu(self)
        self.editServerList.addTo(self.PopupMenu)
        self.menuConfigurePlugins.addTo(self.PopupMenu)
        self.selectLanguage.addTo(self.PopupMenu)
        self.menubar.insertItem(QString(""),self.PopupMenu,2)

        self.PopupMenu_2 = QPopupMenu(self)
        self.about.addTo(self.PopupMenu_2)
        self.menubar.insertItem(QString(""),self.PopupMenu_2,3)


        self.languageChange()

        self.resize(QSize(479,321).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.about,SIGNAL("activated()"),self.showAboutLuma)
        self.connect(self.exitItem,SIGNAL("activated()"),self.quitApplication)
        self.connect(self.editServerList,SIGNAL("activated()"),self.showServerEditor)
        self.connect(self.menuConfigurePlugins,SIGNAL("activated()"),self.configurePlugins)
        self.connect(self.reload,SIGNAL("activated()"),self.reloadPlugins)
        self.connect(self.selectLanguage,SIGNAL("activated()"),self.showLanguageDialog)


    def languageChange(self):
        self.setCaption(self.__tr("Luma"))
        self.about.setText(self.__tr("About Luma..."))
        self.about.setMenuText(self.__tr("About Luma..."))
        self.about.setAccel(self.__tr("Ctrl+A"))
        self.editServerList.setText(self.__tr("Edit Server List..."))
        self.editServerList.setMenuText(self.__tr("Edit Server List..."))
        self.editServerList.setAccel(self.__tr("Ctrl+E"))
        self.exitItem.setText(self.__tr("Exit"))
        self.exitItem.setMenuText(self.__tr("Exit"))
        self.exitItem.setAccel(self.__tr("Ctrl+X"))
        self.menuConfigurePlugins.setText(self.__tr("Configure Plugins..."))
        self.menuConfigurePlugins.setMenuText(self.__tr("Configure Plugins..."))
        self.menuConfigurePlugins.setAccel(self.__tr("Ctrl+C"))
        self.reload.setText(self.__tr("Reload Plugins"))
        self.reload.setMenuText(self.__tr("Reload Plugins"))
        self.reload.setAccel(self.__tr("Ctrl+R"))
        self.selectLanguage.setText(self.__tr("Language..."))
        self.selectLanguage.setMenuText(self.__tr("Language..."))
        self.selectLanguage.setAccel(self.__tr("Ctrl+L"))
        self.togglePluginList.setText(self.__tr("Hide/Show pluginlist"))
        self.togglePluginList.setMenuText(self.__tr("Hide/Show pluginlist"))
        self.togglePluginList.setAccel(self.__tr("Ctrl+P"))
        if self.menubar.findItem(1):
            self.menubar.findItem(1).setText(self.__tr("Program"))
        if self.menubar.findItem(2):
            self.menubar.findItem(2).setText(self.__tr("Settings"))
        if self.menubar.findItem(3):
            self.menubar.findItem(3).setText(self.__tr("Help"))


    def quitApplication(self):
        print "MainWinDesign.quitApplication(): Not implemented yet"

    def showServerEditor(self):
        print "MainWinDesign.showServerEditor(): Not implemented yet"

    def showAboutLuma(self):
        print "MainWinDesign.showAboutLuma(): Not implemented yet"

    def loadPlugins(self):
        print "MainWinDesign.loadPlugins(): Not implemented yet"

    def unloadPlugins(self):
        print "MainWinDesign.unloadPlugins(): Not implemented yet"

    def configurePlugins(self):
        print "MainWinDesign.configurePlugins(): Not implemented yet"

    def reloadPlugins(self):
        print "MainWinDesign.reloadPlugins(): Not implemented yet"

    def showLanguageDialog(self):
        print "MainWinDesign.showLanguageDialog(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("MainWinDesign",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = MainWinDesign()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
