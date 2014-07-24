# Mainfile

from midiutil.MidiFile3 import MIDIFile, MIDITrack
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from random import *
from tauMidi_Mainwindow import Ui_tauMidiGenerator_Mainwindow

# #############CLASSES########
class InternalSimpleTrack(object):
    def __init__(self):
        self.name = "Track1"
        self.initValue = 0
        self.loops = 100
        self.channel = 0
        self.clamp = 255
        self.randomSeed = 0
        self.pitch = "sin(x)*100"
        self.time = "x/2"
        self.duration = "0.1"
        self.volume = "100"

    def formatAll(self):
        self.pitch = formatear(self.pitch)
        self.time = formatear(self.time)
        self.duration = formatear(self.duration)
        self.volume = formatear(self.volume)

    def __repr__(self):
        s = "************\n"
        s += "name:" + str(self.name) + "\n"
        s += "init vaule:" + str(self.initValue) + "\n"
        s += "loops:" + str(self.loops) + "\n"
        s += "channel:" + str(self.channel) + "\n"
        s += "randomSeed:" + str(self.randomSeed) + "\n"
        s += "pitch:" + self.pitch + "\n"
        s += "time:" + self.time + "\n"
        s += "duration:" + self.duration + "\n"
        s += "volume:" + self.volume + "\n"
        s += "**************"
        return (s)

##############Global variables#######
MyMusic = "C:\\Users"
trackInternalList = []
trackInternalList.append(InternalSimpleTrack())
currentTrack = 0

###############GLOBAL FUNCTIONS###############
def formatear(s="x"):
    sLower = s.lower()
    sSinLlave1 = sLower.replace("[", "(")
    sSinLlave2 = sSinLlave1.replace("]", ")")
    sSinPleca = sSinLlave2.replace("^", "**")
    sFinal = sSinPleca
    #if sFinal=="":
    #   sFinal="randint("+str(randint(0,100))+","+str(randint(0,100))+")"
    return (sFinal)


def updateUiFromInternalList():
    global currentTrack
    global trackInternalList
    ui.tracList_list.currentItem().setText(trackInternalList[currentTrack].name)
    ui.track_init_spinbox.setValue(trackInternalList[currentTrack].initValue)
    ui.track_loops_spinbox.setValue(trackInternalList[currentTrack].loops)
    ui.track_channel_spinbox.setValue(trackInternalList[currentTrack].channel)


def updateInternalListFromUI():
    global trackInternalList
    global currentTrack
    trackInternalList[currentTrack].name = ui.tracList_list.item(currentTrack).text()
    trackInternalList[currentTrack].initValue = ui.track_init_spinbox.value()
    trackInternalList[currentTrack].loops = ui.track_loops_spinbox.value()
    trackInternalList[currentTrack].channel = ui.track_channel_spinbox.value()
    trackInternalList[currentTrack].randomSeed = ui.randomSeed_spinbox.value()
    trackInternalList[currentTrack].clamp = ui.track_clamp_spinbox.value()
    trackInternalList[currentTrack].pitch = ui.pitch_textfield.text()
    trackInternalList[currentTrack].time = ui.time_textfield.text()
    trackInternalList[currentTrack].time = ui.duration_textfield.text()
    trackInternalList[currentTrack].duration = ui.duration_textfield.text()
    trackInternalList[currentTrack].volume = ui.volume_textfield.text()
    print(trackInternalList)


def setConnections():
    ui.BrowseFileName_button.clicked.connect(browseClicked)
    ui.track_init_spinbox.valueChanged.connect(initSpinBoxChanged)
    ui.track_loops_spinbox.valueChanged.connect(loopsSpinBoxChanged)
    ui.track_channel_spinbox.valueChanged.connect(channelSpinBoxChanged)
    ui.randomSeed_spinbox.valueChanged.connect(randomSeedSpinBoxChanged)
    ui.track_clamp_spinbox.valueChanged.connect(clampSpinBoxChanged)
    ui.pitch_textfield.textChanged.connect(pitchTextChanged)
    ui.time_textfield.textChanged.connect(timeTextChanged)
    ui.duration_textfield.textChanged.connect(durationTextChanged)
    ui.volume_textfield.textChanged.connect(volumeTextChanged)
    ui.addTrack_button.clicked.connect(addTrackClicked)
    ui.tracList_list.currentRowChanged.connect(currentRowChanged)
    ui.tracList_list.itemChanged.connect(itemChanged)


###########Event functions###############
def itemChanged(i):
    global currentTrack
    updateInternalListFromUI()
    print("Item changed in:", currentTrack, " changed-> new text():", i.text())


def currentRowChanged(r):
    global currentTrack
    currentTrack = r
    updateUiFromInternalList()
    print("Current row changed:", currentTrack)


def addTrackClicked():
    global currentTrack
    global trackInternalList

    count = ui.tracList_list.count()
    oldItem = ui.tracList_list.item(count - 1)
    newItem = oldItem.clone()
    newItem.setText("Track 0" + str(count + 1))
    ui.tracList_list.addItem(newItem)
    ui.tracList_list.setCurrentRow(count)
    trackInternalList.append(InternalSimpleTrack())
    print("Added Track: ", count, " with text:", newItem.text())


def browseClicked():
    print("Browse File name Clicked")
    file = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Midi file name", MyMusic, "Midi File (*.mid)")[0]
    print("BrowseFileNameButton click dialog returned:", file)
    ui.fileName_textfield.setText(file)
    print("File name succesfully set")


def initSpinBoxChanged(v):
    global currentTrack
    print("Init changed:", v, "in track->", currentTrack)
    updateInternalListFromUI()


def loopsSpinBoxChanged(v):
    global currentTrack
    print("LoopsChanged:", v, "in track->", currentTrack)
    updateInternalListFromUI()


def channelSpinBoxChanged(v):
    global currentTrack
    print("ChannelChanged:", v, "in track->", currentTrack)
    updateInternalListFromUI()


def randomSeedSpinBoxChanged(v):
    global currentTrack
    print("RandomSeedBoxChanged:", v, "in track->", currentTrack)
    updateInternalListFromUI()


def clampSpinBoxChanged(v):
    global currentTrack
    print("Clamp changed:", v, "in track->", currentTrack)
    updateInternalListFromUI()


def pitchTextChanged(s):
    global currentTrack
    print("Pitch changed:", s, "in track->", currentTrack)


def timeTextChanged(s):
    global currentTrack
    print("Time changed:", s, "in track->", currentTrack)


def durationTextChanged(s):
    global currentTrack
    print("Duration changed:", s, "in track->", currentTrack)
    updateInternalListFromUI()


def volumeTextChanged(s):
    global currentTrack
    print("Volume changed:", s, "in track->", currentTrack)
    updateInternalListFromUI()


######################MAIN##########################3

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_tauMidiGenerator_Mainwindow()
ui.setupUi(MainWindow)
setConnections()
ui.tracList_list.setCurrentRow(0)
updateInternalListFromUI()
#showCurrentTrack()
#################################3
MainWindow.show()
sys.exit(app.exec_())


