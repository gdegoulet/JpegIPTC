# JpegIPTC

## About:
This program is related with https://github.com/gdegoulet/thumbor-piliptc-engine

The purpose is to extract APP13 (iptc data) from image and raw copy APP13 to another image

**Original image with IPTC tags --> thumbor transformation --> new image with original IPTC tags**

## IPTC tags :
JPEG IPTC (International Press Telecommunications Council) tags are a set of metadata that can be embedded into JPEG image files to provide information about the image content, including ownership and copyright information. These tags can be used by photographers, artists, and publishers to identify their work and protect their intellectual property rights. By including IPTC tags in their JPEG images, creators can ensure that their ownership and copyright information is attached to their work and remains with it as it is shared and distributed across the internet. This can be particularly important for photographers and other creators who rely on their work to generate income, as it can help deter unauthorized use and ensure that they are properly credited for their work. In this way, JPEG IPTC tags can play an essential role in protecting the intellectual property of creators and maintaining the integrity of their work.


In Europe, image copyright is protected by various laws and regulations, such as the Berne Convention for the Protection of Literary and Artistic Works and the Directive on the harmonization of certain aspects of copyright and related rights in the information society. These laws provide creators with exclusive rights over their works, including photographs and images, and require that any use of these works by others be authorized or licensed by the creator.


The use of JPEG IPTC tags can be particularly helpful in enforcing these copyright laws. **In fact, some countries in Europe, such as France and Germany, have enacted specific laws that require the use of IPTC tags on certain types of images, such as those used in advertising and editorial content.** These laws require that the copyright owner's name and contact information be included in the IPTC tags, making it easier for potential infringers to identify and contact the owner for permission to use the image.


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

###
```
pip install JpegIPTC
```

## Functions:

- load_from_file(filename) : initialize object from file location (return booleans)
- load_from_binarydata(rawdata) : initialize object from binary string (return booleans) **(for thumbor integration)**
- save() : for object initialized with load_from_file : overwrite with new content (return booleans)
- save_as(output_filename) : write/overwrite new content to output_filename (return booleans)
- get_raw_iptc() : return raw iptc as binary string **(for thumbor integration)**
- set_raw_iptc(rawdata) : write new iptc binary string as raw_iptc properties of current object **(for thumbor integration)**
- dump() : like save but only return image as binary string **(for thumbor integration)**
- is_jpeg() : return booleans


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

    jpegiptc_object = JpegIPTC()
    jpegiptc_object.load_from_binarydata(buffer)
    jpegiptc_object_d = JpegIPTC()
    jpegiptc_object_d.load_from_binarydata(results)

    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.get_raw_iptc())
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

```

As you can see, IPTC Envelope has vanished .. :( for now ..

**since 0.3 : ALL IPTC data (record 1 and 2 from APP13) are raw copied**

**since 1.0 : Searching for IPTC data only if input is regular jpeg file**

**since 1.4 : available on Pypip"
