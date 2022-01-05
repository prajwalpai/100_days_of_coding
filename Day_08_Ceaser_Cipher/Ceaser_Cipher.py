import os

ceaser = '''

  ,ad8888ba,                                                                 
 d8"'    `"8b                                                                
d8'                                                                          
88              ,adPPYba,  ,adPPYYba,  ,adPPYba,   ,adPPYba,  8b,dPPYba,     
88             a8P_____88  ""     `Y8  I8[    ""  a8P_____88  88P'   "Y8     
Y8,            8PP"""""""  ,adPPPPP88   `"Y8ba,   8PP"""""""  88             
 Y8a.    .a8P  "8b,   ,aa  88,    ,88  aa    ]8I  "8b,   ,aa  88             
  `"Y8888Y"'    `"Ybbd8"'  `"8bbdP"Y8  `"YbbdP"'   `"Ybbd8"'  88             



  ,ad8888ba,   88               88                                           
 d8"'    `"8b  ""               88                                           
d8'                             88                                           
88             88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,          
88             88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8          
Y8,            88  88       d8  88       88  8PP"""""""  88                  
 Y8a.    .a8P  88  88b,   ,a8"  88       88  "8b,   ,aa  88                  
  `"Y8888Y"'   88  88`YbbdP"'   88       88   `"Ybbd8"'  88                  
                   88                                                        
                   88     
'''
def encode(msg,swiftkey):
    encoded_msg_tmp=[]
    for letter in msg:
        if ( ord(letter)+swiftkey > 122):
            swiftkey = swiftkey - 26
        encoded_msg_tmp += chr(ord(letter)+swiftkey)
    encoded_msg=''.join([str(elem) for elem in encoded_msg_tmp])
    print(encoded_msg)
def decode(msg,swiftkey):
    decoded_msg_tmp = []
    for letter in msg:
        if  (  ord(letter) - swiftkey < 97):
            swiftkey = swiftkey - 26
        decoded_msg_tmp += chr(ord(letter) - swiftkey)
    decoded_msg = ''.join([str(elem) for elem in decoded_msg_tmp])
    print(decoded_msg)
os.system('clear')
print(ceaser)
choice=input("Type 'encode' to Encrypt and Type 'decode' to Decrypt : ")
msg=input("Type your message : ")
shiftkey=int(input("Type the Shift number : "))
if choice=="encode":
    encode(msg,shiftkey)
elif choice=="decode":
    decode(msg,shiftkey)
else:
    print("Invalid Choice")