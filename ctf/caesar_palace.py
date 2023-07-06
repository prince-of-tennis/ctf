from pwn import *
#nc 20.85.231.234 1338


def caesar(txt, s):
    result = ""
    for i in range(len(txt)):  
        char = txt[i]  
        result += chr((ord(char) - int(s) - 96) % 26 + 97)  
    return result

d = open("dictionary.txt", "r").read()
conn = remote('20.85.231.234',1338)
conn.recvline()
conn.recvline()

while (1==1):
    c = str(conn.recvline())
    w = c.split(" ")[3][:-3]
    for i in range(0,11):
        word = caesar(w,i)
        if(word in d):
            print(word)
            conn.sendline(w.encode())
            break

conn.close()
