from scapy.all import sniff

def packet_callback(packet):
    print("\n--- Packet Captured ---")

    if packet.haslayer("IP"):
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)

    if packet.haslayer("TCP"):
        print("Protocol: TCP")
    elif packet.haslayer("UDP"):
        print("Protocol: UDP")

    if packet.haslayer("Raw"):
        print("Payload:", packet["Raw"].load)

def main():
    print("Starting Packet Sniffer... Press CTRL+C to stop.")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
