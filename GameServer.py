import asyncore, socket, Main

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
                
    def handle_accept(self):
        conn, addr = self.accept() #@UnusedVariable
        Main.MainClass(conn)
        
    def handle_close(self):
        self.close()
        
# class ServerHandler(asyncore.dispatcher):
#     messages = []
#     SIZE = 1024
#     
#     def __init__(self, socket):
#         asyncore.dispatcher.__init__(self, socket)
#         self.size = 0
#         self.data = ""
#         
#     def writable(self):
#         return self.size < len(ServerHandler.messages)
#         
#     def handle_read(self):
#         data = self.recv(ServerHandler.SIZE)
#         ServerHandler.messages.append(data)
#         
#     def handle_write(self):
#         if not self.data:
#             self.data = ServerHandler.messages[self.size]
#             sent = self.send(self.data)
#         else:
#             sent = self.send(self.data)
#         self.data = self.data[sent:]
#         if not self.data:
#             self.size += 1
#         
#     def handle_close(self):
#         self.close()
        

Server("localhost", 8000)
asyncore.loop()