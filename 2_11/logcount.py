import sys


if len(sys.argv) < 2:
    print("Usage: python3 logcount.py <logfile>")  
    sys.exit(1)
file = sys.argv[1]

try:
    with open(file) as log_file:
        data = log_file.read()
        logs = data.strip().split("\n")
        
        ip_list = []
        ip_dict = {}

        for line in logs:
            parts  = line.split()
            if not parts:
                continue
            ip_list.append(parts[0])
             
        for item in ip_list:
            if item in ip_dict:
                ip_dict[item] += 1
            else:
                ip_dict[item] = 1     
       
        ranked = sorted(ip_dict.items(), reverse=True, key=lambda item: item[1])
        for key, value in ranked:
            print(f"{value:6} {key}")
        if ranked:
            print(f"\nTop = {ranked[0][0]}")

except FileNotFoundError:
    print(f"Error: file not found: {file}")
    sys.exit(1)
