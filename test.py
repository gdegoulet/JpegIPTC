#!/usr/bin/env python3
import datetime
from JpegIPTC import JpegIPTC

if __name__ == '__main__':  # pragma: no cover
    # fetch iptc data from jpeg => iptc data present
    # create a new jpeg file and add previous iptc data
    print("")
    print("TEST 1")
    source = "76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg"
    destination = "P1000056.jpg"
    outputfile = "test.jpg"

    with open(source, "rb") as file:
        buffer = file.read()
    with open(destination, "rb") as file:
        results = file.read()

    iptc_start = datetime.datetime.now()
    jpegiptc_object = JpegIPTC()
    jpegiptc_object.load_from_binarydata(buffer)
    jpegiptc_object_d = JpegIPTC()
    jpegiptc_object_d.load_from_binarydata(results)

    #print("Copy IPTC data from "+source+" to "+destination)
    #print(jpegiptc_object.get_raw_iptc())
    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.get_raw_iptc())

    #print("Dumping raw data from new image")
    newresults = jpegiptc_object_d.dump()
    iptc_total_time = ( datetime.datetime.now() - iptc_start).total_seconds() * 1000
    print(iptc_total_time)

    if newresults is not None:
        results = newresults
    print("Dump OK : writing output to "+outputfile)
    with open(outputfile, "wb") as binary_file:
        binary_file.write(results)
        binary_file.close()

    del jpegiptc_object
    del jpegiptc_object_d

    # fetch iptc data from png file => no iptc data
    # create a new jpeg file and add previous iptc data
    print("")
    print("TEST 2")
    source="iptc-logo.png"
    destination = "P1000056.jpg"
    outputfile = "test2.jpg"

    with open(destination, "rb") as file:
        results = file.read()

    iptc_start = datetime.datetime.now()
    jpegiptc_object = JpegIPTC()
    jpegiptc_object.load_from_file(source)
    jpegiptc_object_d = JpegIPTC()
    jpegiptc_object_d.load_from_binarydata(results)
    #print(jpegiptc_object.get_raw_iptc())
    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.get_raw_iptc())
    newresults = jpegiptc_object_d.dump()
    iptc_total_time = ( datetime.datetime.now() - iptc_start).total_seconds() * 1000
    print(iptc_total_time)

    if newresults is not None:
        results = newresults
    print("Dump OK : writing output to "+outputfile)
    with open(outputfile, "wb") as binary_file:
        binary_file.write(results)
        binary_file.close()

    del jpegiptc_object
    del jpegiptc_object_d

    # fetch iptc data from jpeg => iptc data present
    # create a new png file and add previous iptc data
    # we don't support png file as output file
    # so jpegiptc_object_d.dump should return None
    # and you should not overwrite your initial result
    print("")
    print("TEST 3")
    source = "76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg"
    destination = "iptc-logo.png"
    outputfile = "test3.png"

    with open(source, "rb") as file:
        buffer = file.read()
    with open(destination, "rb") as file:
        results = file.read()

    iptc_start = datetime.datetime.now()
    jpegiptc_object = JpegIPTC()
    jpegiptc_object.load_from_binarydata(buffer)
    jpegiptc_object_d = JpegIPTC()
    jpegiptc_object_d.load_from_binarydata(results)

    #print("Copy IPTC data from "+source+" to "+destination)
    #print(jpegiptc_object.get_raw_iptc())
    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.get_raw_iptc())

    #print("Dumping raw data from new image")
    newresults = jpegiptc_object_d.dump()
    iptc_total_time = ( datetime.datetime.now() - iptc_start).total_seconds() * 1000
    print(iptc_total_time)

    if newresults is not None:
        results = newresults
    else:
        print("Warning: newresults is None")
    print("Dump OK : writing output to "+outputfile)
    with open(outputfile, "wb") as binary_file:
        binary_file.write(results)
        binary_file.close()

    del jpegiptc_object
    del jpegiptc_object_d


    # fetch iptc data from jpeg => iptc data present
    # create a new png file and add previous iptc data
    # we don't support png file as output file
    # test save_as method
    print("")
    print("TEST 4")
    source = "76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg"
    destination = "iptc-logo.png"
    outputfile = "test4.png"

    with open(source, "rb") as file:
        buffer = file.read()
    with open(destination, "rb") as file:
        results = file.read()

    iptc_start = datetime.datetime.now()
    jpegiptc_object = JpegIPTC()
    jpegiptc_object.load_from_binarydata(buffer)
    jpegiptc_object_d = JpegIPTC()
    jpegiptc_object_d.load_from_binarydata(results)

    #print("Copy IPTC data from "+source+" to "+destination)
    #print(jpegiptc_object.get_raw_iptc())
    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.get_raw_iptc())

    #print("Dumping raw data from new image")
    print("Dump OK : writing output to "+outputfile)
    newresults = jpegiptc_object_d.save_as(outputfile)
    iptc_total_time = ( datetime.datetime.now() - iptc_start).total_seconds() * 1000
    print(iptc_total_time)

    del jpegiptc_object
    del jpegiptc_object_d
