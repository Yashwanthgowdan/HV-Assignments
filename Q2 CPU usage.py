import psutil
# Setting CPU threshold
cpu_usage = 5
print("Monitoring CPU usage")
while True:
        # To measure CPU usage
        cpu = psutil.cpu_percent(interval=1)

        # Check if usage is above the threshold
        if cpu > cpu_usage:
            print("Alert! CPU usage exceeds threshold:", cpu ,"%")
