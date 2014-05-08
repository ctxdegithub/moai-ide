# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debugdock.ui'
#
# Created: Thu May  8 17:04:49 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_debugdock(object):
    def setupUi(self, debugdock):
        debugdock.setObjectName("debugdock")
        debugdock.resize(459, 673)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(124, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        self.forceGC_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.forceGC_btn.setObjectName("forceGC_btn")
        self.gridLayout.addWidget(self.forceGC_btn, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.reportHistogram_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.reportHistogram_btn.setObjectName("reportHistogram_btn")
        self.gridLayout.addWidget(self.reportHistogram_btn, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(124, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 15, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.partitionCells = QtGui.QCheckBox(self.groupBox)
        self.partitionCells.setObjectName("partitionCells")
        self.gridLayout_2.addWidget(self.partitionCells, 0, 0, 1, 1)
        self.partitionPaddedCells = QtGui.QCheckBox(self.groupBox)
        self.partitionPaddedCells.setObjectName("partitionPaddedCells")
        self.gridLayout_2.addWidget(self.partitionPaddedCells, 1, 0, 1, 1)
        self.partitionPaddedCellsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partitionPaddedCellsWidth.sizePolicy().hasHeightForWidth())
        self.partitionPaddedCellsWidth.setSizePolicy(sizePolicy)
        self.partitionPaddedCellsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.partitionPaddedCellsWidth.setObjectName("partitionPaddedCellsWidth")
        self.gridLayout_2.addWidget(self.partitionPaddedCellsWidth, 1, 1, 1, 1)
        self.textBox = QtGui.QCheckBox(self.groupBox)
        self.textBox.setObjectName("textBox")
        self.gridLayout_2.addWidget(self.textBox, 5, 0, 1, 1)
        self.partitionCellsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partitionCellsWidth.sizePolicy().hasHeightForWidth())
        self.partitionCellsWidth.setSizePolicy(sizePolicy)
        self.partitionCellsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.partitionCellsWidth.setObjectName("partitionCellsWidth")
        self.gridLayout_2.addWidget(self.partitionCellsWidth, 0, 1, 1, 1)
        self.textBoxLayout = QtGui.QCheckBox(self.groupBox)
        self.textBoxLayout.setObjectName("textBoxLayout")
        self.gridLayout_2.addWidget(self.textBoxLayout, 8, 0, 1, 1)
        self.textBoxBaselines = QtGui.QCheckBox(self.groupBox)
        self.textBoxBaselines.setObjectName("textBoxBaselines")
        self.gridLayout_2.addWidget(self.textBoxBaselines, 7, 0, 1, 1)
        self.partitionCellsColor = QtGui.QToolButton(self.groupBox)
        self.partitionCellsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.partitionCellsColor.setText("")
        self.partitionCellsColor.setObjectName("partitionCellsColor")
        self.gridLayout_2.addWidget(self.partitionCellsColor, 0, 2, 1, 1)
        self.partitionPaddedCellsColor = QtGui.QToolButton(self.groupBox)
        self.partitionPaddedCellsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.partitionPaddedCellsColor.setText("")
        self.partitionPaddedCellsColor.setObjectName("partitionPaddedCellsColor")
        self.gridLayout_2.addWidget(self.partitionPaddedCellsColor, 1, 2, 1, 1)
        self.propModelBounds = QtGui.QCheckBox(self.groupBox)
        self.propModelBounds.setObjectName("propModelBounds")
        self.gridLayout_2.addWidget(self.propModelBounds, 2, 0, 1, 1)
        self.propWorldBounds = QtGui.QCheckBox(self.groupBox)
        self.propWorldBounds.setObjectName("propWorldBounds")
        self.gridLayout_2.addWidget(self.propWorldBounds, 4, 0, 1, 1)
        self.propModelBoundsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propModelBoundsWidth.sizePolicy().hasHeightForWidth())
        self.propModelBoundsWidth.setSizePolicy(sizePolicy)
        self.propModelBoundsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.propModelBoundsWidth.setObjectName("propModelBoundsWidth")
        self.gridLayout_2.addWidget(self.propModelBoundsWidth, 2, 1, 1, 1)
        self.propModelBoundsColor = QtGui.QToolButton(self.groupBox)
        self.propModelBoundsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.propModelBoundsColor.setText("")
        self.propModelBoundsColor.setObjectName("propModelBoundsColor")
        self.gridLayout_2.addWidget(self.propModelBoundsColor, 2, 2, 1, 1)
        self.propWorldBoundsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propWorldBoundsWidth.sizePolicy().hasHeightForWidth())
        self.propWorldBoundsWidth.setSizePolicy(sizePolicy)
        self.propWorldBoundsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.propWorldBoundsWidth.setObjectName("propWorldBoundsWidth")
        self.gridLayout_2.addWidget(self.propWorldBoundsWidth, 4, 1, 1, 1)
        self.propWorldBoundsColor = QtGui.QToolButton(self.groupBox)
        self.propWorldBoundsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.propWorldBoundsColor.setText("")
        self.propWorldBoundsColor.setObjectName("propWorldBoundsColor")
        self.gridLayout_2.addWidget(self.propWorldBoundsColor, 4, 2, 1, 1)
        self.textBoxWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxWidth.sizePolicy().hasHeightForWidth())
        self.textBoxWidth.setSizePolicy(sizePolicy)
        self.textBoxWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.textBoxWidth.setObjectName("textBoxWidth")
        self.gridLayout_2.addWidget(self.textBoxWidth, 5, 1, 1, 1)
        self.textBoxBaselinesWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxBaselinesWidth.sizePolicy().hasHeightForWidth())
        self.textBoxBaselinesWidth.setSizePolicy(sizePolicy)
        self.textBoxBaselinesWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.textBoxBaselinesWidth.setObjectName("textBoxBaselinesWidth")
        self.gridLayout_2.addWidget(self.textBoxBaselinesWidth, 7, 1, 1, 1)
        self.textBoxLayoutWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxLayoutWidth.sizePolicy().hasHeightForWidth())
        self.textBoxLayoutWidth.setSizePolicy(sizePolicy)
        self.textBoxLayoutWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.textBoxLayoutWidth.setObjectName("textBoxLayoutWidth")
        self.gridLayout_2.addWidget(self.textBoxLayoutWidth, 8, 1, 1, 1)
        self.textBoxColor = QtGui.QToolButton(self.groupBox)
        self.textBoxColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBoxColor.setText("")
        self.textBoxColor.setObjectName("textBoxColor")
        self.gridLayout_2.addWidget(self.textBoxColor, 5, 2, 1, 1)
        self.textBoxBaselinesColor = QtGui.QToolButton(self.groupBox)
        self.textBoxBaselinesColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBoxBaselinesColor.setText("")
        self.textBoxBaselinesColor.setObjectName("textBoxBaselinesColor")
        self.gridLayout_2.addWidget(self.textBoxBaselinesColor, 7, 2, 1, 1)
        self.textBoxLayoutColor = QtGui.QToolButton(self.groupBox)
        self.textBoxLayoutColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBoxLayoutColor.setText("")
        self.textBoxLayoutColor.setObjectName("textBoxLayoutColor")
        self.gridLayout_2.addWidget(self.textBoxLayoutColor, 8, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 15, 1, 1, 1)
        self.allocLog = QtGui.QCheckBox(self.dockWidgetContents)
        self.allocLog.setObjectName("allocLog")
        self.gridLayout.addWidget(self.allocLog, 1, 1, 1, 1)
        self.luaStringEdit = QtGui.QTextEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.luaStringEdit.sizePolicy().hasHeightForWidth())
        self.luaStringEdit.setSizePolicy(sizePolicy)
        self.luaStringEdit.setMaximumSize(QtCore.QSize(16777215, 130))
        self.luaStringEdit.setAcceptRichText(False)
        self.luaStringEdit.setObjectName("luaStringEdit")
        self.gridLayout.addWidget(self.luaStringEdit, 16, 1, 1, 1)
        self.histogram = QtGui.QCheckBox(self.dockWidgetContents)
        self.histogram.setObjectName("histogram")
        self.gridLayout.addWidget(self.histogram, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 319, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 18, 1, 1, 1)
        self.runStringBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.runStringBtn.setObjectName("runStringBtn")
        self.gridLayout.addWidget(self.runStringBtn, 17, 1, 1, 1)
        debugdock.setWidget(self.dockWidgetContents)

        self.retranslateUi(debugdock)
        QtCore.QObject.connect(self.partitionCells, QtCore.SIGNAL("toggled(bool)"), debugdock.togglePartitionCells)
        QtCore.QObject.connect(self.partitionPaddedCells, QtCore.SIGNAL("toggled(bool)"), debugdock.togglePartitionPaddedCells)
        QtCore.QObject.connect(self.propModelBounds, QtCore.SIGNAL("toggled(bool)"), debugdock.togglePropModelBounds)
        QtCore.QObject.connect(self.propWorldBounds, QtCore.SIGNAL("toggled(bool)"), debugdock.togglePropWorldBounds)
        QtCore.QObject.connect(self.textBox, QtCore.SIGNAL("toggled(bool)"), debugdock.toggleTextBox)
        QtCore.QObject.connect(self.textBoxBaselines, QtCore.SIGNAL("toggled(bool)"), debugdock.toggleTextBoxBaselines)
        QtCore.QObject.connect(self.textBoxLayout, QtCore.SIGNAL("toggled(bool)"), debugdock.toggleTextBoxLayout)
        QtCore.QObject.connect(self.partitionCellsWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthPartitionCells)
        QtCore.QObject.connect(self.partitionPaddedCellsWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthPartitionPaddedCells)
        QtCore.QObject.connect(self.propModelBoundsWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthPropModelBounds)
        QtCore.QObject.connect(self.propWorldBoundsWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthPropWorldBounds)
        QtCore.QObject.connect(self.textBoxWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthTextBox)
        QtCore.QObject.connect(self.textBoxBaselinesWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthTextBoxBaselines)
        QtCore.QObject.connect(self.textBoxLayoutWidth, QtCore.SIGNAL("textChanged(QString)"), debugdock.setWidthTextBoxLayout)
        QtCore.QObject.connect(self.partitionCellsColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorPartitionCells)
        QtCore.QObject.connect(self.partitionPaddedCellsColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorPartitionPaddedCells)
        QtCore.QObject.connect(self.propModelBoundsColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorPropModelBounds)
        QtCore.QObject.connect(self.propWorldBoundsColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorPropWorldBounds)
        QtCore.QObject.connect(self.textBoxColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorTextBox)
        QtCore.QObject.connect(self.textBoxBaselinesColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorTextBoxBaselines)
        QtCore.QObject.connect(self.textBoxLayoutColor, QtCore.SIGNAL("clicked()"), debugdock.pickColorTextBoxLayout)
        QtCore.QObject.connect(self.allocLog, QtCore.SIGNAL("toggled(bool)"), debugdock.toggleLuaAllocLogEnabled)
        QtCore.QObject.connect(self.histogram, QtCore.SIGNAL("toggled(bool)"), debugdock.toggleHistogramEnabled)
        QtCore.QObject.connect(self.reportHistogram_btn, QtCore.SIGNAL("clicked()"), debugdock.reportHistogram)
        QtCore.QObject.connect(self.forceGC_btn, QtCore.SIGNAL("clicked()"), debugdock.forceGC)
        QtCore.QObject.connect(self.histogram, QtCore.SIGNAL("toggled(bool)"), self.reportHistogram_btn.setEnabled)
        QtCore.QObject.connect(self.runStringBtn, QtCore.SIGNAL("clicked()"), debugdock.runString)
        QtCore.QMetaObject.connectSlotsByName(debugdock)
        debugdock.setTabOrder(self.histogram, self.allocLog)
        debugdock.setTabOrder(self.allocLog, self.reportHistogram_btn)
        debugdock.setTabOrder(self.reportHistogram_btn, self.forceGC_btn)
        debugdock.setTabOrder(self.forceGC_btn, self.partitionCells)
        debugdock.setTabOrder(self.partitionCells, self.partitionCellsWidth)
        debugdock.setTabOrder(self.partitionCellsWidth, self.partitionPaddedCells)
        debugdock.setTabOrder(self.partitionPaddedCells, self.partitionPaddedCellsWidth)
        debugdock.setTabOrder(self.partitionPaddedCellsWidth, self.propModelBounds)
        debugdock.setTabOrder(self.propModelBounds, self.propModelBoundsWidth)
        debugdock.setTabOrder(self.propModelBoundsWidth, self.propWorldBounds)
        debugdock.setTabOrder(self.propWorldBounds, self.propWorldBoundsWidth)
        debugdock.setTabOrder(self.propWorldBoundsWidth, self.textBox)
        debugdock.setTabOrder(self.textBox, self.textBoxWidth)
        debugdock.setTabOrder(self.textBoxWidth, self.textBoxBaselines)
        debugdock.setTabOrder(self.textBoxBaselines, self.textBoxBaselinesWidth)
        debugdock.setTabOrder(self.textBoxBaselinesWidth, self.textBoxLayout)
        debugdock.setTabOrder(self.textBoxLayout, self.textBoxLayoutWidth)
        debugdock.setTabOrder(self.textBoxLayoutWidth, self.propWorldBoundsColor)
        debugdock.setTabOrder(self.propWorldBoundsColor, self.textBoxColor)
        debugdock.setTabOrder(self.textBoxColor, self.textBoxBaselinesColor)
        debugdock.setTabOrder(self.textBoxBaselinesColor, self.textBoxLayoutColor)
        debugdock.setTabOrder(self.textBoxLayoutColor, self.partitionPaddedCellsColor)
        debugdock.setTabOrder(self.partitionPaddedCellsColor, self.propModelBoundsColor)
        debugdock.setTabOrder(self.propModelBoundsColor, self.partitionCellsColor)

    def retranslateUi(self, debugdock):
        debugdock.setWindowTitle(QtGui.QApplication.translate("debugdock", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.forceGC_btn.setText(QtGui.QApplication.translate("debugdock", "Force Garbage Collection", None, QtGui.QApplication.UnicodeUTF8))
        self.reportHistogram_btn.setText(QtGui.QApplication.translate("debugdock", "Report Histogram", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("debugdock", "Debug Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.partitionCells.setText(QtGui.QApplication.translate("debugdock", "PARTITION_CELLS", None, QtGui.QApplication.UnicodeUTF8))
        self.partitionPaddedCells.setText(QtGui.QApplication.translate("debugdock", "PARTITION_PADDED_CELLS", None, QtGui.QApplication.UnicodeUTF8))
        self.textBox.setText(QtGui.QApplication.translate("debugdock", "TEXT_BOX", None, QtGui.QApplication.UnicodeUTF8))
        self.textBoxLayout.setText(QtGui.QApplication.translate("debugdock", "TEXT_BOX_LAYOUT", None, QtGui.QApplication.UnicodeUTF8))
        self.textBoxBaselines.setText(QtGui.QApplication.translate("debugdock", "TEXT_BOX_BASELINES", None, QtGui.QApplication.UnicodeUTF8))
        self.propModelBounds.setText(QtGui.QApplication.translate("debugdock", "PROP_MODEL_BOUNDS", None, QtGui.QApplication.UnicodeUTF8))
        self.propWorldBounds.setText(QtGui.QApplication.translate("debugdock", "PROP_WORLD_BOUNDS", None, QtGui.QApplication.UnicodeUTF8))
        self.allocLog.setText(QtGui.QApplication.translate("debugdock", "Lua Alloc Log Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.histogram.setText(QtGui.QApplication.translate("debugdock", "Histogram Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.runStringBtn.setText(QtGui.QApplication.translate("debugdock", "Run String on Device", None, QtGui.QApplication.UnicodeUTF8))

