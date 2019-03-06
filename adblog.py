from . import adbpath
import os
import pandas as pd

modulepath = adbpath.__file__[:-10] + 'LOG/'

if bool(os.listdir(modulepath)):
    pass
else:
    with open(modulepath + 'log.txt', 'w', encoding='utf-8') as f:
        f.write('%s,%s,%s\n' % ('品牌名称', '生成时间', '人群包名称', '逻辑单元数'))


def adbloginfo(brand, sptime, personname, dragcount):
    with open(modulepath + 'log.txt', 'a', encoding='utf-8') as f:
        f.write('%s,%s,%s,%s\n' % (brand, sptime, personname, dragcount))


def logdf():
    df = pd.DataFrame()
    for i in os.listdir(modulepath):
        _df = pd.read_csv(modulepath + i, encoding='utf-8')
        _df.columns = ['品牌名称', '生成时间', '人群包名称', '逻辑单元数']
        _df['生成时间'] = pd.to_datetime(_df['生成时间'])
        df = pd.concat([df, _df])
    return df.drop_duplicates()
