""" Run a simple printing loop """

from datetime import datetime
from time import sleep


def get_current_time_str() -> str:
    """ Get the current time in the format Hours:Minutes:Seconds

    Returns:
        The current time.
    """
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def main():
    """ The main script loop """
    for i in range(10):
        print(f"Line {i + 1}.  Time is now {get_current_time_str()}")
        sleep(0.1) # Do nothing for tenth of a second.


if __name__ == "__main__":
    main()
