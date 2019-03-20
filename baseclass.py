import time
import pyautogui
import pyperclip
from datetime import datetime
from threading import Thread

from .positiondf import positiondict, contents, mglogic, pp, dragxy
from .actionfunc import click2, dragg, ppaste
from .actionfunc import two_check_time
from .combaction import aclick_after_clickdown, clicks_after_clickdown
from .combaction import datetime_ptptt, input_in_twoblocks
from .adblog import adbloginfo


class BaseAuto():
    __slots__ = ('zhanghao', '_tmall_global', '_purchase_Behaviour',
                 'drgcount', 'smallscreen',
                 'yybp_order', 'ppld_order',
                 'ppzq_order', 'mxdp_order', 'zszw_order')

    def __init__(init, zhanghao=2, tmall_global=False,
                 purchase_Behaviour='dp', brand_name='未命名'):
        init.tmall_global = tmall_global
        init.purchase_Behaviour = purchase_Behaviour
        init.zhanghao = zhanghao
        init.brand_name = brand_name

        init.drgcount = 0
        init.smallscreen = pyautogui.size() == (1366, 768)

        init.yybp_order = zhanghao
        init.ppld_order = zhanghao
        init.ppzq_order = zhanghao
        init.mxdp_order = zhanghao
        init.zszw_order = zhanghao

        if (not init.tmall_global) and (purchase_Behaviour == 'gj'):
            raise Error('No gjp in no-tmall_global')

    @property
    def tmall_global(self):
        return self._tmall_global

    @tmall_global.setter
    def tmall_global(self, value):
        if value not in [True, False]:
            raise TypeError('Only True and False')
        self._tmall_global = value

    @property
    def purchase_Behaviour(self):
        return self._purchase_Behaviour

    @purchase_Behaviour.setter
    def purchase_Behaviour(self, value):
        if value not in ['dp', 'gj']:
            raise TypeError('Only dp and gj')
        self._purchase_Behaviour = value

    def _createpeople(self):
        click2(positiondict['diyichuangkou'])
        pyautogui.keyDown('f5')
        time.sleep(2)
        click2(positiondict['zidingyirenqun'])
        time.sleep(1)
        click2(positiondict['xinjianrenqun'])
        time.sleep(4)
        click2(positiondict['diyichuangkouguanbi'])
        self.drgcount = 0
    cp = _createpeople

    def _savepeople(self, people_name, yanzheng=True):
        click2(positiondict['renqunmingcheng'])
        ppaste(people_name)

        if yanzheng:
            if self.smallscreen:
                pyautogui.moveTo(
                    positiondict['countnumber'], duration=0.25, pause=0.25)
                pyautogui.doubleClick()
                pyautogui.hotkey('ctrl', 'c')
            else:
                pyautogui.hotkey('ctrl', 'shift', 'i')
                pyautogui.moveTo(
                    positiondict['countnumber'], duration=0.25, pause=0.25)
                pyautogui.doubleClick()
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.hotkey('ctrl', 'shift', 'i')

            assert int(pyperclip.paste()) == self.drgcount  # 网络不稳定

        click2(positiondict['baocun'])
        click2(positiondict['baocunqueding'])

        timenow = datetime.now().strftime('%Y-%m-%d')
        adbloginfo(self.brand_name, timenow, people_name, self.drgcount)

        time.sleep(1)

    sp = _savepeople

    def _drag_to_workspace_and_jbc(self, wz, nm, nn, jbc):
        # if self.drgcount == 2:
        #    self.drgcount = 1
        #    dragg(contents(wz))
        self.drgcount += 1
        dragg(contents(wz))

        jbc = str(jbc)
        assert jbc in 'jbc123'
        click2(mglogic(nm, nn)[jbc])

    def srq(self, num=1, ordernum=1, has_sousuoci=False):
        assert isinstance(num, int) and isinstance(ordernum, int)
        click2(positiondict['diyichuangkou'])
        click2(positiondict['zidingyirenqun'])
        pyautogui.scroll(clicks=2000)

        for i in range(num):
            px, py = positiondict['delete']
            po_delete = px, py + 60 * ordernum - 60
            if has_sousuoci:
                pyautogui.click(positiondict['fangdajing'], pause=0.5)
            pyautogui.click(po_delete, pause=0.6)
            pyautogui.click(positiondict['confirm_de'], pause=0.7)
            pyautogui.click(positiondict['confirm_dede'], pause=0.6)

    def _quanlianluzhuangtai(self, aipl, start_date, end_date, jbc):
        '''全链路状态---全链路状态'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 1, 2, 2, 4
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        clicks_after_clickdown(1, aipl)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def jcsx(self, kk, jj, jbc):
        '''属性圈人---基础属性'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 10, 2, 0, 0
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(1, kk)
        clicks_after_clickdown(2, jj)
        #-----------------------------------------------------------------------------------#
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def xfxw(self, kk, jj, jbc):
        '''属性圈人---基础属性'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 12, 2, 0, 0
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(1, kk)
        clicks_after_clickdown(2, jj)
        #-----------------------------------------------------------------------------------#
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def pjpc(self, jj, jbc):
        '''属性圈人---啤酒频次'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 14, 2, 0, 0
        click2(contents(13))
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        click2(contents(16))
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(1, 4, Downstyle=True)
        clicks_after_clickdown(2, jj)
        #-----------------------------------------------------------------------------------#

        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def ss(self, words, start_date, end_date, jbc='j'):
        '''搜索'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 3, 1, 2, 3
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        Downstyle = True  # Always True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #-----------------------------------------------------------------------------------#
        click2(pp(1))
        ppaste(words)
        click2(positiondict['zuoroll'])
        pyautogui.click(positiondict['zuoroll'], clicks=50, duration=1)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def super_ss(self, words, start_date, end_date, jbc='bb'):
        '''超级搜索'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        swords = words.split(',')
        for i in range(len(swords) // 20 + 1):
            _jbc = jbc[0] if i == 0 else jbc[1]
            pas_words = ','.join(swords[i * 20:i * 20 + 20])
            self.ss(pas_words, start_date, end_date, _jbc)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _fufeiguanggao(self, fenlei, qujian, start_date, end_date, jbc,
                       action, position_of_Real):
        '''付费广告总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 4, 2, 2, 4
        assert two_check_time(start_date, end_date, False)
        assert isinstance(qujian, list) and len(qujian) == 2
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        aclick_after_clickdown(-1, fenlei)
        #-----------------------------------------------------------------------------------#
        if 3 <= fenlei <= 7:  # yybp # ppld # ppzq # mxdp # zszw
            aclick_after_clickdown(1, position_of_Real)  # 账号
            aclick_after_clickdown(2, action)
            input_in_twoblocks(3, qujian)
            tt = 5
        else:
            aclick_after_clickdown(1, action)
            input_in_twoblocks(2, qujian)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _pinpaihao(self, actiontype, action, start_date, end_date, jbc):
        '''品牌号总方法---单独的内容方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 5, 1, 0, 4
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(1, actiontype)
        aclick_after_clickdown(2, action)
        if actiontype == 1:
            tt = 5
            aclick_after_clickdown(3, 1)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _neirongyunying(self, fenlei, action, start_date, end_date, jbc):
        '''内容运营总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 5, 1, 0, 4
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#

        if fenlei == 2:
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, 1)
            aclick_after_clickdown(2, 1)
            aclick_after_clickdown(3, action)
            tt = 5
        elif fenlei == 7:
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, action)
            aclick_after_clickdown(2, 1)
            aclick_after_clickdown(3, 1)
            tt = 5
        elif fenlei in [3, 4, 5, 6]:
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, action)
        elif fenlei == 8:
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, 1)
            aclick_after_clickdown(2, action)
            aclick_after_clickdown(3, 1)
            aclick_after_clickdown(4, 1)
            tt = 6
        elif fenlei == 10:
            aclick_after_clickdown(-1, 8, Downstyle=True)
            aclick_after_clickdown(1, action)
            if action != 3:
                aclick_after_clickdown(2, self.zhanghao)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def tbtt_v(self, action, start_date, end_date, jbc):
        '''内容运营---淘宝头条---V任务'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 5, 1, 0, 5
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(-1, 2)

        aclick_after_clickdown(1, 2)
        aclick_after_clickdown(2, 1)
        aclick_after_clickdown(3, action)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def wt_v(self, action, start_date, end_date, jbc):
        '''内容运营---微淘---V任务'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 5, 1, 0, 6
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(-1, 8)

        aclick_after_clickdown(1, 1)
        aclick_after_clickdown(2, action)
        aclick_after_clickdown(3, 2)
        aclick_after_clickdown(4, 1)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def wt_gg(self, action, start_date, end_date, jbc):
        '''内容运营---微淘---关注'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 5, 1, 0, 4
        assert two_check_time(start_date, end_date)
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(-1, 8)

        aclick_after_clickdown(1, 2)
        aclick_after_clickdown(2, action)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _yingxiaopingtai(self, fenlei, actiontype, action, start_date, end_date, jbc):
        '''天猫营销平台总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 6, 1, 2, 4
        assert two_check_time(start_date, end_date)
        click2(contents(6))
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        click2(contents(10))
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(-1, fenlei)
        if fenlei in [1, 8]:
            tt = 3
            aclick_after_clickdown(1, action)
        elif fenlei == 2:
            aclick_after_clickdown(1, actiontype)
            aclick_after_clickdown(2, action)
        elif fenlei == 3:
            aclick_after_clickdown(1, actiontype)
            aclick_after_clickdown(2, action)
            aclick_after_clickdown(3, 1)
            tt = 5
        elif fenlei == 6:  # 天猫优先
            aclick_after_clickdown(1, 1)
            aclick_after_clickdown(2, action)
            #aclick_after_clickdown(3, 1)
            tt = 5
        else:
            aclick_after_clickdown(1, action)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if (self.smallscreen and tt > 3) else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _xiaoshouqudao(self, fenlei, action, start_date, end_date, jbc):
        '''销售渠道总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz,  tt = 7,  4
        nm = 2 if self._tmall_global else 1
        nn = 2 if self._tmall_global else 0
        assert two_check_time(start_date, end_date)
        click2(contents(6))
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        click2(contents(10))
        aclick_after_clickdown(-1, fenlei)
        #-----------------------------------------------------------------------------------#
        if fenlei in [1, 4]:
            aclick_after_clickdown(1, self.zhanghao)
            aclick_after_clickdown(2, action)
        elif fenlei == 3:
            aclick_after_clickdown(1, action)
            tt = 3
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _xianxiachudian(self, fenlei, action, start_date, end_date, jbc):
        '''线下触点总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nn, nm,  tt = 8, 1, 2, 3
        assert two_check_time(start_date, end_date)
        click2(contents(6))
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        click2(contents(10))
        aclick_after_clickdown(-1, fenlei)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(1, action)
        if (fenlei == 1) and (action == 3):
            click2((650, 345))
            click2((650, 380))
        tt = 4 if fenlei == 2 else 3
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen and tt > 3 else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def _dianpushangpin(self, fenlei, action, start_date, end_date, jbc):
        '''店铺圈人方法总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        saction = str(action)

        if len(saction) >= 2:
            tt = 6
        elif saction == '1':
            tt = 7
        elif saction in '234':
            tt = 6
        elif saction == '5':
            tt = 8

        if action == 5:
            assert two_check_time(start_date, end_date, False)
        else:
            assert two_check_time(start_date, end_date)
        #-----------------------------------------------------------------------------------#
        wz, nm, nn = 8, 2, 3
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        if fenlei == 1:
            tt -= 1
            #aclick_after_clickdown(1, 1)
            clicks_after_clickdown(2, action)
        elif fenlei in [3, 4, 6, 7]:  # 天猫国际直营 # 天猫超市 全球购 淘宝集市
            aclick_after_clickdown(-1, fenlei)
            #aclick_after_clickdown(1, 1)
            #aclick_after_clickdown(2, 1)
            clicks_after_clickdown(3, action)
        else:  # fenlei == 2 or 5
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, self.zhanghao)
            aclick_after_clickdown(2, 1)
            clicks_after_clickdown(3, action)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def hy(self, action, start_date, end_date, jbc='j'):
        '''会员方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn, tt = 15, 1, 0, 3
        assert two_check_time(start_date, end_date)
        if self.smallscreen:
            click2(contents(1))
            pyautogui.scroll(clicks=-2500)
            wz = 9
            self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
            click2(contents(1))
            pyautogui.scroll(clicks=2500)
        else:
            self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        #-----------------------------------------------------------------------------------#
        aclick_after_clickdown(1, action)
        #-----------------------------------------------------------------------------------#
        Downstyle = True  # Always True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def zdy(self, peo1, jbc='j', usess=1):
        '''项目自定义人方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        wz, nm, nn = 17, 1, 0
        if self.smallscreen:
            click2(contents(1))
            pyautogui.scroll(clicks=-2500)
            wz = 11
            self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
            click2(contents(1))
            pyautogui.scroll(clicks=2500)
        else:
            self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        click2(pp(1))
        click2(pp(2))
        ppaste(peo1)
        pusess = dragxy(pp(1), 1 + usess)[0], dragxy(pp(1), 1 + usess)[1] + 10
        click2(pusess)
        click2(positiondict['blankk'])
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def klnll(self, fenlei, cishu, start_date, end_date, jbc):
        '''科罗娜浏览---店铺圈人方法总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        assert two_check_time(start_date, end_date, False)
        action = 1
        tt = 7
        #-----------------------------------------------------------------------------------#
        wz, nm, nn = 8, 2, 3
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        if fenlei == 1:
            tt -= 1
            #aclick_after_clickdown(1, 1)
            clicks_after_clickdown(2, action)
            input_in_twoblocks(3, cishu)
        else:
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, self.zhanghao)
            aclick_after_clickdown(2, 1)
            clicks_after_clickdown(3, action)
            input_in_twoblocks(4, cishu)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

    def klngm(self, fenlei, jine, start_date, end_date, jbc):
        '''科罗娜购买---店铺圈人方法总方法'''
        #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
        assert two_check_time(start_date, end_date, False)
        action = 5
        tt = 8
        #-----------------------------------------------------------------------------------#
        wz, nm, nn = 8, 2, 3
        self._drag_to_workspace_and_jbc(wz, nm, nn, jbc)
        if fenlei == 1:
            tt -= 1
            #aclick_after_clickdown(1, 1)
            clicks_after_clickdown(2, action)
            input_in_twoblocks(3, cishu)
        else:
            aclick_after_clickdown(-1, fenlei)
            aclick_after_clickdown(1, self.zhanghao)
            aclick_after_clickdown(2, 1)
            clicks_after_clickdown(3, action)
            input_in_twoblocks(5, jine)
        #-----------------------------------------------------------------------------------#
        Downstyle = False if self.smallscreen else True
        datetime_ptptt(tt, start_date, end_date, Downstyle)
        #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
