#!/usr/bin/env python
 
import dbus
import time
import threading
 
class Notification:
 
        def __init__(self):
                self.app_name = ""
                self.replaces_id = 0
                self.app_icon = ""
                self.summary = ""
                self.body = ""
                self.actions = []
                self.hints = {}
                self.expire_timeout = 1000
 
                try:
                        session_bus = dbus.SessionBus()
                        obj = session_bus.get_object("org.freedesktop.Notifications","/org/freedesktop/Notifications")
                        self.interface = dbus.Interface(obj, "org.freedesktop.Notifications")
                except Exception:
                        self.interface = None
 
        def setAppName(self, app_name):
                self.app_name = app_name
 
        def setReplacesId(self, replaces_id):
                self.replaces_id = replaces_id
 
        def setIcon(self, app_icon):
                self.app_icon = app_icon
 
        def setSummary(self, summary):
                self.summary = summary
 
        def setBody(self, body):
                self.body = body
 
        def addAction(self, action):
                t.append(action)
 
        def addHint(self, hint):
                pass # TODO
 
        def setTimeout(self, expire_timeout):
                self.expire_timeout = expire_timeout * 1000
 
        def setMSTimeout(self, expire_timeout):
                self.expire_timeout = expire_timeout
 
        def notify(self):
                self.interface.Notify(self.app_name, self.replaces_id, self.app_icon, self.summary, self.body, self.actions, self.hints, self.expire_timeout)
 
class Timer(threading.Thread):
	 	def __init__(self, seconds):
 			self.runTime = seconds
 			threading.Thread.__init__(self)
 		def run(self):
 			time.sleep(self.runTime)
 			#print "Buzzzz!! Time's up!"
			notif = Notification()
			notif.setAppName("Pymodoro")
			notif.setSummary("Is the task ended?")
			notif.setBody("time's up ! \n Put a check on your sheet of paper")
			notif.setIcon("/home/ffourc/Projets/pymodoro/pomodoro.jpg")
			#notif.setTimeout(7)
			notif.notify()
t = Timer(1500)
t.start()

