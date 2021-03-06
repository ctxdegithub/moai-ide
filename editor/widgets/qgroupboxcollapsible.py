import PySide

from PySide import QtCore, QtGui
from PySide.QtGui import QGroupBox

class QGroupBoxCollapsible (QGroupBox):
    def __init__(self, parent=None):
        super(QGroupBoxCollapsible, self).__init__(parent)
        self.toggled.connect(self.collapse)

    @QtCore.Slot(bool)
    def collapse(self, flag):
        for child in self.children():
            if hasattr(child, "setVisible"):
                child.setVisible(flag)