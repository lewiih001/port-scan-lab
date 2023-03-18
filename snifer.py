from scapy.all import *
# Ask user for input
user_input = input("Enter filter expression: ")

# Define filter expression and sniff packets
results=sniff(filter=user_input, prn=lambda x: x.summary())
wrpcap('sniffer.pcap',results)