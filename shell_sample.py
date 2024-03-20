#!/usr/bin/python3
import cmd

'''Writing a code that passed the python code check'''

'''Creating a class'''


class Shell_sample(cmd.Cmd):

    '''next is to create a subclass of the cmd'''
    def do_hello(self, arg):
        '''say hello'''
        print('Hello, World')

    '''exit option subclass'''
    def do_exit(self, arg):

        '''To exit'''
        return True


'''calling the function'''
if __name__ == '__main__':
    display = Shell_sample()
    '''looping the command line'''
    display.cmdloop('Input Hello!')
