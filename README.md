# JpegIPTC

## About:
This program is related with https://github.com/gdegoulet/thumbor-piliptc-engine

The purpose is to extract APP13 (iptc data) from image and raw copy APP13 to another image

**Original image with IPTC tags --> thumbor transformation --> new image with original IPTC tags**

## Credit:
```
# Ported from James Campbell iptcinfo3 https://github.com/james-see/iptcinfo3 
# Ported from Josh Carter's Perl IPTCInfo.pm by Tamás Gulácsi
#
# IPTCInfo: extractor for IPTC metadata embedded in images
# Copyright (C) 2000-2004 Josh Carter <josh@multipart-mixed.com>
# Copyright (C) 2004-2008 Tamás Gulácsi <gthomas@gthomas.hu>
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the same terms as Python itself.

```

## Example:
See test.py : we fetch iptc tags from file 76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg and we add it to P1000056.jpg

```python
    source = "76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg"
    destination = "P1000056.jpg"
    outputfile = "test.jpg"

    with open(source, "rb") as file:
      buffer = file.read()
    with open(destination, "rb") as file:
      results = file.read()

    jpegiptc_object = JpegIPTC(buffer)
    jpegiptc_object_d = JpegIPTC(results)
    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.raw_iptc)
    newresults = jpegiptc_object_d.dump()
    
    with open(outputfile, "wb") as binary_file:
      binary_file.write(newresults)
```

```
iptc 76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg
76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg:
 Tag      Name                 Type      Size  Value
 -------- -------------------- --------- ----  -----
 1:000    Model Version        Short        2  2
 1:020    File Format          Short        2  1
 1:022    File Version         Short        2  2
 1:030    Service Identifier   String       9  AFP-PHOTO
 1:040    Envelope Number      NumString    8  12345678
 1:060    Envelope Priority    NumString    1  5
 1:070    Date Sent            Date         8  20221120
 1:080    Time Sent            Time        11  210118+0000
 1:090    Coded Character Set  Binary       3  1b 2d 41
 1:100    Unique Name of Objec String      11  AFP_32PC4R2
 2:000    Record Version       Short        2  2
 2:005    Object Name          String      27  UKRAINE-RUSSIA-WAR-CONFLICT
 2:010    Urgency              NumString    1  5
 2:012:00 Subject Reference    String      45  IPTC:16009000:unrest, conflicts and  war:war:
 2:012:01 Subject Reference    String      41  IPTC:16000000:unrest, conflicts and  war:
 2:015    Category             String       3  WAR
 2:020    Supplemental Categor String       3  war
 2:025:00 Keywords             String       3  war
 2:025:01 Keywords             String      10  Horizontal
 2:055    Date Created         Date         8  20221120
 2:060    Time Created         Time        11  152935+0300
 2:062    Digital Creation Dat Date         8  20221120
 2:063    Digital Creation Tim Time        11  152935+0300
 2:065    Originating Program  String      22  g2mapping/libg2 3.9.39
 2:070    Program Version      String       6  3.9.15
 2:080    By-line              String      12  BULENT KILIC
 2:085    By-line Title        String       3  STF
 2:090    City                 String      12  Chornobaivka
 2:100    Country Code         String       3  UKR
 2:101    Country Name         String       7  Ukraine
 2:110    Credit               String       3  AFP
 2:115    Source               String       3  AFP
 2:116    Copyright Notice     String      16  AFP or licensors
 2:120    Caption/Abstract     String     242  A Ukrainian soldier walks in front of a destroyed building of the International Airport of Kherson in the village of Chornobaivka, outskirts of Kherson, on November 20, 2022, amid the Russian invasion of Ukraine. (Photo by BULENT KILIC / AFP)
 2:135    Language Identifier  String       2  EN


iptc test.jpg 
test.jpg:
 Tag      Name                 Type      Size  Value
 -------- -------------------- --------- ----  -----
 2:000    Record Version       Short        2  2
 2:005    Object Name          String      27  UKRAINE-RUSSIA-WAR-CONFLICT
 2:010    Urgency              NumString    1  5
 2:012:00 Subject Reference    String      45  IPTC:16009000:unrest, conflicts and  war:war:
 2:012:01 Subject Reference    String      41  IPTC:16000000:unrest, conflicts and  war:
 2:015    Category             String       3  WAR
 2:020    Supplemental Categor String       3  war
 2:025:00 Keywords             String       3  war
 2:025:01 Keywords             String      10  Horizontal
 2:055    Date Created         Date         8  20221120
 2:060    Time Created         Time        11  152935+0300
 2:062    Digital Creation Dat Date         8  20221120
 2:063    Digital Creation Tim Time        11  152935+0300
 2:065    Originating Program  String      22  g2mapping/libg2 3.9.39
 2:070    Program Version      String       6  3.9.15
 2:080    By-line              String      12  BULENT KILIC
 2:085    By-line Title        String       3  STF
 2:090    City                 String      12  Chornobaivka
 2:100    Country Code         String       3  UKR
 2:101    Country Name         String       7  Ukraine
 2:110    Credit               String       3  AFP
 2:115    Source               String       3  AFP
 2:116    Copyright Notice     String      16  AFP or licensors
 2:120    Caption/Abstract     String     242  A Ukrainian soldier walks in front of a destroyed building of the International Airport of Kherson in the village of Chornobaivka, outskirts of Kherson, on November 20, 2022, amid the Russian invasion of Ukraine. (Photo by BULENT KILIC / AFP)
 2:135    Language Identifier  String       2  EN

```

As you can see, IPTC Envelope has vanished .. :( for now ..
