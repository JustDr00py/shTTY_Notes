import os
from cryptography.fernet import Fernet
import os
from time import sleep

path = "./notes"
dir_list = os.listdir(path)
# prints all files

nn = ['1','new', 'New', 'New Note', 'new note', 'n', 'nn']
on = ['2','open', 'Open', 'Open Note', 'open note', 'o', 'r']
gk = ['3', 'key', 'gk', 'get key', 'get']

class Note:
    def __init__(self, title, msg):
        self.title = title
        self.msg = msg

    def write():
        m1 = input('Title: ')
        m2 = input('Note: ')
        print(m2)
        note = Note(m1,m2)
        print(f'{note.title} \n {note.msg}')
        f = open(f'./notes/{note.title}.txt', 'xt')
        f.write(f'{note.msg}')
        f.close()
        return print(f'{note.title} {note.msg}') 

    def read():
        dir_list = os.listdir(path)
        answer = input('Select a File: ')
        if f'{answer}.txt' in dir_list:
            f = open(f'./notes/{answer}.txt', "r")
            print(f'Title: {answer}')
            m = f.read()
            print(m)
        return answer

    def delete(x):
        if os.path.exists(f'./notes/{x}.txt'):
            os.remove(f'./notes/{x}.txt')
        else:
            print("The file does not exist") 
            

    def encrypt(x):
        # opening the key
        with open('mykey.key', 'rb') as filekey:
            key = filekey.read()
        
        # using the generated key
        fernet = Fernet(key)
        
        # opening the original file to encrypt
        with open(f'./notes/{x}.txt', 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and
        # writing the encrypted data
        with open(f'./notes/{x}.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt(x):
        # opening the key
        with open('mykey.key', 'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)
 
        # opening the encrypted file
        with open(f'./notes/{x}.txt', 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        # opening the file in write mode and
        # writing the decrypted data
        with open(f'./notes/{x}.txt', 'wb') as dec_file:
            dec_file.write(decrypted)

    def get_key():
        if os.path.exists('mykey.key'):
            answer = input(f'mykey.key already exists! \n Would you like to change it? (y/n): ')
            if answer == 'n':
                Note.doRun()
            elif answer == 'y':
                confirm = input('Are you sure!? (y/n)')
                if confirm == 'n':
                    print('Aborted!')
                    sleep(2)
                    Note.doRun()
                elif confirm == 'y':
                    key = Fernet.generate_key() #this is your "password"
                    with open('mykey.key', 'wb') as mykey:
                        mykey.write(key)

    def menu():
        print(' ________________')
        print('|  shTTY NOTES   |')
        print('|----------------|')
        print('| 1) new note    |')
        print('| 2) open note   |')
        print('| 3) get key     |')
        print('|________________|') 
        print("\n Files:")
        dir_list = os.listdir(path)
        print(dir_list)
        global q
        q = input('What would you like to do?: ')
        
    def doRun():
        Note.menu()
        Note.selection(q)

    def selection(x):
        if x in nn:
            Note.write()
            print('-New Note-')
        elif x in on:
            print('-Open Note-')
            t = Note.read()
            back = input('hit ENTER to go back | d to Delete | e to Encrypt: | y to decrypt:')
            if back == '':
                pass
            if back == 'd':
                Note.delete(t)
            if back == 'e':
                Note.encrypt(t)
            if back == 'y':
                Note.decrypt(t)
        elif x in gk:
            print('-Get Key-')
            sleep(.5)
            Note.get_key()    
        else:
            print('Sorry, an option!')
            sleep(1)
            Note.doRun()
