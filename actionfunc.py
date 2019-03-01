from pyautogui import moveTo, click, mouseDown, hotkey, position
from random import choice, randint
import pyperclip
import pyautogui

from .positiondf import positiondict

pyautogui.FAILSAFE = 1  # 1代表True，表示可以使用左上角打断
pyautogui.PAUSE = 0.65  # 标准库的截断时间

DEFAULT_DURA = 0.11
DEFAFLLTPAUSE = 0.13


def set_pause(pause=0.101, dura=0.15):
    '''setting the speed of click2 in pause and dura'''
    global DEFAFLLTPAUSE
    DEFAFLLTPAUSE = pause
    print('Pause was set to %s seconds' % DEFAFLLTPAUSE)
    global DEFAULT_DURA
    DEFAULT_DURA = dura
    print('Dura was set to %s seconds' % DEFAULT_DURA)


def click2(xy):
    '''xy为长度为2的元组，代表一个屏幕坐标'''
    moveTo(xy, duration=DEFAULT_DURA,
           tween=easeOutQuad, pause=0)
    click(pause=DEFAFLLTPAUSE)


def dragg(location):
    '''complexed action for instead of dragg action from pyautogui.dragto '''
    click(location)
    mouseDown()
    moveTo(positiondict['dragposition'][0] + randint(0, 300),
           positiondict['dragposition'][1],
           duration=0.5,
           tween=easeOutQuad)
    click()


def ppaste(astr):
    '''Recreated typwrite for ###supportting chinese-lang'''
    pyperclip.copy(astr)
    hotkey('ctrl', 'v')


from datetime import datetime, timedelta
from dateutil.parser import parse


def swtime(timeinput, StrType=True):
    ''' input-datetime switch to str,For example:
    int ：811 → means 20XX-08-11 ,
    str : '2017-11-11' convert to standard-datetime-style'''
    if isinstance(timeinput, int):
        # 快捷方式
        anyinput = str(timeinput)[:-2] + '-' + str(timeinput)[-2:]
        return parse(anyinput).strftime('%Y-%m-%d') if StrType else parse(anyinput)
    elif isinstance(timeinput, str):
        # str ~ time 标准格式
        return parse(timeinput).strftime('%Y-%m-%d') if StrType else parse(timeinput)
    elif isinstance(timeinput, datetime):
        # 标准时间库
        return timeinput.strftime('%Y-%m-%d') if StrType else parse(timeinput.strftime('%Y-%m-%d'))
    else:
        raise TypeError('输入类型错误：int or str or datetime & 须在时间范围之内')


def somedays(dtinput, theday=90):
    return swtime(swtime(dtinput, False) - timedelta(theday))


tnow = swtime(datetime.now() - timedelta(1), False)
t180 = swtime(datetime.now() - timedelta(180), False)
t365 = swtime(datetime.now() - timedelta(365), False)


def checktime(inputtime, defultChecking=True):
    '''time checkfunction'''
    if defultChecking:
        return t180 <= swtime(inputtime, False) <= tnow
    else:
        return t365 <= swtime(inputtime, False) <= tnow


def two_check_time(ts, te, defultChecking=True):
    if defultChecking:
        return checktime(ts) and checktime(te) and (swtime(ts, False) <= swtime(ts, False))
    else:
        return checktime(ts, False) and checktime(te, False) and (swtime(ts, False) <= swtime(ts, False))
