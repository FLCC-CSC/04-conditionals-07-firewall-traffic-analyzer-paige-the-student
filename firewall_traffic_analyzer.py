def main():
    print("=== Network Traffic Security Analyzer ===")
    print()
    
    # Step 1: Prompt the user for port number and data transfer size
    port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
    transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))
    
    
    # Step 2: Categorize traffic using if-elif-else
    if port == 22 or port == 3389:
        risk_level = "HIGH RISK: Potential unauthorized remote access detected!"
    elif port == 80 and transfer_size > 100:
        risk_level = "MEDIUM RISK: Large unencrypted data transfer detected."
    elif port == 443:
        risk_level = "LOW RISK: Secure encrypted transfer detected."
    else:
        risk_level = "UNKNOWN: Unrecognized traffic pattern."
    
    # Step 3: Print a firewall log message
    print("\nFIREWALL LOG:")
    print(f"Port: {port}, Transfer Size: {transfer_size} MB")
    print(f"Risk Assessment: {risk_level}")
    print("------------------------")

if __name__ == "__main__":
    main()
