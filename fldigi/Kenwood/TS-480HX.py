

import serial

ser = serial.Serial('COM5',9600)  # open serial port
print(ser.name)         # check which port was really used
msg=""
while 1:
  value = ser.read()
  if value.decode()==";":
        
        if msg=="IF":
            msg="IF00007074000000000000000000000000000;"
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif msg=="RX":
            msg="RX0;"
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif msg=="MD":
            msg="MD1;"  #LSB
            #msg="MD2"   #USB
            #msg="MD3"   #CW
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif "FA" in msg and len(msg)==13:
            msg="FA00007074000;"  #LSB
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="FA":
            msg="FA00007074000;"  #LSB
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="FA":
            msg="FA00007074000;"  #LSB
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="PC":
            msg="PC005;"  #5W
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif  msg=="SM0":
            msg="SM00005;"  #S-metr
            print(msg)
            ser.write(bytes(msg, 'utf-8'))
            msg=""
        elif 64<len(msg):
            msg=""
        else:
            print(msg)
            print(len(msg))
        
                        
  else:
    msg+=value.decode()
        
    
ser.close()             # close por