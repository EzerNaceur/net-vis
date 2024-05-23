import dpkt
import socket
import pygeoip

import requests

gi = pygeoip.GeoIP('GeoLiteCity-data/GeoLiteCity.dat')

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']
    return ip_address

def createKML(dstip):
    dst = gi.record_by_name(dstip)
    srcip = get_public_ip()
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
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
            )%(dstip, dstLong, dstLat, srcLong, srcLat)
        return kml
    except:
        print("Error while creating kml")
            


def plotIPs(pcap):
    kmlpts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dest = socket.inet_ntoa(ip.dst)
            KML = createKML(dest, src)
            kmlpts = kmlpts + KML
        except:
            print("There has been an error!/n")
    return kmlpts

def main():
    file = open('tcpdump.pcap', 'rb')
    pcap = dpkt.pcap.Reader(file)
    kmlhead = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
              '<Style id="customStyle">' \
              '<width>1<width>' \
              '<color>1B85B</color>' \
              '</LineStyle>' \
              '</Style>'
    kmlfoot = '</Document>\n</kml>\n'
    kmldoc = kmlhead + plotIPs(pcap)+kmlfoot
    print(kmldoc)
    
if __name__ == '__main__':
    main()
