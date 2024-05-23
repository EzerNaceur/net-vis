import dpkt
import socket
import pygeoip

import sys

gi = pygeoip.GeoIP('GeoLiteCity-data/GeoLiteCity.dat')


def createKML(dstip):
    dst = gi.record_by_name(dstip)
    srcip = sys.argv[1]
    src = gi.record_by_name(srcip)
    try:
        dstLong = dst['longitude']
        dstLat = dst['latitude']
        srcLong = src['longitude']
        srcLat = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#customStyle</styleUrl>\n'
            '<LineString>\n'
            '<coordinates> %6f,%6f\n%6f,%6f </coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
            )%(dstip, dstLong, dstLat, srcLong, srcLat)
        return kml
    except:
        return ''
            

def pltips(pcap):
    kmlpts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dest = socket.inet_ntoa(ip.dst)
            KML = createKML(dest)
            kmlpts = kmlpts + KML
        except:
            pass
    return kmlpts


def main():
    file = open('tcpdump.pcap', 'rb')
    pcap = dpkt.pcap.Reader(file)
    kmlhead = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
              '<Style id="customStyle">\n' \
              '<LineStyle>\n' \
              '<width>1</width>\n' \
              '<color>7dff0000</color>\n' \
              '</LineStyle>\n' \
              '</Style>\n'
    kmlfoot = '</Document>\n</kml>\n'
    kmldoc = kmlhead + pltips(pcap) + kmlfoot
    with open('result.kml', 'w') as file:
        file.write(kmldoc)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('[x] Please specify an ip address: python net-vis.py ip_address\n')
    else:
        main()
