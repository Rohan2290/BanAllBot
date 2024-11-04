import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv(25206101))
    API_HASH = os.getenv(2135724a8fdecb737f31d22ec8e6894b)
    BOT_TOKEN = os.getenv(7782160094:AAFBnV4svrGDUicXVguCoKQOdE2JUuxy_dY)
    sudo = os.getenv(7601457849)
    SUDO = [7601457849]
    if sudo:
        SUDO = make_int(sudo)
