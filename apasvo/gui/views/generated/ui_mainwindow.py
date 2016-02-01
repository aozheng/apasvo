# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Thu Aug 15 22:30:31 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

'''
@author:     Jose Emilio Romero Lopez

@copyright:  Copyright 2013-2014, Jose Emilio Romero Lopez.

@license:    GPL

@contact:    jemromerol@gmail.com

  This file is part of APASVO.

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from PySide import QtCore, QtGui
from apasvo.gui.views.generated import qrc_icons


DEFAULT_UNDO_LIMIT = 10


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setVisible(False)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayout.addWidget(self.splitter)
        self.EventsTableView = QtGui.QTableView(self.splitter)
        self.EventsTableView.setObjectName("EventsTableView")
        self.EventsTableView.horizontalHeader().setMovable(True)
        self.EventsTableView.setSortingEnabled(True)
        self.EventsTableView.horizontalHeader().setStretchLastSection(True)
        self.EventsTableView.resizeColumnsToContents()
        self.EventsTableView.verticalHeader().setVisible(True)
        self.EventsTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.EventsTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_Recent = QtGui.QMenu(self.menuFile)
        self.menuOpen_Recent.setIcon(QtGui.QIcon(":/open-recent.png"))
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QtGui.QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuSignal_Inspector = QtGui.QMenu(self.menuView)
        self.menuSignal_Inspector.setObjectName("menuSignal_Inspector")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAnalysis = QtGui.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.toolBarMain = QtGui.QToolBar(MainWindow)
        self.toolBarMain.setObjectName("toolBarMain")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarMain)
        self.toolBarAnalysis = QtGui.QToolBar(MainWindow)
        self.toolBarAnalysis.setMovable(True)
        self.toolBarAnalysis.setFloatable(True)
        self.toolBarAnalysis.setObjectName("toolBarAnalysis")
        self.toolBarAnalysis.setEnabled(False)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setIcon(QtGui.QIcon(":/open.png"))
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setIcon(QtGui.QIcon(":/settings.png"))
        self.actionSettings.setIconVisibleInMenu(True)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(QtGui.QIcon(":/about.png"))
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOnlineHelp = QtGui.QAction(MainWindow)
        self.actionOnlineHelp.setIcon(QtGui.QIcon(":/online-help.png"))
        self.actionOnlineHelp.setIconVisibleInMenu(True)
        self.actionEvent_List = QtGui.QAction(MainWindow)
        self.actionEvent_List.setCheckable(True)
        self.actionEvent_List.setChecked(True)
        self.actionEvent_List.setObjectName("actionEvent_List")
        self.actionSTA_LTA = QtGui.QAction(MainWindow)
        self.actionSTA_LTA.setIcon(QtGui.QIcon(":/stalta.png"))
        self.actionSTA_LTA.setEnabled(False)
        self.actionSTA_LTA.setObjectName("actionSTA_LTA")
        self.actionAMPA = QtGui.QAction(MainWindow)
        self.actionAMPA.setIcon(QtGui.QIcon(":/ampa.png"))
        self.actionAMPA.setEnabled(False)
        self.actionAMPA.setObjectName("actionAMPA")
        # create undo and redo actions
        self.command_stack = QtGui.QUndoStack(self)
        self.command_stack.setUndoLimit(DEFAULT_UNDO_LIMIT)
        self.actionUndo = self.command_stack.createUndoAction(self)
        self.actionRedo = self.command_stack.createRedoAction(self)
        self.actionUndo.setIcon(QtGui.QIcon(":/undo.png"))
        self.actionUndo.setIconVisibleInMenu(True)
        self.actionRedo.setIcon(QtGui.QIcon(":/redo.png"))
        self.actionRedo.setIconVisibleInMenu(True)
        self.actionSaveEvents = QtGui.QAction(MainWindow)
        self.actionSaveEvents.setEnabled(False)
        self.actionSaveEvents.setIcon(QtGui.QIcon(":/save.png"))
        self.actionSaveEvents.setIconVisibleInMenu(True)
        self.actionSaveEvents_As = QtGui.QAction(MainWindow)
        self.actionSaveEvents_As.setEnabled(False)
        self.actionSaveEvents_As.setIcon(QtGui.QIcon(":/save-as.png"))
        self.actionSaveEvents_As.setIconVisibleInMenu(True)
        self.actionSaveCF = QtGui.QAction(MainWindow)
        self.actionSaveCF.setEnabled(False)
        self.actionSaveCF.setIcon(QtGui.QIcon(":/save.png"))
        self.actionSaveCF.setIconVisibleInMenu(True)
        self.actionSaveCF.setObjectName("actionSaveCF")
        self.actionSaveCF_As = QtGui.QAction(MainWindow)
        self.actionSaveCF_As.setEnabled(False)
        self.actionSaveCF_As.setIcon(QtGui.QIcon(":/save-as.png"))
        self.actionSaveCF_As.setIconVisibleInMenu(True)
        self.actionSaveCF_As.setObjectName("actionSaveCF_As")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setIcon(QtGui.QIcon(":/exit.png"))
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMedia_Toolbar = QtGui.QAction(MainWindow)
        self.actionMedia_Toolbar.setCheckable(True)
        self.actionMedia_Toolbar.setChecked(True)
        self.actionMedia_Toolbar.setObjectName("actionMedia_Toolbar")
        self.actionNavigation_Toolbar = QtGui.QAction(MainWindow)
        self.actionNavigation_Toolbar.setCheckable(True)
        self.actionNavigation_Toolbar.setChecked(True)
        self.actionNavigation_Toolbar.setObjectName("actionNavigation_Toolbar")
        self.actionClearRecent = QtGui.QAction(MainWindow)
        self.actionClearRecent.setEnabled(False)
        self.actionClearRecent.setIcon(QtGui.QIcon(":/clear-list.png"))
        self.actionClearRecent.setIconVisibleInMenu(True)
        self.actionClearRecent.setObjectName("actionClearRecent")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setEnabled(False)
        self.actionClose.setIcon(QtGui.QIcon(":/close.png"))
        self.actionClose.setIconVisibleInMenu(True)
        self.actionClose.setObjectName("actionClose")
        self.actionTakanami = QtGui.QAction(MainWindow)
        self.actionTakanami.setIcon(QtGui.QIcon(":/takanami.png"))
        self.actionTakanami.setEnabled(False)
        self.actionTakanami.setObjectName("actionTakanami")
        #######################################################################
        self.actionFilterDesing = QtGui.QAction(MainWindow)
        self.actionFilterDesing.setIcon(QtGui.QIcon(":/takanami.png"))
        self.actionFilterDesing.setEnabled(False)
        self.actionFilterDesing.setObjectName("actionFilterDesing")
        self.viewFilteredCheckBox = QtGui.QCheckBox("View filtered signal")
        self.viewFilteredCheckBox.setChecked(True)
        ########################################################################
        self.actionSignal_Amplitude = QtGui.QAction(MainWindow)
        self.actionSignal_Amplitude.setCheckable(True)
        self.actionSignal_Amplitude.setChecked(True)
        self.actionSignal_Amplitude.setObjectName("actionSignal_Amplitude")
        self.actionSignal_Envelope = QtGui.QAction(MainWindow)
        self.actionSignal_Envelope.setCheckable(True)
        self.actionSignal_Envelope.setChecked(True)
        self.actionSignal_Envelope.setObjectName("actionSignal_Envelope")
        self.actionCharacteristic_Function = QtGui.QAction(MainWindow)
        self.actionCharacteristic_Function.setCheckable(True)
        self.actionCharacteristic_Function.setChecked(False)
        self.actionCharacteristic_Function.setEnabled(False)
        self.actionCharacteristic_Function.setObjectName("actionCharacteristic_Function")
        self.actionEspectrogram = QtGui.QAction(MainWindow)
        self.actionEspectrogram.setCheckable(True)
        self.actionEspectrogram.setChecked(True)
        self.actionEspectrogram.setObjectName("actionEspectrogram")
        self.actionMain_Toolbar = QtGui.QAction(MainWindow)
        self.actionMain_Toolbar.setCheckable(True)
        self.actionMain_Toolbar.setChecked(True)
        self.actionMain_Toolbar.setObjectName("actionMain_Toolbar")
        self.actionAnalysis_Toolbar = QtGui.QAction(MainWindow)
        self.actionAnalysis_Toolbar.setCheckable(True)
        self.actionAnalysis_Toolbar.setChecked(True)
        self.actionAnalysis_Toolbar.setObjectName("actionAnalysis_Toolbar")
        self.actionSignal_MiniMap = QtGui.QAction(MainWindow)
        self.actionSignal_MiniMap.setCheckable(True)
        self.actionSignal_MiniMap.setChecked(True)
        self.actionSignal_MiniMap.setObjectName("actionSignal_MiniMap")
        self.action_show_trace_selector = QtGui.QAction(MainWindow)
        self.action_show_trace_selector.setCheckable(True)
        self.action_show_trace_selector.setChecked(False)
        self.action_show_trace_selector.setEnabled(False)
        self.action_show_trace_selector.setObjectName("action_show_trace_selector")
        self.actionDelete_Selected = QtGui.QAction(MainWindow)
        self.actionDelete_Selected.setEnabled(False)
        self.actionDelete_Selected.setObjectName("actionDelete_Selected")
        self.actionClear_Event_List = QtGui.QAction(MainWindow)
        self.actionClear_Event_List.setEnabled(False)
        self.actionClear_Event_List.setObjectName("actionClear_Event_List")
        self.menuFile.addAction(self.actionOpen)
        self.menuOpen_Recent.menuAction().setIconVisibleInMenu(True)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveEvents)
        self.menuFile.addAction(self.actionSaveEvents_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveCF)
        self.menuFile.addAction(self.actionSaveCF_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete_Selected)
        self.menuEdit.addAction(self.actionClear_Event_List)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSettings)
        self.menuToolbars.addAction(self.actionMain_Toolbar)
        self.menuToolbars.addAction(self.actionAnalysis_Toolbar)
        self.menuToolbars.addAction(self.actionNavigation_Toolbar)
        self.menuToolbars.addAction(self.actionMedia_Toolbar)
        self.menuSignal_Inspector.addAction(self.actionSignal_Amplitude)
        self.menuSignal_Inspector.addAction(self.actionSignal_Envelope)
        self.menuSignal_Inspector.addAction(self.actionCharacteristic_Function)
        self.menuSignal_Inspector.addAction(self.actionEspectrogram)
        self.menuView.addAction(self.actionEvent_List)
        self.menuView.addAction(self.actionSignal_MiniMap)
        self.menuView.addAction(self.action_show_trace_selector)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuSignal_Inspector.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionOnlineHelp)
        self.menuAnalysis.addAction(self.actionSTA_LTA)
        self.menuAnalysis.addAction(self.actionAMPA)
        self.menuAnalysis.addAction(self.actionTakanami)
        ####################################################################
        self.menuAnalysis.addAction(self.actionFilterDesing)
        ####################################################################
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBarMain.addAction(self.actionOpen)
        self.toolBarMain.addAction(self.actionClose)
        self.toolBarMain.addSeparator()
        self.toolBarMain.addAction(self.actionUndo)
        self.toolBarMain.addAction(self.actionRedo)
        self.toolBarMain.addSeparator()
        self.toolBarMain.addAction(self.actionSettings)
        self.toolBarAnalysis.addAction(self.actionSTA_LTA)
        self.toolBarAnalysis.addAction(self.actionAMPA)
        self.toolBarAnalysis.addSeparator()
        self.actionActivateThreshold = QtGui.QAction(MainWindow)
        self.actionActivateThreshold.setIcon(QtGui.QIcon(":/threshold.png"))
        self.actionActivateThreshold.setCheckable(True)
        self.actionActivateThreshold.setChecked(False)
        self.actionActivateThreshold.setObjectName("actionActivateThreshold")
        self.actionActivateThreshold.setToolTip("Enable/Disable Threshold")
        self.toolBarAnalysis.addAction(self.actionActivateThreshold)
        self.thresholdLabel = QtGui.QLabel(" Threshold value: ", parent=self.toolBarAnalysis)
        self.thresholdLabel.setEnabled(False)
        self.toolBarAnalysis.addWidget(self.thresholdLabel)
        self.thresholdSpinBox = QtGui.QDoubleSpinBox(self.toolBarAnalysis)
        self.thresholdSpinBox.setMinimum(0.0)
        self.thresholdSpinBox.setMaximum(20.0)
        self.thresholdSpinBox.setSingleStep(0.01)
        self.thresholdSpinBox.setValue(1.0)
        self.thresholdSpinBox.setAccelerated(True)
        self.thresholdSpinBox.setEnabled(False)
        self.toolBarAnalysis.addWidget(self.thresholdSpinBox)
        self.toolBarAnalysis.addSeparator()
        self.toolBarAnalysis.addAction(self.actionTakanami)
        ##############################################################
        self.toolBarAnalysis.addAction(self.actionFilterDesing)
        self.toolBarAnalysis.addWidget(self.viewFilteredCheckBox)
        #self.toolBarAnalysis.addAction(self.viewFilteredCheckBox)
        #############################################################
        # set up status bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.analysis_label = QtGui.QLabel("", self.statusbar)
        self.analysis_progress_bar = QtGui.QProgressBar(self.statusbar)
        self.analysis_progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.analysis_progress_bar.setRange(0, 0)
        self.analysis_progress_bar.hide()
        self.statusbar.addPermanentWidget(self.analysis_label)
        self.statusbar.addPermanentWidget(self.analysis_progress_bar)
        # apply translation
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpen_Recent.setTitle(QtGui.QApplication.translate("MainWindow", "Open &Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuToolbars.setTitle(QtGui.QApplication.translate("MainWindow", "&Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSignal_Inspector.setTitle(QtGui.QApplication.translate("MainWindow", "&Signal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAnalysis.setTitle(QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBarMain.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip("Open an existing file")
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "&Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setStatusTip("Settings")
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setStatusTip("Display application info")
        self.actionOnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOnlineHelp.setStatusTip("Visit APASVO wiki")
        self.actionEvent_List.setText(QtGui.QApplication.translate("MainWindow", "&Event List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSTA_LTA.setText(QtGui.QApplication.translate("MainWindow", "&STA-LTA...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSTA_LTA.setToolTip("Apply STA-LTA")
        self.actionSTA_LTA.setStatusTip("Apply STA-LTA algorithm to the entire trace")
        self.actionSTA_LTA.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAMPA.setText(QtGui.QApplication.translate("MainWindow", "&AMPA...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAMPA.setToolTip("Apply AMPA")
        self.actionAMPA.setStatusTip("Apply AMPA algorithm to the entire trace")
        self.actionAMPA.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "&Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "&Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveEvents.setText(QtGui.QApplication.translate("MainWindow", "Save &Event List...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveEvents.setStatusTip("Save event list")
        self.actionSaveEvents.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveEvents_As.setText(QtGui.QApplication.translate("MainWindow", "Save E&vent List As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveEvents_As.setStatusTip("Save event list to a new file")
        self.actionSaveEvents_As.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveCF.setText(QtGui.QApplication.translate("MainWindow", "Save &CF...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveCF.setStatusTip("Save characteristic function")
        self.actionSaveCF.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveCF_As.setText(QtGui.QApplication.translate("MainWindow", "Save C&F As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveCF_As.setStatusTip("Save characteristic function to a new file")
        self.actionSaveCF_As.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip("Close the application")
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMedia_Toolbar.setText(QtGui.QApplication.translate("MainWindow", "M&edia Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMedia_Toolbar.setStatusTip("Show/Hide Media Toolbar")
        self.actionNavigation_Toolbar.setText(QtGui.QApplication.translate("MainWindow", "&Navigation Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNavigation_Toolbar.setStatusTip("Show/Hide Navigation Toolbar")
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setStatusTip("Close the current trace")
        self.actionClearRecent.setText(QtGui.QApplication.translate("MainWindow", "&Clear List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearRecent.setStatusTip("Clear recent opened files list")
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTakanami.setText(QtGui.QApplication.translate("MainWindow", "&Takanami on selection...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTakanami.setToolTip("Apply Takanami")
        self.actionTakanami.setStatusTip("Apply Takanami algorithm to selection")
        self.actionTakanami.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        ########################################################################################################################
        self.actionFilterDesing.setText(QtGui.QApplication.translate("MainWindow", "&Filter Design", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterDesing.setToolTip("Apply filter algorithm")
        self.actionFilterDesing.setStatusTip("Apply filter algorithm")
        self.actionFilterDesing.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        ########################################################################################################################
        self.actionSignal_Amplitude.setText(QtGui.QApplication.translate("MainWindow", "Signal &Amplitude", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignal_Amplitude.setStatusTip("Show/Hide signal amplitude")
        self.actionSignal_Envelope.setText(QtGui.QApplication.translate("MainWindow", "Signal &Envelope", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignal_Envelope.setStatusTip("Show/Hide signal envelope")
        self.actionCharacteristic_Function.setText(QtGui.QApplication.translate("MainWindow", "&Characteristic Function", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCharacteristic_Function.setStatusTip("Show/Hide characteristic function")
        self.actionEspectrogram.setText(QtGui.QApplication.translate("MainWindow", "&Espectrogram", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEspectrogram.setStatusTip("Show/Hide spectrogram")
        self.actionMain_Toolbar.setText(QtGui.QApplication.translate("MainWindow", "&Main Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMain_Toolbar.setStatusTip("Show/Hide Main Toolbar")
        self.actionAnalysis_Toolbar.setText(QtGui.QApplication.translate("MainWindow", "&Analysis Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalysis_Toolbar.setStatusTip("Show/Hide Analysis Toolbar")
        self.actionSignal_MiniMap.setText(QtGui.QApplication.translate("MainWindow", "Signal &Minimap", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignal_MiniMap.setStatusTip("Show/Hide Signal Minimap")
        self.action_show_trace_selector.setText(QtGui.QApplication.translate("MainWindow", "&Trace Selector", None, QtGui.QApplication.UnicodeUTF8))
        self.action_show_trace_selector.setStatusTip("Show/Hide Trace Selector")
        self.actionDelete_Selected.setText(QtGui.QApplication.translate("MainWindow", "&Delete Selected Event(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Selected.setStatusTip("Delete selected events")
        self.actionClear_Event_List.setText(QtGui.QApplication.translate("MainWindow", "&Clear Event List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_Event_List.setStatusTip("Clear event list")

