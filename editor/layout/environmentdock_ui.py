# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'environmentdock.ui'
#
# Created: Wed Aug  5 14:50:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_environmentdock(object):
    def setupUi(self, environmentdock):
        environmentdock.setObjectName("environmentdock")
        environmentdock.resize(442, 921)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reloadGroup = QGroupBoxCollapsible(self.dockWidgetContents)
        self.reloadGroup.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.reloadGroup.setFlat(True)
        self.reloadGroup.setCheckable(True)
        self.reloadGroup.setObjectName("reloadGroup")
        self.gridLayout_5 = QtGui.QGridLayout(self.reloadGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.localAutoreload = QtGui.QCheckBox(self.reloadGroup)
        self.localAutoreload.setFocusPolicy(QtCore.Qt.TabFocus)
        self.localAutoreload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.localAutoreload.setObjectName("localAutoreload")
        self.gridLayout_5.addWidget(self.localAutoreload, 1, 1, 1, 1)
        self.deviceAutoreload = QtGui.QCheckBox(self.reloadGroup)
        self.deviceAutoreload.setFocusPolicy(QtCore.Qt.TabFocus)
        self.deviceAutoreload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deviceAutoreload.setObjectName("deviceAutoreload")
        self.gridLayout_5.addWidget(self.deviceAutoreload, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.reloadGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.reloadGroup)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.clearOverridesBtn = QtGui.QPushButton(self.reloadGroup)
        self.clearOverridesBtn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.clearOverridesBtn.setObjectName("clearOverridesBtn")
        self.gridLayout_5.addWidget(self.clearOverridesBtn, 6, 1, 1, 1)
        self.reloadNowBtn = QtGui.QPushButton(self.reloadGroup)
        self.reloadNowBtn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.reloadNowBtn.setObjectName("reloadNowBtn")
        self.gridLayout_5.addWidget(self.reloadNowBtn, 4, 1, 1, 1)
        self.updateDevicesBtn = QtGui.QToolButton(self.reloadGroup)
        self.updateDevicesBtn.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.updateDevicesBtn.setIcon(icon)
        self.updateDevicesBtn.setIconSize(QtCore.QSize(16, 16))
        self.updateDevicesBtn.setAutoRaise(False)
        self.updateDevicesBtn.setObjectName("updateDevicesBtn")
        self.gridLayout_5.addWidget(self.updateDevicesBtn, 0, 2, 1, 1)
        self.availableDevicesList = QtGui.QComboBox(self.reloadGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableDevicesList.sizePolicy().hasHeightForWidth())
        self.availableDevicesList.setSizePolicy(sizePolicy)
        self.availableDevicesList.setObjectName("availableDevicesList")
        self.gridLayout_5.addWidget(self.availableDevicesList, 0, 1, 1, 1)
        self.fullAutoreload = QtGui.QCheckBox(self.reloadGroup)
        self.fullAutoreload.setObjectName("fullAutoreload")
        self.gridLayout_5.addWidget(self.fullAutoreload, 3, 1, 1, 1)
        self.reloadNowRemoteBtn = QtGui.QPushButton(self.reloadGroup)
        self.reloadNowRemoteBtn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.reloadNowRemoteBtn.setObjectName("reloadNowRemoteBtn")
        self.gridLayout_5.addWidget(self.reloadNowRemoteBtn, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.reloadGroup)
        self.environmentGroup = QGroupBoxCollapsible(self.dockWidgetContents)
        self.environmentGroup.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.environmentGroup.setFlat(True)
        self.environmentGroup.setCheckable(True)
        self.environmentGroup.setChecked(True)
        self.environmentGroup.setObjectName("environmentGroup")
        self.gridLayout_4 = QtGui.QGridLayout(self.environmentGroup)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.heightEdit = QtGui.QLineEdit(self.environmentGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightEdit.sizePolicy().hasHeightForWidth())
        self.heightEdit.setSizePolicy(sizePolicy)
        self.heightEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.heightEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.heightEdit.setObjectName("heightEdit")
        self.gridLayout_4.addWidget(self.heightEdit, 1, 1, 1, 1)
        self.widthEdit = QtGui.QLineEdit(self.environmentGroup)
        self.widthEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widthEdit.setObjectName("widthEdit")
        self.gridLayout_4.addWidget(self.widthEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.environmentGroup)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.environmentGroup)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)
        self.languageBox = QtGui.QComboBox(self.environmentGroup)
        self.languageBox.setObjectName("languageBox")
        self.gridLayout_4.addWidget(self.languageBox, 4, 1, 1, 1)
        self.documentsBtn = QtGui.QPushButton(self.environmentGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.documentsBtn.sizePolicy().hasHeightForWidth())
        self.documentsBtn.setSizePolicy(sizePolicy)
        self.documentsBtn.setMaximumSize(QtCore.QSize(16777215, 26))
        self.documentsBtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.documentsBtn.setAutoRepeat(False)
        self.documentsBtn.setDefault(False)
        self.documentsBtn.setFlat(True)
        self.documentsBtn.setObjectName("documentsBtn")
        self.gridLayout_4.addWidget(self.documentsBtn, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.environmentGroup)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.environmentGroup)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.environmentGroup)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.dpiEdit = QtGui.QLineEdit(self.environmentGroup)
        self.dpiEdit.setObjectName("dpiEdit")
        self.gridLayout_4.addWidget(self.dpiEdit, 2, 1, 1, 1)
        self.countryBox = QtGui.QComboBox(self.environmentGroup)
        self.countryBox.setObjectName("countryBox")
        self.gridLayout_4.addWidget(self.countryBox, 5, 1, 1, 1)
        self.deviceBox = QtGui.QComboBox(self.environmentGroup)
        self.deviceBox.setObjectName("deviceBox")
        self.gridLayout_4.addWidget(self.deviceBox, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.environmentGroup)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.environmentGroup)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.environmentGroup)
        self.notificationsGroup = QGroupBoxCollapsible(self.dockWidgetContents)
        self.notificationsGroup.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.notificationsGroup.setFlat(True)
        self.notificationsGroup.setCheckable(True)
        self.notificationsGroup.setChecked(True)
        self.notificationsGroup.setObjectName("notificationsGroup")
        self.gridLayout_2 = QtGui.QGridLayout(self.notificationsGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtGui.QLabel(self.notificationsGroup)
        self.label_11.setMinimumSize(QtCore.QSize(90, 0))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.pushUserInfo = QtGui.QPlainTextEdit(self.notificationsGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushUserInfo.sizePolicy().hasHeightForWidth())
        self.pushUserInfo.setSizePolicy(sizePolicy)
        self.pushUserInfo.setMaximumSize(QtCore.QSize(16777215, 130))
        self.pushUserInfo.setObjectName("pushUserInfo")
        self.gridLayout_2.addWidget(self.pushUserInfo, 1, 1, 1, 1)
        self.pushSend = QtGui.QPushButton(self.notificationsGroup)
        self.pushSend.setObjectName("pushSend")
        self.gridLayout_2.addWidget(self.pushSend, 2, 1, 1, 1)
        self.pushLocal = QtGui.QCheckBox(self.notificationsGroup)
        self.pushLocal.setObjectName("pushLocal")
        self.gridLayout_2.addWidget(self.pushLocal, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.notificationsGroup)
        self.seesionGroup = QGroupBoxCollapsible(self.dockWidgetContents)
        self.seesionGroup.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.seesionGroup.setFlat(True)
        self.seesionGroup.setCheckable(True)
        self.seesionGroup.setObjectName("seesionGroup")
        self.gridLayout_3 = QtGui.QGridLayout(self.seesionGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.urlEdit = QtGui.QLineEdit(self.seesionGroup)
        self.urlEdit.setObjectName("urlEdit")
        self.gridLayout_3.addWidget(self.urlEdit, 3, 1, 1, 1)
        self.urlBtn = QtGui.QPushButton(self.seesionGroup)
        self.urlBtn.setObjectName("urlBtn")
        self.gridLayout_3.addWidget(self.urlBtn, 3, 0, 1, 1)
        self.sessionEndBtn = QtGui.QPushButton(self.seesionGroup)
        self.sessionEndBtn.setObjectName("sessionEndBtn")
        self.gridLayout_3.addWidget(self.sessionEndBtn, 1, 0, 1, 1)
        self.sessionStartBtn = QtGui.QPushButton(self.seesionGroup)
        self.sessionStartBtn.setObjectName("sessionStartBtn")
        self.gridLayout_3.addWidget(self.sessionStartBtn, 0, 0, 1, 1)
        self.sessionResume = QtGui.QCheckBox(self.seesionGroup)
        self.sessionResume.setObjectName("sessionResume")
        self.gridLayout_3.addWidget(self.sessionResume, 0, 1, 1, 1)
        self.backBtn = QtGui.QPushButton(self.seesionGroup)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout_3.addWidget(self.backBtn, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.seesionGroup)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        environmentdock.setWidget(self.dockWidgetContents)

        self.retranslateUi(environmentdock)
        QtCore.QObject.connect(self.reloadNowBtn, QtCore.SIGNAL("clicked()"), environmentdock.reloadMoai)
        QtCore.QObject.connect(self.localAutoreload, QtCore.SIGNAL("toggled(bool)"), environmentdock.setAutoreloadHost)
        QtCore.QObject.connect(self.fullAutoreload, QtCore.SIGNAL("toggled(bool)"), environmentdock.setAutoreloadFull)
        QtCore.QObject.connect(self.deviceAutoreload, QtCore.SIGNAL("toggled(bool)"), environmentdock.setAutoreloadDevice)
        QtCore.QObject.connect(self.availableDevicesList, QtCore.SIGNAL("currentIndexChanged(int)"), environmentdock.setCurrentDevice)
        QtCore.QObject.connect(self.updateDevicesBtn, QtCore.SIGNAL("clicked()"), environmentdock.updateDeviceList)
        QtCore.QObject.connect(self.dpiEdit, QtCore.SIGNAL("textChanged(QString)"), environmentdock.setScreenDpi)
        QtCore.QObject.connect(self.countryBox, QtCore.SIGNAL("currentIndexChanged(int)"), environmentdock.setCountryCode)
        QtCore.QObject.connect(self.languageBox, QtCore.SIGNAL("currentIndexChanged(int)"), environmentdock.setLanguageCode)
        QtCore.QObject.connect(self.documentsBtn, QtCore.SIGNAL("clicked()"), environmentdock.browseDocuments)
        QtCore.QObject.connect(self.sessionStartBtn, QtCore.SIGNAL("clicked()"), environmentdock.onStartSession)
        QtCore.QObject.connect(self.sessionEndBtn, QtCore.SIGNAL("clicked()"), environmentdock.onEndSession)
        QtCore.QObject.connect(self.urlBtn, QtCore.SIGNAL("clicked()"), environmentdock.onOpenedFromUrl)
        QtCore.QObject.connect(self.pushSend, QtCore.SIGNAL("clicked()"), environmentdock.sendNotification)
        QtCore.QObject.connect(self.clearOverridesBtn, QtCore.SIGNAL("clicked()"), environmentdock.clearRemoteOverrides)
        QtCore.QObject.connect(self.deviceBox, QtCore.SIGNAL("currentIndexChanged(int)"), environmentdock.setDeviceType)
        QtCore.QObject.connect(self.backBtn, QtCore.SIGNAL("clicked()"), environmentdock.onBackButton)
        QtCore.QObject.connect(self.reloadNowRemoteBtn, QtCore.SIGNAL("clicked()"), environmentdock.reloadRemote)
        QtCore.QMetaObject.connectSlotsByName(environmentdock)
        environmentdock.setTabOrder(self.reloadGroup, self.availableDevicesList)
        environmentdock.setTabOrder(self.availableDevicesList, self.updateDevicesBtn)
        environmentdock.setTabOrder(self.updateDevicesBtn, self.localAutoreload)
        environmentdock.setTabOrder(self.localAutoreload, self.deviceAutoreload)
        environmentdock.setTabOrder(self.deviceAutoreload, self.fullAutoreload)
        environmentdock.setTabOrder(self.fullAutoreload, self.reloadNowBtn)
        environmentdock.setTabOrder(self.reloadNowBtn, self.environmentGroup)
        environmentdock.setTabOrder(self.environmentGroup, self.widthEdit)
        environmentdock.setTabOrder(self.widthEdit, self.heightEdit)
        environmentdock.setTabOrder(self.heightEdit, self.dpiEdit)
        environmentdock.setTabOrder(self.dpiEdit, self.documentsBtn)
        environmentdock.setTabOrder(self.documentsBtn, self.languageBox)
        environmentdock.setTabOrder(self.languageBox, self.countryBox)
        environmentdock.setTabOrder(self.countryBox, self.notificationsGroup)
        environmentdock.setTabOrder(self.notificationsGroup, self.pushUserInfo)
        environmentdock.setTabOrder(self.pushUserInfo, self.pushLocal)
        environmentdock.setTabOrder(self.pushLocal, self.pushSend)
        environmentdock.setTabOrder(self.pushSend, self.seesionGroup)
        environmentdock.setTabOrder(self.seesionGroup, self.sessionStartBtn)
        environmentdock.setTabOrder(self.sessionStartBtn, self.sessionResume)
        environmentdock.setTabOrder(self.sessionResume, self.sessionEndBtn)
        environmentdock.setTabOrder(self.sessionEndBtn, self.urlBtn)
        environmentdock.setTabOrder(self.urlBtn, self.urlEdit)

    def retranslateUi(self, environmentdock):
        environmentdock.setWindowTitle(QtGui.QApplication.translate("environmentdock", "Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadGroup.setTitle(QtGui.QApplication.translate("environmentdock", "Live Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.localAutoreload.setText(QtGui.QApplication.translate("environmentdock", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceAutoreload.setText(QtGui.QApplication.translate("environmentdock", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("environmentdock", "Remote Device", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("environmentdock", "Auro Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOverridesBtn.setText(QtGui.QApplication.translate("environmentdock", "Clear Overrides", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadNowBtn.setText(QtGui.QApplication.translate("environmentdock", "Reload now", None, QtGui.QApplication.UnicodeUTF8))
        self.updateDevicesBtn.setText(QtGui.QApplication.translate("environmentdock", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.fullAutoreload.setText(QtGui.QApplication.translate("environmentdock", "Full reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadNowRemoteBtn.setText(QtGui.QApplication.translate("environmentdock", "Reload Remote", None, QtGui.QApplication.UnicodeUTF8))
        self.environmentGroup.setTitle(QtGui.QApplication.translate("environmentdock", "MOAIEnvironment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("environmentdock", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("environmentdock", "Language Code", None, QtGui.QApplication.UnicodeUTF8))
        self.documentsBtn.setText(QtGui.QApplication.translate("environmentdock", "docs/", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("environmentdock", "DeviceType", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("environmentdock", "Documents", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("environmentdock", "DPI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("environmentdock", "Country Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("environmentdock", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.notificationsGroup.setTitle(QtGui.QApplication.translate("environmentdock", "Notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("environmentdock", "UserInfo \n"
"(Lua table)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSend.setText(QtGui.QApplication.translate("environmentdock", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.pushLocal.setText(QtGui.QApplication.translate("environmentdock", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.seesionGroup.setTitle(QtGui.QApplication.translate("environmentdock", "Session", None, QtGui.QApplication.UnicodeUTF8))
        self.urlBtn.setText(QtGui.QApplication.translate("environmentdock", "Open Url", None, QtGui.QApplication.UnicodeUTF8))
        self.sessionEndBtn.setText(QtGui.QApplication.translate("environmentdock", "End Session", None, QtGui.QApplication.UnicodeUTF8))
        self.sessionStartBtn.setText(QtGui.QApplication.translate("environmentdock", "Start Session", None, QtGui.QApplication.UnicodeUTF8))
        self.sessionResume.setText(QtGui.QApplication.translate("environmentdock", "resume", None, QtGui.QApplication.UnicodeUTF8))
        self.backBtn.setText(QtGui.QApplication.translate("environmentdock", "Back (Android)", None, QtGui.QApplication.UnicodeUTF8))

from widgets.qgroupboxcollapsible import QGroupBoxCollapsible
import resources_rc
