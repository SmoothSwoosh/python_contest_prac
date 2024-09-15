import cmd
import threading
import time
import readline
import sys
import socket
import shlex


class simple(cmd.Cmd):
    my_socket = None
    buffer = ""

    def __init__(self):
        super().__init__()
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect(("localhost", 8080))


    def send_msg(self, msg):
        self.my_socket.send(msg.encode())
        self.recieve = True


    def do_cows(self, arg):
        if arg != "":
            print("Something wrong with parameters")
            return
        self.my_socket.send("cows\n".encode())


    def do_who(self, arg):
        if arg != "":
            print("Something wrong with parameters")
            return
        self.my_socket.send("who\n".encode())


    def do_login(self, arg):
        match shlex.split(arg):
            case [cowname]:
                self.my_socket.send(f"login {cowname}\n".encode())
            case _:
                print("Something wrong with parameters")


    def complete_login(self, prefix, line, begidx, endidx):
        global pause
        self.my_socket.send(f"GET_COWS\n".encode())

        while True:
            time.sleep(0.1)
            if self.buffer == "":
                continue
            variants = eval(self.buffer)
            break
        self.buffer = ""
        return [cow for cow in variants if cow.startswith(prefix)]


    def do_say(self, arg):
        match shlex.split(arg):
            case [cowname, msg]:
                self.my_socket.send(f"say {cowname} '{msg}'\n".encode())
            case _:
                print("Something wrong with parameters")
    

    def complete_say(self, prefix, line, begidx, endidx):
        global pause
        self.my_socket.send(f"GET_COWS_USED\n".encode())
        
        while True:
            time.sleep(0.1)
            if self.buffer == "":
                continue
            variants = eval(self.buffer)
            break
        self.buffer = ""
        return [cow for cow in variants if cow.startswith(prefix)]


    def do_yield(self, arg):
        match shlex.split(arg):
            case [msg]:
                self.my_socket.send(f"yield '{msg}'\n".encode())
            case _:
                print("Something wrong with parameters")


    def do_quit(self, arg):
        if arg != "":
            print("Something wrong with parameters")
            return 
        self.my_socket.send("quit\n".encode())
        return True


    def output(self):
        while True:
            text = self.my_socket.recv(1024).decode().strip()
            if text == "":
                break

            if text[0] == "[":
                self.buffer = text
            else:
                print(f"\n{text}\n{self.prompt}{readline.get_line_buffer()}", end="", flush=True)


cmdline = simple()
output = threading.Thread(target=cmdline.output, args=())
output.start()
cmdline.cmdloop()
