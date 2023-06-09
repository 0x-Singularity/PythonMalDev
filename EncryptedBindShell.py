import socket
import subprocess
import threading
import argparse

DEFAULT_PORT = 1234
MAX_BUFFER = 4096


def execute_cmd(cmd):
    try:
        output = subprocess.check_output(
            "cmd /c {}".format(cmd), strderr=subprocess.STDOUT)
    except:
        output = b"Command Failed!"
    return output


print(execute_cmd("whoami"))
