import socket
import pyautogui
# Set up the socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8003))

# Receive keystroke data and process it
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    # Process the received keystroke data
    print(f"Received keystroke: {data}")
    if data == '8':
       pyautogui.moveTo(100,100)
# Clean up
client_socket.close()

