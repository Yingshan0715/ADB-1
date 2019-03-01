from .actionfunc import set_pause
# Class Behavior function
from .actionfunc import click2, ppaste
from .actionfunc import position as dw
# Reaction of pyautogui action
from .actionfunc import somedays
from .actionfunc import t365, t180, tnow
from .actionfunc import swtime, timedelta, checktime, two_check_time
# Checking function

from .baseclass import set_ROF
from .autoclass import AutoDatabank
# Auto Class

from .adblog import logdf
#Log system

aalc = AutoDatabank(2)


def shan_renqun(num=1, ordernum=1, has_sousuoci=False):
    aalc.srq(num, ordernum, has_sousuoci)
