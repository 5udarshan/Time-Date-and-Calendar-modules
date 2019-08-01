Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.time ()
1564254094.7432134
>>> time.asctime ()
'Sun Jul 28 00:31:52 2019'
>>> time.localtime (1564254094.7432134)
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=28, tm_hour=0, tm_min=31, tm_sec=34, tm_wday=6, tm_yday=209, tm_isdst=0)
>>> time.ctime ()
'Sun Jul 28 00:33:49 2019'
>>> time.get_clock_info ()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    time.get_clock_info ()
TypeError: get_clock_info() takes exactly 1 argument (0 given)
>>> time.monotonic ()
1228.632
>>> time.gmtime ()
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=27, tm_hour=19, tm_min=4, tm_sec=38, tm_wday=5, tm_yday=208, tm_isdst=0)
>>> time.sleep ()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    time.sleep ()
TypeError: sleep() takes exactly one argument (0 given)
>>> 
