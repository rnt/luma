# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/plugins/template_plugin/AddTemplateDialogDesign.ui'
#
# Created: Sun Aug 29 00:52:47 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.12
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x30\x00\x00\x00\x30" \
    "\x08\x06\x00\x00\x00\x57\x02\xf9\x87\x00\x00\x08" \
    "\xa0\x49\x44\x41\x54\x78\x9c\xc5\x99\x7d\x6c\x9d" \
    "\x55\x1d\xc7\x3f\xcf\x73\xdb\xdb\xde\xf6\xbe\xb4" \
    "\x83\xad\x0c\xe6\x06\x6e\x2c\x33\xd1\x4d\xa2\x53" \
    "\x23\x26\xc4\x68\x90\xec\x0f\x94\x40\x04\x45\x32" \
    "\xff\x41\x12\x70\x43\x12\x13\xfe\x51\x91\x3f\x48" \
    "\x50\x20\x90\x18\x88\x71\x89\xd0\x39\x89\x28\x32" \
    "\x90\xb9\x31\x5e\x52\xac\x5d\xdb\x31\xec\x06\x1d" \
    "\x74\x5b\xdf\xd6\x7b\xd7\xae\xdd\x6d\x7b\x7b\x5f" \
    "\x9f\x97\xfb\x9c\x73\xfc\xe3\xdc\x96\x8e\xf5\xbe" \
    "\xf4\xde\x4e\x7f\xc9\x2f\x4d\x9f\xe7\x39\xbf\xf3" \
    "\xfb\xfe\xce\xef\xf5\x5c\x43\x29\x45\x31\x32\x0c" \
    "\xa3\xe8\xbb\xc5\xf4\xdc\x73\x5d\x37\x28\xa5\x6e" \
    "\xf3\x3c\x6e\x92\x52\x6d\x93\x52\x45\x3c\x4f\x22" \
    "\x84\xc4\xf3\x34\x0b\x21\x92\xae\x9b\xef\xb7\x6d" \
    "\xa7\x2b\x93\x49\xbe\xfa\xfc\xf3\xf7\xfe\x07\x10" \
    "\x40\x71\x05\x16\x51\x31\x3d\x8d\x6a\x01\xbc\xf0" \
    "\xc2\xb1\x16\x21\xc4\x43\x42\xb0\x53\x4a\xb5\x61" \
    "\xb1\xc2\x18\x26\x8d\x4d\xcd\x08\x21\x91\x52\x31" \
    "\x37\x93\xc4\xb6\x9d\x02\x18\x85\x10\x92\x7c\xde" \
    "\x8b\x59\x56\xee\xc5\x68\xf4\xf8\x33\x1d\x1d\x4f" \
    "\xc7\x0b\x60\xfe\x37\x00\xda\xdb\xdf\x7b\x48\x08" \
    "\x1e\x11\x42\x45\x84\x90\x98\x75\x7e\x42\x2d\xad" \
    "\x84\x5b\x57\x11\x6a\x89\x14\x95\x37\x3d\x35\xc3" \
    "\xf8\xd8\x79\xa2\xa3\xe3\x24\xe7\x32\x05\x40\x22" \
    "\x95\xc9\x24\x9e\x78\xe5\x95\xfb\x9f\x02\x1c\x40" \
    "\x5e\x36\x00\xfb\xf6\xf5\xb5\x08\x21\x5f\x95\x52" \
    "\xdd\x24\x84\xa4\xa1\x29\xc8\x95\x6b\xd7\xd1\x1c" \
    "\x0e\x53\xe7\x83\x48\x08\x82\x01\x68\x0e\x40\x5d" \
    "\xdd\x27\xeb\x6c\x07\x1c\x17\xe6\x32\x90\x4c\xeb" \
    "\x67\x93\x13\x71\xfa\x7a\x4f\x12\x3b\x3b\x89\x10" \
    "\x12\xc7\xb1\x8e\x0e\x0e\x1e\xbe\xf3\xe4\xc9\x97" \
    "\xc7\x01\x6f\xc5\x01\xec\xdd\xfb\xde\x0d\x60\xee" \
    "\x97\x52\x6d\x90\xca\xa4\x6d\xfd\x75\x84\x5a\x5a" \
    "\x89\x84\xa0\x6d\x15\xb4\x5d\x51\x54\xcc\x45\xe4" \
    "\x09\x98\x99\x83\xe8\x79\xb0\x5d\x18\x1d\x3a\xc7" \
    "\x5b\x07\x8e\xe0\xd8\x2e\x52\x7a\x13\xf1\xf8\xa9" \
    "\x7b\x3a\x3b\x7f\xdb\x05\xe4\x59\x14\x1f\x35\x01" \
    "\xd8\xb7\xaf\xaf\x45\x29\x35\x2a\x84\x6c\xa9\xf3" \
    "\x07\x58\xb7\x69\x0b\x7e\xbf\x8f\xcd\x1b\xe0\x8a" \
    "\x96\xca\x14\x5f\x8a\xc6\x2f\x68\x20\xd9\x9c\xcb" \
    "\x2b\x2f\xbe\xc9\xf4\x54\x02\xa5\x64\xba\xaf\xaf" \
    "\xfd\x2b\x23\x23\x1d\xa3\x68\x97\x2a\x09\xc0\xac" \
    "\x64\x23\x29\xe5\xbb\x8b\x95\x0f\x87\x7c\x6c\xff" \
    "\x7c\x6d\xca\x03\x5c\xb3\x06\xb6\x6e\x86\xe6\x66" \
    "\x3f\xb7\xff\xf0\x66\x56\xb7\xb5\x62\x18\x66\x68" \
    "\xdb\xb6\x1f\xbc\x06\xb4\x02\x75\xe5\x64\x94\x05" \
    "\xb0\x77\xef\xb1\x47\xa5\x64\x9b\xe9\xf3\xb3\x7e" \
    "\xf3\x16\x82\xcd\x3e\xbe\x70\x3d\xd4\xf9\x6a\x53" \
    "\x7e\x9e\x9a\x03\xb0\xf5\x7a\x08\x06\xfd\xdc\x71" \
    "\xf7\xcd\x84\x23\x41\xea\xea\x1a\x37\xdf\x72\xcb" \
    "\x6f\x1e\x01\xc2\xe5\x74\x2c\xf9\xb2\xbd\xfd\xfd" \
    "\x16\x21\x78\x50\x08\xc9\xd5\xd7\x5e\x4b\x7d\xbd" \
    "\x8f\xeb\xd7\xaf\x9c\xf2\xf3\xd4\x1c\x80\xf5\x6b" \
    "\x21\xd0\xe4\xe7\x3b\xb7\x7e\x1d\x80\x60\x70\xcd" \
    "\x8f\xae\xb9\xe6\x4b\xd7\x01\x8d\xa5\xd6\x96\x04" \
    "\x20\x84\xb8\x4d\x4a\x15\x09\x34\x07\x09\xb5\x84" \
    "\x89\x04\x21\x14\xd4\x91\xb5\xd2\x7c\xd5\x95\xd0" \
    "\xd8\x00\x1b\xae\x6b\xe3\x33\x1b\xda\x30\x0c\x5f" \
    "\x70\xd3\xa6\x6f\x7f\x17\x68\x2e\xa5\x67\x19\x00" \
    "\xea\x7b\x42\x48\x56\xaf\x6d\xc3\x34\xb4\xcf\x0b" \
    "\x71\xf9\xb8\x35\x04\xa6\x01\x5f\xfe\xda\xe7\x00" \
    "\x08\x85\xae\xfe\x26\x10\x04\xea\x8b\xe9\x58\x32" \
    "\x48\x94\xe2\x56\xcf\x93\xac\x5a\xbd\x4a\x7f\xec" \
    "\xd3\x1b\x5d\x2e\x6a\x0a\x80\x99\x84\x0d\x9f\x6d" \
    "\x03\x20\x10\x68\xfd\x06\x10\x02\xfc\x2c\xca\x48" \
    "\x8b\xa9\x24\x00\x21\x24\x81\xa6\x26\xcc\xc2\x39" \
    "\x49\x05\x62\xc9\x3a\xb9\x32\x64\x18\x60\x9a\xd0" \
    "\xd4\xe4\xa7\x6d\x6d\x2b\x53\xe7\x13\x00\x01\xaa" \
    "\x3d\x01\xcf\x53\x18\xa6\x89\x59\xa8\x67\x52\x5e" \
    "\xde\x13\xb0\x1d\x16\xf6\x6a\x6c\xf4\xcf\x3f\xf6" \
    "\x01\x45\x9b\xb2\xb2\x27\x20\xa5\x5a\x38\x81\x9c" \
    "\x0d\xfe\xb2\x99\xb9\x7a\xca\x7b\x2c\xec\x55\x61" \
    "\x23\x5c\x1e\x40\x7c\x6a\x76\x41\xa8\xe3\x42\x5e" \
    "\x54\x2e\x7c\x39\x24\x24\x58\xce\x27\x00\xce\x8e" \
    "\x4c\x55\xb4\xae\x24\x00\xdb\x76\x8e\x18\x86\xef" \
    "\xc6\xd4\x5c\x9a\x96\x55\x21\x14\x90\xb5\x20\xd0" \
    "\x50\xab\xba\x97\x52\xd6\xfa\x44\xf9\xc9\x89\x44" \
    "\x61\xff\x64\x3f\x65\x66\x86\x92\x69\xd4\xb2\x72" \
    "\x07\x3c\x4f\x72\x66\x20\x8a\xcf\x00\x9f\x01\xf9" \
    "\xbc\x3e\x89\x95\x4c\x9f\x39\x5b\xff\x9d\xdf\xa3" \
    "\xb7\x6b\x00\x80\x54\xea\x5c\x37\x60\xb3\x44\x77" \
    "\x5a\x11\x80\x44\x62\x6a\xbf\x10\x92\x33\x03\x31" \
    "\xb2\x59\x0b\xd3\xd4\x56\xca\x7b\xe0\x7a\xe0\xc9" \
    "\xda\xd9\xc9\xeb\xe4\x30\x2f\x3b\x39\x97\xa1\xef" \
    "\xfd\x61\x00\x46\x47\xff\xdd\x09\x64\x01\xb7\x2a" \
    "\x00\xcf\x3e\x7b\xdf\x50\x3a\x9d\xdc\x23\x84\xe2" \
    "\xdd\xb7\x3e\x58\xd8\xc4\x34\x41\xa9\x95\xb1\x3e" \
    "\x70\x91\xdc\x97\x5f\xea\x06\x20\x9d\x9e\x7c\x3b" \
    "\x1a\xed\x1e\x05\x32\xe8\xd6\x7a\xf9\x00\x00\x79" \
    "\xea\x54\xf7\xaf\x3d\xcf\x4b\x47\xc7\xe2\x0c\x7c" \
    "\x14\xc3\x34\xb8\x84\x0d\x43\x3b\xe9\x7c\x9a\x2d" \
    "\xc6\x52\xea\xef\x8c\x25\x64\x98\x06\xf4\x1d\x1b" \
    "\x66\x64\x68\x0a\x29\x45\xf6\xe8\xd1\xe7\x9e\x05" \
    "\x92\x05\x00\x45\xab\x4f\x39\x00\xea\xe0\xc1\x67" \
    "\xa6\xe2\xf1\x73\xbb\x84\x90\xbc\x73\xf8\x03\x5c" \
    "\x37\x7f\x91\xc5\x4c\x13\x7c\x26\xd4\xfb\xc0\x5f" \
    "\x0f\x0d\x7e\xa8\xaf\xbf\x94\x1b\xfc\xfa\x7d\xbd" \
    "\x4f\x7f\xff\x69\x19\x8e\xe3\xf2\x8f\xfd\xef\x03" \
    "\x30\x31\xd1\xf7\x87\x44\xe2\xec\x04\x30\x03\x58" \
    "\x54\x1b\xc4\x05\x12\xed\xed\xf7\xbf\x64\xdb\x56" \
    "\x6f\x36\xeb\xd0\xd9\xf1\xd1\x25\x9b\x7f\x9a\xeb" \
    "\x7c\x97\x72\xb9\x35\x6f\xbe\xf1\x21\x96\xe5\x62" \
    "\xdb\xc9\xfe\x9e\x9e\xdf\xbd\x06\x4c\x17\x4e\xa0" \
    "\x64\xe9\xac\x68\xa0\x01\xdc\x58\xec\xe4\x4f\x84" \
    "\x90\x74\x75\x9e\x21\x39\x97\x5d\xd2\x05\xaa\xe5" \
    "\xb9\x44\x86\xce\x0e\x9d\x79\x4e\x9c\xf8\xf3\x13" \
    "\x40\x02\x98\xa5\x44\xf0\x2e\x17\x80\x3c\x74\xe8" \
    "\xb1\x53\xb9\x5c\xf6\xaf\x42\x48\xde\x3c\xd4\x5f" \
    "\xd6\xa2\xcb\xe1\x37\x0e\x7e\x08\xe8\xc0\x8d\xc5" \
    "\x7a\x47\xd0\xae\x93\xa5\x84\xef\x2f\x17\x00\x80" \
    "\x37\x33\x73\xf6\xd1\x7c\xde\x4b\xf7\x74\x0f\x91" \
    "\x48\x64\x56\x44\xf9\x44\x22\xc3\xd1\x9e\x61\xa4" \
    "\x14\xd9\x8f\x3f\xde\xdf\x8e\xb6\x7e\x92\x12\xb9" \
    "\xbf\x5a\x00\xea\xf0\xe1\x47\xcf\xd8\x76\xe6\x2f" \
    "\x4a\x29\x0e\x1d\xf8\x70\x45\x00\x1c\x3a\xa0\xad" \
    "\x9f\x4a\x8d\xbf\x1d\x8d\xf6\x0c\x15\x00\xd8\x54" \
    "\x78\x63\xb7\x1c\x00\x00\x22\x99\x3c\xf7\x0c\x40" \
    "\x4f\xf7\x30\xb6\xe5\xd6\xe4\xfb\xb6\xe5\xd2\xd3" \
    "\xad\x8b\xd6\xe9\xd3\xff\xfc\x1b\xda\xf2\x29\xca" \
    "\x04\x6e\x2d\x00\x54\x47\xc7\x63\x67\xf2\x79\xeb" \
    "\x25\x80\xde\x9e\xe1\x9a\xac\xdf\xdb\xa3\x95\xd7" \
    "\x45\xab\x67\x14\x98\x43\x0f\x2e\x15\x59\xbf\x1a" \
    "\x00\x00\xc2\xf3\xec\xd7\x00\x7a\x8e\x0c\xe3\x2b" \
    "\xd4\x81\x6a\xb8\xe7\x88\x06\x30\x33\x33\x78\x04" \
    "\x6d\xf9\x0c\xcb\xb0\x7e\xb5\x00\xd4\x81\x03\x0f" \
    "\xfe\x5d\x29\x95\x8a\x46\x13\xcc\xce\x54\x17\xcc" \
    "\xb3\x33\x19\xa2\xd1\x04\x52\x8a\xec\xb1\x63\x7b" \
    "\x3a\x80\x34\xcb\xb4\x7e\xb5\x00\x00\x3c\x21\x9c" \
    "\x83\x00\xa7\x4f\x4f\x55\xe5\xff\xb1\x98\x6e\x99" \
    "\xb3\xd9\x78\x0f\xba\xda\x66\xa9\x30\xf3\xac\x04" \
    "\x00\xa9\x94\x3c\x01\x30\x33\x9d\xad\xea\x04\x62" \
    "\x51\x0d\xc0\xb2\x66\x87\x80\x1c\x3a\xf3\x2c\x7b" \
    "\xe2\xae\x7a\x40\x94\xd2\x3b\x0e\x90\xb3\x5c\xcc" \
    "\x2a\xcc\x90\xb3\x74\x91\x4d\x26\x63\x67\x28\xd3" \
    "\xf3\x97\xa2\xaa\x01\x98\x66\x9d\x04\x88\x8e\xcd" \
    "\x2e\x0c\xe2\xcb\xa1\xe8\xd8\x2c\x00\x86\x61\x4a" \
    "\x74\xcb\x50\xd5\x7d\x47\xb5\x2e\x44\x26\x73\xe1" \
    "\x04\x40\x3c\x9e\xc5\x2a\x9c\x42\xa5\x6c\x59\x2e" \
    "\x63\x63\xda\x85\xc6\xc6\xba\x07\xd1\x99\xa7\x2a" \
    "\x00\x55\xff\xc4\x04\x98\xb7\xdf\xfe\xc7\x4e\xd3" \
    "\xac\xbb\xb1\x9a\x8d\x41\xcf\xbc\xaf\xbf\xbe\xeb" \
    "\x3e\x60\x08\xdd\xff\x14\x05\x51\xd3\xf5\x7a\x11" \
    "\x92\x23\x23\x1d\x77\xe5\xf3\xd6\xb1\x6a\x16\xdb" \
    "\x76\xb2\xbf\xab\xeb\xa9\x5f\xa1\xf3\x7f\x55\x01" \
    "\x0c\x35\xc4\x00\xc0\xf1\xe3\x7f\x9a\xbc\xe3\x8e" \
    "\x2d\xc7\x5d\xd7\xdd\x3e\x3d\x3d\xcd\x52\xec\xba" \
    "\x45\x3b\xe2\x61\xa5\xd4\x38\xba\xef\xb7\xaa\xd5" \
    "\xa1\x16\x17\xe2\xc9\x27\x9f\xbc\xc1\xb6\xed\xbe" \
    "\x9d\x3b\x7f\xcc\x9a\x35\x6b\xf0\x3c\xb1\xc0\x42" \
    "\x88\x8b\xfe\x9f\x7f\x36\x32\x32\xce\x3b\xef\xfc" \
    "\x8b\xa7\x9f\xfe\x05\xc0\x5d\x4a\xa9\xc3\xe8\x1e" \
    "\xa8\x64\x01\x5b\xf1\x9f\x59\x0b\x64\x3e\xfc\xf0" \
    "\xc3\xb3\xe1\x70\x38\x72\xf7\xdd\xf7\x10\x0a\x45" \
    "\x70\x5d\x17\xc7\xf1\x70\x1c\x17\xd7\xcd\xe3\x38" \
    "\x2e\x8e\x93\xc7\x71\xf2\xb8\xae\xcb\xe0\xe0\x30" \
    "\x8f\x3f\xfe\x4b\x26\x26\xc6\xb2\x4a\xa9\x6f\x01" \
    "\xc3\xe8\xe1\xa5\xa4\x0b\x5d\x8e\x18\xe0\x81\x07" \
    "\x1e\xb8\x36\x95\x4a\x45\xd6\xae\xbd\x9a\x86\x86" \
    "\x46\x3c\x4f\xe0\xba\x5a\x79\xdb\x76\xc8\xe5\x6c" \
    "\xb2\x59\x9b\x74\x3a\xc7\xf8\xf8\x05\xc6\xc6\x26" \
    "\xc9\x64\x5c\x36\x6e\xdc\x02\xfa\xde\x7f\x1d\x25" \
    "\xee\x3d\x2b\xa1\x9a\x62\xc0\x75\x5d\x72\xb9\x1c" \
    "\xf5\xf5\x75\x84\x42\xcd\x18\x86\x49\x63\xa3\x7f" \
    "\x49\x17\xb2\x6d\x97\x5c\xce\xfe\xb4\x08\x83\x1a" \
    "\x01\xd4\x74\x02\x7b\xf6\xec\x39\x9b\x4c\x26\x93" \
    "\x9d\x9d\x9d\xcc\xce\xce\x15\x94\xb4\x48\xa7\x73" \
    "\x24\x12\x69\x66\x66\x92\x5c\xb8\x30\x4b\x2c\x36" \
    "\xb5\xa0\xbc\x65\x65\x19\x1e\x3e\x05\xba\xf7\x39" \
    "\x5f\xcb\xfe\x35\x03\xd8\xb1\x63\xc7\x17\x53\xa9" \
    "\x54\x64\xd7\xae\xdd\x84\xc3\x61\x1c\xc7\x25\x9b" \
    "\xb5\x49\xa5\xb2\xcc\xcd\xcd\x03\x48\x10\x8f\x27" \
    "\x10\x85\x5b\xac\xd6\xd6\xd5\xdc\x79\xe7\xbd\x00" \
    "\xcd\x86\x61\x6c\x62\x99\xdd\xe7\x25\xa4\x94\x2a" \
    "\xca\x15\x90\xb9\x75\xeb\xd6\xdf\xaf\x5b\xb7\x4e" \
    "\x35\x36\x36\x2a\xc3\x30\x96\xc3\xaf\x02\x5f\x05" \
    "\xae\xa4\x02\x43\x16\xd3\xb1\xd6\x2c\x64\xa0\x83" \
    "\xf1\x2a\xa0\x75\xe3\xc6\x8d\x3f\xdf\xbd\x7b\xf7" \
    "\xf7\x23\x91\x08\xa3\xa3\xa3\x0c\x0c\x0c\xd0\xdf" \
    "\xdf\xcf\xe0\xe0\x20\x42\x08\x94\x52\x3f\x05\x3e" \
    "\x42\x5f\x15\xba\xe8\xf9\x77\x12\xed\x4e\xff\x97" \
    "\x34\x0a\xda\x7a\x8d\x40\x03\xd0\x60\x18\xc6\xcf" \
    "\xb6\x6f\xdf\xbe\xd3\x34\xcd\xab\x2c\xcb\x62\x64" \
    "\x64\x84\x4c\x26\xd3\xab\x94\xda\x0b\xf4\x01\x17" \
    "\xd0\x93\x97\x87\x1e\x60\x2a\xaa\xc2\xc5\xf4\xfc" \
    "\x2f\x7b\xb6\xa4\x84\x50\x78\x98\x08\x00\x00\x00" \
    "\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

class AddTemplateDialogDesign(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        if not name:
            self.setName("AddTemplateDialogDesign")

        self.setSizeGripEnabled(1)

        AddTemplateDialogDesignLayout = QGridLayout(self,1,1,11,6,"AddTemplateDialogDesignLayout")

        self.pixmapLabel1 = QLabel(self,"pixmapLabel1")
        self.pixmapLabel1.setSizePolicy(QSizePolicy(0,0,0,0,self.pixmapLabel1.sizePolicy().hasHeightForWidth()))
        self.pixmapLabel1.setPixmap(self.image0)
        self.pixmapLabel1.setScaledContents(0)

        AddTemplateDialogDesignLayout.addWidget(self.pixmapLabel1,0,0)

        self.textLabel3 = QLabel(self,"textLabel3")
        self.textLabel3.setScaledContents(0)
        self.textLabel3.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.textLabel3,0,0,1,3)

        Layout1 = QHBoxLayout(None,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.okButton = QPushButton(self,"okButton")
        self.okButton.setEnabled(0)
        self.okButton.setAutoDefault(1)
        self.okButton.setDefault(1)
        Layout1.addWidget(self.okButton)

        self.cancelButton = QPushButton(self,"cancelButton")
        self.cancelButton.setAutoDefault(1)
        Layout1.addWidget(self.cancelButton)

        AddTemplateDialogDesignLayout.addMultiCellLayout(Layout1,8,8,0,3)

        self.line1 = QFrame(self,"line1")
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setFrameShape(QFrame.HLine)

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.line1,7,7,0,3)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setSizePolicy(QSizePolicy(0,5,0,0,self.textLabel1.sizePolicy().hasHeightForWidth()))

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.textLabel1,2,2,0,2)

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setSizePolicy(QSizePolicy(0,5,0,0,self.textLabel2.sizePolicy().hasHeightForWidth()))

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.textLabel2,3,3,0,1)

        self.nameEdit = QLineEdit(self,"nameEdit")

        AddTemplateDialogDesignLayout.addWidget(self.nameEdit,2,3)

        self.textLabel4 = QLabel(self,"textLabel4")

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.textLabel4,4,4,0,2)

        self.serverBox = QComboBox(0,self,"serverBox")

        AddTemplateDialogDesignLayout.addWidget(self.serverBox,3,3)

        self.line2 = QFrame(self,"line2")
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.setFrameShape(QFrame.HLine)

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.line2,1,1,0,3)

        self.descriptionEdit = QLineEdit(self,"descriptionEdit")

        AddTemplateDialogDesignLayout.addWidget(self.descriptionEdit,4,3)

        self.statusLabel = QLabel(self,"statusLabel")

        AddTemplateDialogDesignLayout.addMultiCellWidget(self.statusLabel,6,6,0,3)
        spacer10 = QSpacerItem(21,30,QSizePolicy.Minimum,QSizePolicy.Expanding)
        AddTemplateDialogDesignLayout.addItem(spacer10,5,2)

        self.languageChange()

        self.resize(QSize(461,292).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.okButton,SIGNAL("clicked()"),self,SLOT("accept()"))
        self.connect(self.cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.connect(self.nameEdit,SIGNAL("textChanged(const QString&)"),self.valuesChanged)
        self.connect(self.serverBox,SIGNAL("textChanged(const QString&)"),self.valuesChanged)

        self.setTabOrder(self.nameEdit,self.serverBox)
        self.setTabOrder(self.serverBox,self.descriptionEdit)
        self.setTabOrder(self.descriptionEdit,self.okButton)
        self.setTabOrder(self.okButton,self.cancelButton)


    def languageChange(self):
        self.setCaption(self.__tr("New Template"))
        self.textLabel3.setText(self.__tr("Please choose a template name, a description and a server with which the template is associated."))
        self.okButton.setText(self.__tr("&OK"))
        self.okButton.setAccel(QString.null)
        self.cancelButton.setText(self.__tr("&Cancel"))
        self.cancelButton.setAccel(QString.null)
        self.textLabel1.setText(self.__tr("Template name:"))
        self.textLabel2.setText(self.__tr("Server:"))
        self.textLabel4.setText(self.__tr("Description:"))
        self.statusLabel.setText(self.__tr("Please supply a template name."))


    def valuesChanged(self):
        print "AddTemplateDialogDesign.valuesChanged(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("AddTemplateDialogDesign",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = AddTemplateDialogDesign()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
