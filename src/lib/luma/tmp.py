'''
Created on 2. feb. 2011

@author: Christian
'''

from plugins.browser_plugin.BrowserView import BrowserView
from PyQt4 import QtGui, QtCore
import sys

       
        
if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    
    b = BrowserView(None,"/tmp")
    b.show()
    
    sys.exit(app.exec_())