#!usr/bin/env python
# coding=utf-8

import re

str = """
sn=LEA7E06230580031, imeid1=861124030282665, imeid2=861124030282673, imeid3=null, imeid4=null, woid=HUBE, pallet=HCLEX528P66AHUBE0019, boxnum=LPS366A01579, battery=LE40800000281616652FHR5, charge=LE408400002826456590B8Q, nal=161664000235600, btaddr=C825E1B2A346, spare1=LP031271E6220366071, spare2=C825E1B673D6, spare3=keybox_86112403028266.bin, spare4=IJXCNCM5601405234S, mainId=1465597857345, spare5=5.132, spare6=null, spare7=447, spare8=null, spare9=null, spare10=null, valid=0, snDatetime=2016-6-10 15:26:28. 0, imeiDatetime=2016-6-10 15:26:28. 0, nalDatetime=2016-6-10 16:59:53. 0, bindDatetime=2016-6-10 15:26:28. 0, biDatetime=2016-6-11 1:24:12. 0, sscc=null, custSn=null, custPo=null, erpPo=null, custPartnumber=null, innerPartnumber=null, factoryName=null, custMachine=null, createTime=null, updateTime=null, boxCount=null, mPwd1=null, mPwd2=null, mPwd3=null, PalletWeight=418800, mPwd4=null, mPwd5=null, bi4PalletDatetime=null, spare11=null, spare12=null, spare13=null, spare14=null, spare15=null, spare16=null, spare17=null, spare18=null, spare19=null, spare20=
"""


a= re.split("(=[.]*,)?", str);
print(a)
a = [value for i, value in enumerate(a) if i % 2 == 1]

print(a)
