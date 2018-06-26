import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

device = mr.waitForConnection(5.0)
if not device:
	print >> sys.stderr,"fail"
	sys.exit(1)

componentName = "com.freeme.camera/.CameraActivity"
device.startActivity(component="com.freeme.camera/com.freeme.camera.CameraActivity")
mr.sleep(3.0)
device.touch(368,1238,'DOWN_AND_UP')
a = 500
while(a > 0):
	mr.sleep(1)
        device.touch(368,1238,'DOWN_AND_UP')
	a = a - 1
	
	http://192.168.48.12:8080/camera/FreemeCamera-AS.git


