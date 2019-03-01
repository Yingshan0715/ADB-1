from .actionfunc import click2, ppaste, swtime
from .positiondf import positiondict, pp, dragxy, pt, ptt
from pyautogui import scroll, moveTo


def aclick_after_clickdown(father, son, Downstyle=False):
    if Downstyle:
        click2(pp(father))
        moveTo(dragxy(pp(father), 2), duration=0.5, pause=0.5)
        scroll(clicks=-2500, pause=0.5)
        click2(dragxy(pp(father), son))
    else:
        click2(pp(father))
        click2(dragxy(pp(father), son))


def clicks_after_clickdown(father, sons):
    if isinstance(sons, int):
        click2(pp(father))
        for i in str(sons):
            #assert 1 <= int(i) <= 5
            click2(dragxy(pp(father), int(i)))
        click2(positiondict['blankk'])
    else:
        raise Exception('int!')


def input_in_twoblocks(crows, qujianlist):
    assert isinstance(qujianlist, list)
    mind, maxd = qujianlist[0], qujianlist[1]
    #assert isinstance(mind, int) and isinstance(maxd, int) and (mind <= maxd)
    aclick_after_clickdown(crows, 3)
    click2((pp(crows)[0] + 100, pp(crows)[1]))
    ppaste(mind)
    click2((pp(crows)[0] + 200, pp(crows)[1]))
    ppaste(maxd)


def datetime_ptptt(timeposition, start_date, end_date, Downstyle):
    assert isinstance(timeposition, int)
    click2(pt(timeposition - 1)['jdsj'])
    click2(ptt(timeposition, Downstyle=True)['leftt'])
    click2(ptt(timeposition, Downstyle=Downstyle)['leftt'])
    ppaste(swtime(start_date))
    click2(ptt(timeposition, Downstyle=Downstyle)['right'])
    ppaste(swtime(end_date))
