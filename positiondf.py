from pyautogui import size
import json
from . import adbpath

modulepath = adbpath.__file__[:-10] + 'setini/'

with open(modulepath + 'j2073600', 'r') as f:
    positiondict_1920_1080 = json.load(f)

with open(modulepath + 'j1049088', 'r') as f:
    positiondict_1366_768 = json.load(f)

if size() == (1920, 1080):
    positiondict = positiondict_1920_1080
elif size() == (1366, 768):
    positiondict = positiondict_1366_768
else:
    raise NameError('非标准屏幕')

#★★★★★★★★★★#
with open(modulepath + 'KEYARGS', 'r') as f:
    ARGS = json.load(f)

STANDARDDEP = ARGS['depths']
pk = ARGS['pk']
p1 = (pk[1] + 420, pk[0] + 190)


def mglogic_1920_1080(m, n):
    return {
        'j': (p1[0] + 417 + 00, STANDARDDEP * m + 33 * n + p1[1] + 27),
        'b': (p1[0] + 417 + 30, STANDARDDEP * m + 33 * n + p1[1] + 27),
        'c': (p1[0] + 417 + 60, STANDARDDEP * m + 33 * n + p1[1] + 27),
        '1': (p1[0] + 417 + 00, STANDARDDEP * m + 33 * n + p1[1] + 27),
        '2': (p1[0] + 417 + 30, STANDARDDEP * m + 33 * n + p1[1] + 27),
        '3': (p1[0] + 417 + 60, STANDARDDEP * m + 33 * n + p1[1] + 27)}


def mglogic_1366_768(m, n):
    return {
        'j': (p1[0] + 293 + 00, STANDARDDEP * m + 33 * n + p1[1] + 27),
        'b': (p1[0] + 293 + 30, STANDARDDEP * m + 33 * n + p1[1] + 27),
        'c': (p1[0] + 293 + 60, STANDARDDEP * m + 33 * n + p1[1] + 27),
        '1': (p1[0] + 293 + 00, STANDARDDEP * m + 33 * n + p1[1] + 27),
        '2': (p1[0] + 293 + 30, STANDARDDEP * m + 33 * n + p1[1] + 27),
        '3': (p1[0] + 293 + 60, STANDARDDEP * m + 33 * n + p1[1] + 27)}

if size() == (1920, 1080):
    mglogic = mglogic_1920_1080
elif size() == (1366, 768):
    mglogic = mglogic_1366_768
else:
    raise NameError('非标准屏幕')
# location dict of logical action


def contents(n):
    return 280, (n - 1) * STANDARDDEP + pk[1] + 205
# location function of contents


def pp(ppnum):
    if ppnum == -1:
        return p1[0] + 60, p1[1] - 43
    else:
        return p1[0], STANDARDDEP * (ppnum - 1) + p1[1]
# location function of child-window items


def dragxy(ip, n):
    '''ip always like ip=pp(-1:-->int type)'''
    return ip[0], ip[1] + (n - 1) * 27 + 37
# location function of child-window-selection used with pp function


def pt(ordernum):
    return {'xdsj': (p1[0] - 37, STANDARDDEP * (ordernum - 2) + 34 + p1[1]),
            'jdsj': (p1[0] + 37, STANDARDDEP * (ordernum - 2) + 34 + p1[1])}
# location function used for click2 timetyple


def ptt(timenum, Downstyle=True):
    if Downstyle:
        return {'leftt': (p1[0] + 000, STANDARDDEP * (timenum - 3) + 70 + p1[1]),
                'right': (p1[0] + 265, STANDARDDEP * (timenum - 3) + 70 + p1[1])}
    else:
        return {'leftt': (p1[0] + 000, STANDARDDEP * (timenum - 3) + 70 + p1[1] - 280),
                'right': (p1[0] + 265, STANDARDDEP * (timenum - 3) + 70 + p1[1] - 280)}
# location function used for jdsj-time-blank
