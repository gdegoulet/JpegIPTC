#!/usr/bin/env python3
import datetime
from JpegIPTC import JpegIPTC

if __name__ == '__main__':  # pragma: no cover
    iptc_main = datetime.datetime.now()
    source = "76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg"
    destination = "P1000056.jpg"
    outputfile = "test.jpg"

    with open(source, "rb") as file:
        buffer = file.read()
    with open(destination, "rb") as file:
        results = file.read()

    iptc_start = datetime.datetime.now()
    jpegiptc_object = JpegIPTC(buffer)
    jpegiptc_object_d = JpegIPTC(results)

    #print("Copy IPTC data from "+source+" to "+destination)
    jpegiptc_object_d.set_raw_iptc(jpegiptc_object.raw_iptc)

    #print("Dumping raw data from new image")
    newresults = jpegiptc_object_d.dump()
    iptc_total_time = ( datetime.datetime.now() - iptc_start).total_seconds() * 1000
    print(iptc_total_time)

    if newresults is not None:
        print("Dump OK : writing output to "+outputfile)
        with open(outputfile, "wb") as binary_file:
            binary_file.write(newresults)

    iptc_total_time = ( datetime.datetime.now() - iptc_main).total_seconds() * 1000
    print(iptc_total_time)
