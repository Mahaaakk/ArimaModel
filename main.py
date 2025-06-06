import sys
import os

from ImageProc.exception import ImageProcException
from ImageProc.logger import logging


def test_exception():
    try:
        logging.info("There is an error here in this line")
        a=1/0
    except Exception as e:
        raise ImageProcException(e,sys)
        

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)