import socket, pickle
import user as u


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432

if __name__ == '__main__':

    email = input('Enter your email to be notified: ')
    prod_link = input("Enter the product's link you wish to track: ")
    new_user = u.User(email, prod_link)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        status = s.recv(1024)
        print('\n[Status] ',status.decode())

        data_string = pickle.dumps(new_user)
        s.send(data_string)

        status = s.recv(1024)

        print('[Status] {}'.format(status.decode()))


