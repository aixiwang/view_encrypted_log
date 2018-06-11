# -*- coding: utf-8 -*-
#============================================
#
# Copyright(c) 2015 by Aixi Wang <aixi.wang@hotmail.com>
#---------------------------------------------------------
import pyaes
import binascii
import sys
import os

#-------------------
# readfile
#-------------------
def readfile(filename):
    f = open(filename,'rb')
    fs = f.read()
    f.close()

    return fs
    
#-------------------
# writefile
#-------------------
def writefile(filename,content):
    f = open(filename,'wb')
    fs = f.write(content)
    f.close()
    return
    
def myaes_encrypt(key,in_file,out_file):
    key2 = "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    key2 = key + key2[len(key):]
    mode = pyaes.AESModeOfOperationCTR(key2.encode('utf-8'))
    file_in = open(in_file,'rb')
    file_out = open(out_file, 'wb')
    pyaes.encrypt_stream(mode, file_in, file_out)
    file_in.close()
    file_out.close()

    
def myaes_decrypt(key,in_file,out_file):
    key2 = "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    key2 = key + key2[len(key):]
    mode = pyaes.AESModeOfOperationCTR(key2.encode('utf-8'))
    file_in = open(in_file,'rb')
    file_out = open(out_file, 'wb')
    pyaes.decrypt_stream(mode, file_in, file_out)
    file_in.close()
    file_out.close()
    
    
#------------------------------------------
#        M A I N    L O O P
#------------------------------------------ 
if __name__ == '__main__':
   
    print('usage: python3 view_encrypted_log.py aes_key hex_string')
    aes_key = sys.argv[1]
    hex_string = sys.argv[2]
    b = bytearray.fromhex(hex_string)
    writefile('output.txt',b)
    myaes_decrypt(aes_key,'output.txt','input2.txt')
    s = readfile('input2.txt').decode('utf-8')
    print(s)
    #os.system('cat input2.txt')
    