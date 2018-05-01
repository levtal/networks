import socket
import sys
currentVersion = sys.version_info
print (currentVersion)
pyVer = currentVersion[0]
""" 
http://www.lamed-oti.com/school/rs/networks/code_samples/
    name / NAME - get the server's name.
    time / TIME - get the server's time as hh:mm:ss,
    rand / RAND - get a random integer between 1 and 10.
    exit / EXIT - Ask the server to terminate its service.
"""

SERVER = '127.0.0.1'
PORT = 1729
FIRST_MESSAGE_LENGTH = 48
MESSAGE_SIZE = 4


def initial_contact(ip, port):
    """ Sends the first hand-shake to the server and ask for the
        services it provides.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Check if the server is up and running , first.
    try:
        client_socket.connect((ip, port))
    except:
        print ('Server is not up , yet')
        return False, '', ''
    message = "Helloa"
    if pyVer >=3:
        client_socket.send(message.encode())
    else:
       client_socket.send(message)

    result = client_socket.recv(FIRST_MESSAGE_LENGTH)
    print("First answer from sever ",result)
    return True, result, client_socket


def send_requests(res, client_socket):
    """ Reads a message from the user,sends it to the server and prints it
        on the screen.
    """
    result = res
    while len(result) > 0:
        if pyVer >= 3:
            message = input('Command: ')
            message = message[:MESSAGE_SIZE].upper() # Ignore msg more than 4 char

            client_socket.send(message.encode())
        else:
            message = raw_input('Command: ')
            message = message[:MESSAGE_SIZE].upper()
            client_socket.send(message)

        # First four bytes contain the message we receive, has the length
        print('This is the mistake' )
        result = client_socket.recv(MESSAGE_SIZE)


        if result:
            message_length = int(result)
            result = client_socket.recv(message_length)
            print("2'st answer from sever ",result)
        else:
            result = ''
    client_socket.close()


def main():
    ## Ask server for the type of services it and loop on requests.
    server_on, result, socket = initial_contact(SERVER, PORT)
    if server_on:
      send_requests(result, socket)

if __name__ == '__main__':
    main()