# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tauMidi_Mainwindow.ui'
#
# Created: Tue Jul 15 18:41:04 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tauMidiGenerator_Mainwindow(object):
    def setupUi(self, tauMidiGenerator_Mainwindow):
        tauMidiGenerator_Mainwindow.setObjectName("tauMidiGenerator_Mainwindow")
        tauMidiGenerator_Mainwindow.resize(580, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tauMidiGenerator_Mainwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(tauMidiGenerator_Mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filename_grouBoc = QtWidgets.QGroupBox(self.centralwidget)
        self.filename_grouBoc.setGeometry(QtCore.QRect(10, 10, 261, 71))
        self.filename_grouBoc.setObjectName("filename_grouBoc")
        self.BrowseFileName_button = QtWidgets.QPushButton(self.filename_grouBoc)
        self.BrowseFileName_button.setGeometry(QtCore.QRect(190, 10, 61, 51))
        self.BrowseFileName_button.setObjectName("BrowseFileName_button")
        self.fileName_textfield = QtWidgets.QLineEdit(self.filename_grouBoc)
        self.fileName_textfield.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.fileName_textfield.setText("")
        self.fileName_textfield.setCursorPosition(0)
        self.fileName_textfield.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fileName_textfield.setClearButtonEnabled(True)
        self.fileName_textfield.setObjectName("fileName_textfield")
        self.TrackList_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.TrackList_groupbox.setGeometry(QtCore.QRect(10, 90, 261, 181))
        self.TrackList_groupbox.setObjectName("TrackList_groupbox")
        self.tracList_list = QtWidgets.QListWidget(self.TrackList_groupbox)
        self.tracList_list.setGeometry(QtCore.QRect(10, 20, 151, 141))
        self.tracList_list.setObjectName("tracList_list")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tracList_list.addItem(item)
        self.addTrack_button = QtWidgets.QPushButton(self.TrackList_groupbox)
        self.addTrack_button.setGeometry(QtCore.QRect(170, 20, 75, 51))
        self.addTrack_button.setObjectName("addTrack_button")
        self.deleteTrack_button = QtWidgets.QPushButton(self.TrackList_groupbox)
        self.deleteTrack_button.setGeometry(QtCore.QRect(170, 80, 75, 51))
        self.deleteTrack_button.setObjectName("deleteTrack_button")
        self.trackAtributes_goupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.trackAtributes_goupbox.setGeometry(QtCore.QRect(280, 10, 261, 131))
        self.trackAtributes_goupbox.setObjectName("trackAtributes_goupbox")
        self.track_init_spinbox = QtWidgets.QSpinBox(self.trackAtributes_goupbox)
        self.track_init_spinbox.setGeometry(QtCore.QRect(70, 20, 51, 22))
        self.track_init_spinbox.setMaximum(10000)
        self.track_init_spinbox.setSingleStep(10)
        self.track_init_spinbox.setObjectName("track_init_spinbox")
        self.initvalue_label = QtWidgets.QLabel(self.trackAtributes_goupbox)
        self.initvalue_label.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.initvalue_label.setObjectName("initvalue_label")
        self.loosp_label = QtWidgets.QLabel(self.trackAtributes_goupbox)
        self.loosp_label.setGeometry(QtCore.QRect(140, 20, 51, 20))
        self.loosp_label.setObjectName("loosp_label")
        self.track_loops_spinbox = QtWidgets.QSpinBox(self.trackAtributes_goupbox)
        self.track_loops_spinbox.setGeometry(QtCore.QRect(180, 20, 61, 22))
        self.track_loops_spinbox.setMaximum(10000)
        self.track_loops_spinbox.setSingleStep(10)
        self.track_loops_spinbox.setObjectName("track_loops_spinbox")
        self.chanel_label = QtWidgets.QLabel(self.trackAtributes_goupbox)
        self.chanel_label.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.chanel_label.setObjectName("chanel_label")
        self.track_channel_spinbox = QtWidgets.QSpinBox(self.trackAtributes_goupbox)
        self.track_channel_spinbox.setGeometry(QtCore.QRect(70, 50, 51, 22))
        self.track_channel_spinbox.setMaximum(255)
        self.track_channel_spinbox.setSingleStep(1)
        self.track_channel_spinbox.setObjectName("track_channel_spinbox")
        self.track_clamp_label = QtWidgets.QLabel(self.trackAtributes_goupbox)
        self.track_clamp_label.setGeometry(QtCore.QRect(140, 50, 51, 16))
        self.track_clamp_label.setObjectName("track_clamp_label")
        self.track_clamp_spinbox = QtWidgets.QSpinBox(self.trackAtributes_goupbox)
        self.track_clamp_spinbox.setGeometry(QtCore.QRect(180, 50, 61, 22))
        self.track_clamp_spinbox.setMaximum(255)
        self.track_clamp_spinbox.setSingleStep(10)
        self.track_clamp_spinbox.setProperty("value", 255)
        self.track_clamp_spinbox.setObjectName("track_clamp_spinbox")
        self.randomSeed_label = QtWidgets.QLabel(self.trackAtributes_goupbox)
        self.randomSeed_label.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.randomSeed_label.setObjectName("randomSeed_label")
        self.randomSeed_spinbox = QtWidgets.QSpinBox(self.trackAtributes_goupbox)
        self.randomSeed_spinbox.setGeometry(QtCore.QRect(130, 90, 71, 22))
        self.randomSeed_spinbox.setMaximum(10000)
        self.randomSeed_spinbox.setSingleStep(1)
        self.randomSeed_spinbox.setObjectName("randomSeed_spinbox")
        self.notesAtributes_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.notesAtributes_groupbox.setGeometry(QtCore.QRect(280, 150, 291, 141))
        self.notesAtributes_groupbox.setObjectName("notesAtributes_groupbox")
        self.pitch_textfield = QtWidgets.QLineEdit(self.notesAtributes_groupbox)
        self.pitch_textfield.setGeometry(QtCore.QRect(60, 20, 221, 20))
        self.pitch_textfield.setClearButtonEnabled(True)
        self.pitch_textfield.setObjectName("pitch_textfield")
        self.track_pitch_label = QtWidgets.QLabel(self.notesAtributes_groupbox)
        self.track_pitch_label.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.track_pitch_label.setObjectName("track_pitch_label")
        self.track_time_label = QtWidgets.QLabel(self.notesAtributes_groupbox)
        self.track_time_label.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.track_time_label.setObjectName("track_time_label")
        self.time_textfield = QtWidgets.QLineEdit(self.notesAtributes_groupbox)
        self.time_textfield.setGeometry(QtCore.QRect(60, 50, 221, 20))
        self.time_textfield.setClearButtonEnabled(True)
        self.time_textfield.setObjectName("time_textfield")
        self.track_duration_label = QtWidgets.QLabel(self.notesAtributes_groupbox)
        self.track_duration_label.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.track_duration_label.setObjectName("track_duration_label")
        self.duration_textfield = QtWidgets.QLineEdit(self.notesAtributes_groupbox)
        self.duration_textfield.setGeometry(QtCore.QRect(70, 80, 211, 20))
        self.duration_textfield.setClearButtonEnabled(True)
        self.duration_textfield.setObjectName("duration_textfield")
        self.track_volume_label = QtWidgets.QLabel(self.notesAtributes_groupbox)
        self.track_volume_label.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.track_volume_label.setObjectName("track_volume_label")
        self.volume_textfield = QtWidgets.QLineEdit(self.notesAtributes_groupbox)
        self.volume_textfield.setGeometry(QtCore.QRect(70, 110, 211, 20))
        self.volume_textfield.setClearButtonEnabled(True)
        self.volume_textfield.setObjectName("volume_textfield")
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(430, 310, 131, 51))
        self.generate_button.setObjectName("generate_button")
        self.options_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.options_groupbox.setGeometry(QtCore.QRect(10, 280, 211, 91))
        self.options_groupbox.setObjectName("options_groupbox")
        self.autoRunMidi_check = QtWidgets.QCheckBox(self.options_groupbox)
        self.autoRunMidi_check.setGeometry(QtCore.QRect(10, 20, 111, 17))
        self.autoRunMidi_check.setChecked(True)
        self.autoRunMidi_check.setObjectName("autoRunMidi_check")
        self.openContainerFolder_check = QtWidgets.QCheckBox(self.options_groupbox)
        self.openContainerFolder_check.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.openContainerFolder_check.setChecked(False)
        self.openContainerFolder_check.setObjectName("openContainerFolder_check")
        self.autoSave_check = QtWidgets.QCheckBox(self.options_groupbox)
        self.autoSave_check.setGeometry(QtCore.QRect(10, 60, 141, 17))
        self.autoSave_check.setChecked(True)
        self.autoSave_check.setObjectName("autoSave_check")
        tauMidiGenerator_Mainwindow.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(tauMidiGenerator_Mainwindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menu.setDefaultUp(False)
        self.menu.setNativeMenuBar(False)
        self.menu.setObjectName("menu")
        self.menuMidi = QtWidgets.QMenu(self.menu)
        self.menuMidi.setTearOffEnabled(True)
        self.menuMidi.setObjectName("menuMidi")
        self.menuHelp = QtWidgets.QMenu(self.menu)
        self.menuHelp.setObjectName("menuHelp")
        tauMidiGenerator_Mainwindow.setMenuBar(self.menu)
        self.statusbar = QtWidgets.QStatusBar(tauMidiGenerator_Mainwindow)
        self.statusbar.setObjectName("statusbar")
        tauMidiGenerator_Mainwindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(tauMidiGenerator_Mainwindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(tauMidiGenerator_Mainwindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(tauMidiGenerator_Mainwindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClear = QtWidgets.QAction(tauMidiGenerator_Mainwindow)
        self.actionClear.setObjectName("actionClear")
        self.actionAbout = QtWidgets.QAction(tauMidiGenerator_Mainwindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGenerate = QtWidgets.QAction(tauMidiGenerator_Mainwindow)
        self.actionGenerate.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionGenerate.setObjectName("actionGenerate")
        self.menuMidi.addAction(self.actionNew)
        self.menuMidi.addAction(self.actionOpen)
        self.menuMidi.addAction(self.actionSave)
        self.menuMidi.addAction(self.actionClear)
        self.menuMidi.addAction(self.actionGenerate)
        self.menuHelp.addAction(self.actionAbout)
        self.menu.addAction(self.menuMidi.menuAction())
        self.menu.addAction(self.menuHelp.menuAction())

        self.retranslateUi(tauMidiGenerator_Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(tauMidiGenerator_Mainwindow)

    def retranslateUi(self, tauMidiGenerator_Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        tauMidiGenerator_Mainwindow.setWindowTitle(_translate("tauMidiGenerator_Mainwindow", "tau Midi Generator - File name"))
        self.filename_grouBoc.setTitle(_translate("tauMidiGenerator_Mainwindow", "File name"))
        self.BrowseFileName_button.setText(_translate("tauMidiGenerator_Mainwindow", "Browse"))
        self.fileName_textfield.setPlaceholderText(_translate("tauMidiGenerator_Mainwindow", ">> Your file name here or press browse."))
        self.TrackList_groupbox.setTitle(_translate("tauMidiGenerator_Mainwindow", "Track List"))
        __sortingEnabled = self.tracList_list.isSortingEnabled()
        self.tracList_list.setSortingEnabled(False)
        item = self.tracList_list.item(0)
        item.setText(_translate("tauMidiGenerator_Mainwindow", "Track 01"))
        self.tracList_list.setSortingEnabled(__sortingEnabled)
        self.addTrack_button.setText(_translate("tauMidiGenerator_Mainwindow", "Add Track"))
        self.deleteTrack_button.setText(_translate("tauMidiGenerator_Mainwindow", "Delete Track"))
        self.trackAtributes_goupbox.setTitle(_translate("tauMidiGenerator_Mainwindow", "Track Atributes"))
        self.initvalue_label.setText(_translate("tauMidiGenerator_Mainwindow", "Init value:"))
        self.loosp_label.setText(_translate("tauMidiGenerator_Mainwindow", "Loops:"))
        self.chanel_label.setText(_translate("tauMidiGenerator_Mainwindow", "Chanel:"))
        self.track_clamp_label.setText(_translate("tauMidiGenerator_Mainwindow", "Clamp:"))
        self.randomSeed_label.setText(_translate("tauMidiGenerator_Mainwindow", "Random Seed:"))
        self.notesAtributes_groupbox.setTitle(_translate("tauMidiGenerator_Mainwindow", "Notes Atributes"))
        self.pitch_textfield.setText(_translate("tauMidiGenerator_Mainwindow", "sin(x)*200"))
        self.track_pitch_label.setText(_translate("tauMidiGenerator_Mainwindow", "pitch(x)="))
        self.track_time_label.setText(_translate("tauMidiGenerator_Mainwindow", "time(x)="))
        self.time_textfield.setText(_translate("tauMidiGenerator_Mainwindow", "x/2"))
        self.track_duration_label.setText(_translate("tauMidiGenerator_Mainwindow", "duration(x)="))
        self.duration_textfield.setText(_translate("tauMidiGenerator_Mainwindow", "0.1"))
        self.track_volume_label.setText(_translate("tauMidiGenerator_Mainwindow", "volume(x)="))
        self.volume_textfield.setText(_translate("tauMidiGenerator_Mainwindow", "100"))
        self.generate_button.setText(_translate("tauMidiGenerator_Mainwindow", "Generate"))
        self.options_groupbox.setTitle(_translate("tauMidiGenerator_Mainwindow", "Options"))
        self.autoRunMidi_check.setText(_translate("tauMidiGenerator_Mainwindow", "Autorun midi file"))
        self.openContainerFolder_check.setText(_translate("tauMidiGenerator_Mainwindow", "Open container folder"))
        self.autoSave_check.setText(_translate("tauMidiGenerator_Mainwindow", "Autosave when generate"))
        self.menuMidi.setTitle(_translate("tauMidiGenerator_Mainwindow", "Midi"))
        self.menuHelp.setTitle(_translate("tauMidiGenerator_Mainwindow", "Help"))
        self.actionNew.setText(_translate("tauMidiGenerator_Mainwindow", "New"))
        self.actionNew.setShortcut(_translate("tauMidiGenerator_Mainwindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("tauMidiGenerator_Mainwindow", "Open"))
        self.actionOpen.setShortcut(_translate("tauMidiGenerator_Mainwindow", "Ctrl+O"))
        self.actionSave.setText(_translate("tauMidiGenerator_Mainwindow", "Save"))
        self.actionSave.setShortcut(_translate("tauMidiGenerator_Mainwindow", "Ctrl+S"))
        self.actionClear.setText(_translate("tauMidiGenerator_Mainwindow", "Clear"))
        self.actionAbout.setText(_translate("tauMidiGenerator_Mainwindow", "About"))
        self.actionGenerate.setText(_translate("tauMidiGenerator_Mainwindow", "Generate"))
        self.actionGenerate.setShortcut(_translate("tauMidiGenerator_Mainwindow", "Ctrl+G"))

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tauMidiGenerator_Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_tauMidiGenerator_Mainwindow()
    ui.setupUi(tauMidiGenerator_Mainwindow)
    tauMidiGenerator_Mainwindow.show()
    sys.exit(app.exec_())
