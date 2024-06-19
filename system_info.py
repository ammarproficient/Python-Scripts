import psutil
import time

while True:
    # CPU Utilization Monitoring
    cpu = psutil.cpu_percent()
    # Network Monitoring
    network = psutil.net_io_counters()
    # RAM Monitoring
    ram = psutil.virtual_memory()

    # CPU Output
    print(f"CPU Percentage Used: {cpu}%")
    # Network Output
    print(f"Bytes sent: {network.bytes_sent}")
    print(f"Bytes received: {network.bytes_recv}")
    print(f"Packets sent: {network.packets_sent}")
    print(f"Packets received: {network.packets_recv}")
    # RAM Output
    print(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {ram.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {ram.used / (1024 ** 3):.2f} GB")
    print(f"Percentage RAM Used: {ram.percent}%")

    # Add a separator for better readability between iterations
    print("-" * 30)

    # Wait for 1 second before the next iteration
    time.sleep(1)
