"""
This is a stubbed out test file designed to be used with PyTest, but can 
easily be modified to support any testing framework.
"""

from pathlib import Path
import sys

# from dotenv import find_dotenv, load_dotenv

# get paths to useful resources - notably where the src directory is
self_pth = Path(__file__)
dir_test = self_pth.parent
dir_prj = dir_test.parent
dir_src = dir_prj / 'src'

# load up the environment variables from the environment file mimicing being set on the local machine
# load_dotenv(find_dotenv())

# insert the src directory into the path and import the projct package
sys.path.insert(0, str(dir_src))
import py_message

def test_send_sms():

    message = "Test Py-Message SMS"
    resp_lst = py_message.send_sms(message)

    assert all([resp.successful for resp in resp_lst])


def test_send_pushover():

    message = "Test Py-Message Pushover"
    resp = py_message.send_pushover(message)
    
    assert(resp)


if __name__ == '__main__':
    test_send_sms()
    test_send_pushover()
