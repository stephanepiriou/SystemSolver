import fcntl
import time
import random
import struct
import sys
import termios
import string
import os
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format



class message(str):
    def __new__(cls, text, speed):
        self = super(message, cls).__new__(cls, text)
        self.speed = speed
        self.y = -1 * len(text)
        self.x = random.randint(0, display().width)
        self.skip = 0
        return self

    def move(self):
        if self.speed > self.skip:
            self.skip += 1
        else:
            self.skip = 0
            self.y += 1


class display(list):

    def __init__(self):
        #Gets width of console
        self.height, self.width = _get_terminal_size_linux()
        #self.height, self.width = struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, '1234'))
        self[:] = [' ' for i in range(self.width * self.height)]

    def set_vertical(self, x, y, string):
        string = string[::-1] #Flips every bit
        if x < 0:
            x = 80 + x
        if x >= self.width:
            x = self.width - 1
        if y < 0:
            string = string[abs(y):]
            y = 0
        if y + len(string) > self.height:
            string = string[0:self.height - y]
        if y >= self.height:
            return
        start = y * self.width + x
        length = self.width * (y + len(string))
        step = self.width #Steps to next "line"
        self[start:length:step] = string

    def __str__(self):
        return ''.join(self)


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])


def entermatrix():

    cprint(figlet_format('                    \n    E n t e r    \n                    ', font='dotmatrix', width=220, justify="center"), 'yellow', 'on_green', attrs=['bold'])
    time.sleep(5)
    os.system('clear')

    cprint(figlet_format('                    \n      T h e       \n                    ', font='dotmatrix', width=220, justify="center"), 'yellow', 'on_green', attrs=['bold'])
    time.sleep(5)
    os.system('clear')

    cprint(figlet_format('                    \n[  M a t r i x  ]\n                    ', font='dotmatrix', width=220, justify="center"), 'yellow', 'on_green', attrs=['bold'])
    time.sleep(5)
    os.system('clear')

    cprint(figlet_format('                    \n  S o l v e r   \n                    ', font='dotmatrix', width=220, justify="center"), 'yellow', 'on_green', attrs=['bold'])
    time.sleep(5)
    os.system('clear')


def matrix(iterations, sleep_time=.08):
    entermatrix()
    messages = []
    d = display()
    import signal
    signal.signal(signal.SIGWINCH, lambda x, y: display.__init__(d))
    for _ in range(iterations):
        #Change the '10' to matrix chars
        messages.append(message(string.ascii_letters, random.randint(1, 5)))
        for text in messages:
            d.set_vertical(text.x, text.y, text)
            text.move()
        sys.stdout.write('\033[1m\033[32m%s\033[0m\r' % d)
        sys.stdout.flush()
        time.sleep(sleep_time)