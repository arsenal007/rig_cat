

import serial

ser = serial.Serial('COM5',9600)  # open serial port
print(ser.name)         # check which port was really used
msg=""
while 1:
  value = ser.read()
  if value.decode()==";":
        
        if msg=="IF":
            print("query: " + msg +";")
            msg="IF00007074000000000000000000000000000;"
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif msg=="RX":
            print("query: " + msg +";")
            msg="RX0;"
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif msg=="MD":
            print("query: " + msg +";")
            msg="MD1;"  #LSB
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif msg=="MD1":
            print("query: " + msg +";")
            msg="MD1;"  #LSB
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif msg=="MD2":
            print("query: " + msg +";")
            msg="MD1;"  #LSB
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif "FA" in msg and len(msg)==13:
            print("query: " + msg +";")
            msg="FA00007074000;"  #LSB
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="FA":
            print("query: " + msg +";")
            msg="FA00007074000;"  #LSB
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="FA":
            print("query: " + msg +";")
            msg="FA00007074000;"  #LSB
            print("ans: " +msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="PC":
            msg="PC005;"  #5W
            print("ans: " + msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif 64<len(msg):
            msg=""
        else:
            print("unknown query: " +msg+" len: " + str(len(msg)))
            
        
                        
  else:
    msg+=value.decode()
        
    
ser.close()             # close por