import hashlib
import sys

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

print(colors.BLUE+" _   _           _       ____                _     ")
print("| | | | __ _ ___| |__   / ___|_ __ __ _  ___| | __ ")
print("| |_| |/ _` / __| '_ \ | |   | '__/ _` |/ __| |/ / ")
print("|  _  | (_| \__ \ | | || |___| | | (_| | (__|   <  ")
print("|_| |_|\__,_|___/_| |_(_)____|_|  \__,_|\___|_|\_\ "+colors.STOP)
print


def md5 (choice, inp, passlist):
    m = hashlib.md5()
    if choice == 0:
        m.update(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
            password = line.strip('\n')
            m.update(password.encode("utf-8"))
            out=m.hexdigest()
            if out == inp:
                print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                print ("-"*30)
                c = 0
                menu()
            else: 
                c=c+1
                password = " "
        if c > 0:
            unable()
            menu()

def sha1 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha1(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha1(password.encode("utf-8"))
                out=m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else:
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha224 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha224(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                m = hashlib.sha224(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha256 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha256(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc (inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha256(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha384 (choice, inp, passlist):
    if choice == 0:
        m = hashlib.sha384(inp.encode("utf-8"))
        output = m.hexdigest()
        print_enc(inp, output)
        menu()
    if choice == 1:
        cracking()
        c=0
        passfile = open(passlist)
        for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha384(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()

def sha512 (choice, inp, passlist):
        if choice == 0:
            m = hashlib.sha512(inp.encode("utf-8"))
            output = m.hexdigest()
	    print_enc(inp, output)
            menu()
        if choice == 1:
            cracking()
            c=0
            passfile = open(passlist)
            for line in passfile.readlines():
                password = line.strip('\n')
                password += ""
                m = hashlib.sha512(password.encode("utf-8"))
                out = m.hexdigest()
                if out == inp:
                    print (colors.GREEN+"[+]" + inp + " : " + password+colors.STOP)
                    print ("-"*30)
                    c = 0
                    menu()
                else: 
                    c=c+1
        if c > 0:
            unable()
            menu()
            
def print_enc (inp, output):
    print
    print (colors.BOLD+"Hashing String..."+colors.STOP)
    print (colors.GREEN+inp + " : " + output+colors.STOP)
    print 

def cracking():
    print (colors.BOLD+"Cracking String...\n"+colors.STOP+"-"*30)

def unable():
    print (colors.RED+"Unable to Find Password...\n"+colors.STOP+"-"*30)

def menu():
    print
    print ("-"*70)
    print (colors.BOLD+"1.md5 \n2.sha1 \n3.sha224 \n4.sha256 \n5.sha384 \n6.sha512 \n99.exit \n"+colors.STOP)
    value = int(input(">>> "))
    if value == 99:
        print (colors.RED+"QUITTING!!"+colors.STOP)
        sys.exit()
    choice = int(input("(0) for Hashing And (1) for Cracking : "))
    inp = str(raw_input("String : "))
    
    if choice == 0:
        passlist = ''
    if choice == 1:
        passlist = raw_input("PASSWORD FILE>>>")
        
    if value == 1:
        md5(choice, inp, passlist)
    if value == 2:
        sha1(choice, inp, passlist)
    if value == 3:
        sha224(choice, inp, passlist)
    if value == 4:
        sha256(choice, inp, passlist)
    if value == 5:
        sha384(choice, inp, passlist)
    if value == 6:
        sha512(choice, inp, passlist)

menu()
