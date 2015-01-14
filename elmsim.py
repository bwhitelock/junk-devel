#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#elmapp="tk"

import sys
from multiprocessing import Queue
thisQueue=Queue()
try:
    from elmDevice.elmDevice import elmDevice as elmDevice
    device=elmDevice(thisQueue)
    device.start()
except ImportError:
    print "The module elmDevice can not be found"

#from elmsim_tk import simpleapp_tk

# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
#gui = 'tk'

try:
    if total > 1:
        print "use tk not wx"
        raise ImportError,"don't want to use wx right now"
    import wx
    #import wx1
    #import elmsim_wx
except ImportError:
    print "trying tkinter"
    try:
        import Tkinter
    except ImportError:
        print "The python-tk or the wxPython module is required to run this program."
    else:
        #gui = 'tk'
        print "running tk app"
        from tkinter.elmsim_tk import simpleapp_tk as myApp
        #app=simpleapp_tk(None,device,thisQueue)
        app=myApp(None,device,thisQueue)
        app.title('ELM327 Test Simulator TK')
        app.mainloop()
else:
    print "running wx app"
    #import elmsim_wx
    from wxpython.elmsim_wx import simpleapp_wx as myApp
    #gui = 'wx'
    app = wx.App()
    frame = myApp(None,-1,'ELM327 Simulator',device,thisQueue)
    app.MainLoop()

print "done"
