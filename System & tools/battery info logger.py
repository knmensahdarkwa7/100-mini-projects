import batteryinfo
from customtkinter import *

# Get battery data
battery = batteryinfo.Battery()
battery_info = battery.as_dict()

print(battery_info)  # For debugging in console

# Create main window
root = CTk()
root.geometry('420x420')
root.title("Battery Health Logger")

# Title label
label = CTkLabel(root, text='Battery Info', font=('Segoe UI', 25, 'bold'))
label.pack(side='top', anchor='w', pady=10)

# Section header
label2 = CTkLabel(root, text='Information', font=('Calibri', 18, 'italic'))
label2.pack(side='top', anchor='w')

# Battery percentage
label3 = CTkLabel(root,
                  text=f'Battery percent: {battery.percent}%',
                  font=('Consolas', 12))
label3.pack(side='top', anchor='w')

# Charging status
label4 = CTkLabel(root,
                  text=f'Charging: {"Yes" if battery.state else "No"}',
                  font=('Consolas', 12))
label4.pack(side='top', anchor='w')

# Time left (if available)
time_left = battery.time_to_full
if isinstance(time_left, int) and time_left > 0:
    hours = time_left // 3600
    minutes = (time_left % 3600) // 60
    time_str = f"{hours}h {minutes}m"
else:
    time_str = "Calculating..."

label5 = CTkLabel(root,
                  text=f'Time left: {time_str}',
                  font=('Consolas', 12))
label5.pack(side='top', anchor='w')

# Voltage (if provided in battery_info)
if 'voltage' in battery_info:
    label6 = CTkLabel(root,
                      text=f'Voltage: {battery_info["voltage"]} V',
                      font=('Consolas', 12))
    label6.pack(side='top', anchor='w')

# Temperature (if provided)
if 'temperature' in battery_info:
    label7 = CTkLabel(root,
                      text=f'Temperature: {battery_info["temperature"]} °C',
                      font=('Consolas', 12))
    label7.pack(side='top', anchor='w')

# Health (if provided)
if 'health' in battery_info:
    label8 = CTkLabel(root,
                      text=f'Health: {battery_info["health"]}%',
                      font=('Consolas', 12))
    label8.pack(side='top', anchor='w')

# Run the app
root.mainloop()