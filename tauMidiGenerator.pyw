# Mainfile

from midiutil.MidiFile3 import MIDIFile, MIDITrack
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from random import *
from math import *
from time import time
from tauMidi_Mainwindow import Ui_tauMidiGenerator_Mainwindow
import functionGenerator

# #############CLASSES########
class InternalSimpleTrack(object):
    def __init__(self):
        self.name = "NEW TRACK"
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

# #############Global variables#######
MyMusic = "C:\\Users"
trackInternalList = []
trackInternalList.append(InternalSimpleTrack())
currentTrack = 0

# ##############GLOBAL FUNCTIONS###############
def formatear(s="x"):
    sLower = s.lower()
    sSinLlave1 = sLower.replace("[", "(")
    sSinLlave2 = sSinLlave1.replace("]", ")")
    sSinPleca = sSinLlave2.replace("^", "**")
    sFinal = sSinPleca
    # if sFinal=="":
    #   sFinal="randint("+str(randint(0,100))+","+str(randint(0,100))+")"
    return (sFinal)


def updateUiFromInternalList():
    global currentTrack
    global trackInternalList
    ui.tracList_list.currentItem().setText(trackInternalList[currentTrack].name)
    ui.track_init_spinbox.setValue(trackInternalList[currentTrack].initValue)
    ui.track_loops_spinbox.setValue(trackInternalList[currentTrack].loops)
    ui.track_channel_spinbox.setValue(trackInternalList[currentTrack].channel)
    ui.track_clamp_spinbox.setValue(trackInternalList[currentTrack].clamp)
    ui.randomSeed_spinbox.setValue(trackInternalList[currentTrack].randomSeed)
    ui.pitch_textfield.setText(trackInternalList[currentTrack].pitch)
    ui.time_textfield.setText(trackInternalList[currentTrack].time)
    ui.duration_textfield.setText(trackInternalList[currentTrack].duration)
    ui.volume_textfield.setText(trackInternalList[currentTrack].volume)
    print("-------------------------ui->Inter----------------------")
    print(trackInternalList)


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
    trackInternalList[currentTrack].duration = ui.duration_textfield.text()
    trackInternalList[currentTrack].volume = ui.volume_textfield.text()
    print("-----------------IN->UI----------------")
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
    ui.deleteTrack_button.clicked.connect(deletTrackClicked)
    ui.tracList_list.currentRowChanged.connect(currentRowChanged)
    ui.tracList_list.itemChanged.connect(itemChanged)
    ui.fileName_textfield.textChanged.connect(fileTextChanged)
    ui.generate_button.clicked.connect(generateClicked)
    ui.pitch_button.clicked.connect(onPitchButton)
    ui.time_button.clicked.connect(onTimeButton)
    ui.duration_button.clicked.connect(onDurationButton)
    ui.volume_button.clicked.connect(onVolumeButton)


def onVolumeButton():
    ui.volume_textfield.setText(str(functionGenerator.DefaultRandomFunction()))


def onDurationButton():
    ui.duration_textfield.setText(str(functionGenerator.DefaultRandomFunction()))


def onTimeButton():
    ui.time_textfield.setText(str(functionGenerator.DefaultRandomFunction()))


def onPitchButton():
    ui.pitch_textfield.setText(str(functionGenerator.DefaultRandomFunction()))


def makeTrack(startAt=0, loops=100, track=0, channel=0, pitch="x", time="x", duration="0.5*x", volume="x", clamp=255,
              initSeed=0):
    seed(initSeed)
    tempNoteList = []
    for x in range(0, loops):
        pit = pitch.replace("x", str(x))
        ti = time.replace("x", str(x))
        du = duration.replace("x", str(x))
        vo = volume.replace("x", str(x))
        # #########################
        try:
            p = int(abs(eval(pit)))
            if p > clamp: p = clamp
        except:
            m=QtWidgets.QMessageBox()
            m.setText("Error evaluating Pitch")
            m.setDetailedText("An error occured evaluating pitch:\n"+pit)
            m.setWindowTitle("Error")
            m.exec()
            break
        try:
            t = abs(eval(ti))
        except:
            m=QtWidgets.QMessageBox()
            m.setText("Error evaluating Time")
            m.setDetailedText("An error occured evaluating time:\n"+ti)
            m.setWindowTitle("Error")
            m.exec()
            break
        try:
            d = abs(eval(du))
        except:
            m=QtWidgets.QMessageBox()
            m.setText("Error evaluating Duration")
            m.setDetailedText("An error occured evaluating duration:\n"+du)
            m.setWindowTitle("Error")
            m.exec()
            break
        try:
            v = int(abs(eval(vo)))
        except:
            m=QtWidgets.QMessageBox()
            m.setText("Error evaluating Volumen")
            m.setDetailedText("An error occured evaluating volume:\n"+vo)
            m.setWindowTitle("Error")
            m.exec()
            break
        #print(pi,ti,du,vo)
        try:
            tempNotesDict = {"c": channel, "p": p, "t": t, "d": d, "v": v}
            tempNoteList.append(tempNotesDict)
        except:
            pass
    return tempNoteList


# ##########Event functions###############
#mjairobenito@gmail.
def generateClicked():
    time0 = time()
    global trackInternalList
    tempMidi = MIDIFile(len(trackInternalList))
    for t in range(0, len(trackInternalList)):
        tempMidi.addTempo(t, 0, ui.tempo_spin.value())
        workTrack = trackInternalList[t]
        tempMidi.addTrackName(t, 0, workTrack.name)
        workDict = makeTrack(workTrack.initValue, workTrack.loops, t, workTrack.channel, workTrack.pitch,
                             workTrack.time, workTrack.duration, workTrack.volume, workTrack.clamp,
                             workTrack.randomSeed)
        #workdict es una lista de diccionarios
        for n in workDict:
            tempMidi.addNote(t, n["c"], n["p"], n["t"], n["d"], n["v"])
    midiBin = open(ui.fileName_textfield.text(), "wb")
    tempMidi.writeFile(midiBin)
    midiBin.close()
    print("Midi object generated in: ", time() - time0, " seconds")


def fileTextChanged(s):
    if ui.fileName_textfield.text() != "" and (
                    "\\" in ui.fileName_textfield.text() or "/" in ui.fileName_textfield.text()):
        ui.generate_button.setEnabled(True)
    else:
        ui.generate_button.setEnabled(False)


def itemChanged(i):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].name = i.text()
    #updateInternalListFromUI()
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
    trackInternalList.append(InternalSimpleTrack())
    trackInternalList[-1].name += " " + str(count)
    newItem.setText(trackInternalList[-1].name)
    ui.tracList_list.addItem(newItem)
    ui.tracList_list.setCurrentRow(count)
    print("Added Track: ", count, " with text:", newItem.text())


def deletTrackClicked():
    if ui.tracList_list.count() < 2:
        print("No track to delete")
    else:
        global currentTrack
        global trackInternalList
        i = ui.tracList_list.takeItem(currentTrack)
        i = None
        del trackInternalList[currentTrack]
        ui.tracList_list.setCurrentRow(currentTrack)


def browseClicked():
    print("Browse File name Clicked")
    file = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Midi file name", MyMusic, "Midi File (*.mid)")[0]
    print("BrowseFileNameButton click dialog returned:", file)
    ui.fileName_textfield.setText(file)
    print("File name succesfully set")


def initSpinBoxChanged(v):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].initValue = v
    print("Init changed:", v, "in track->", currentTrack)
    #updateInternalListFromUI()


def loopsSpinBoxChanged(v):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].loops = v
    print("LoopsChanged:", v, "in track->", currentTrack)
    #updateInternalListFromUI()


def channelSpinBoxChanged(v):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].channel = v
    print("ChannelChanged:", v, "in track->", currentTrack)
    #updateInternalListFromUI()


def randomSeedSpinBoxChanged(v):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].randomSeed = v
    print("RandomSeedBoxChanged:", v, "in track->", currentTrack)
    #updateInternalListFromUI()


def clampSpinBoxChanged(v):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].clamp = v
    print("Clamp changed:", v, "in track->", currentTrack)
    #updateInternalListFromUI()


def pitchTextChanged(s):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].pitch = s
    #updateInternalListFromUI()
    print("Pitch changed:", s, "in track->", currentTrack)


def timeTextChanged(s):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].time = s
    #updateInternalListFromUI()
    print("Time changed:", s, "in track->", currentTrack)


def durationTextChanged(s):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].duration = s
    print("Duration changed:", s, "in track->", currentTrack)
    #updateInternalListFromUI()


def volumeTextChanged(s):
    global currentTrack
    global trackInternalList
    trackInternalList[currentTrack].volume = s
    print("Volume changed:", s, "in track->", currentTrack)
    #updateInternalListFromUI()


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


