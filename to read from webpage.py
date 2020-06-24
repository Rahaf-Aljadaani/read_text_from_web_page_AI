
#لقراءة الكلام العربي من الصفحة

import urllib.request
import urllib.parse
import re

url = 'https://s-m.com.sa/tr/login.html'#موقعنا=)

fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")# أخذ الكود الأصلي للموقع
fp.close()

print(mystr)

#ولأن الموقع بالعربي اتبعت ذي الطريقة
# تصفيت الكلام الغير مرغوب ككلمات البرمجة ورموزها

tt=''
for t in mystr:
    text=re.sub('[a-z,A-Z,#,'"',"'","//",0-9,]','',t)
    tt+=text

tt2=''
for t in tt:
    text=re.sub('[-,!,<,>,,?,*,%,=,+,.,"(",")",:,@,;,{,},|]','',t)
    tt2+=text

tt3=''
for t in tt2:
    text=re.sub('[\n,\[,\]]','',t)
    tt3+=text

    

print (tt3)
print('-----------')
