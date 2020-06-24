from copy import deepcopy
from music21 import stream, pitch, note, interval, chord, clef, text
import pandas as pd

class SyzygiaeBaryphoni:
    triciniaDict = {"perfecte composita": {"perfecta": ["M3", "P5"],
                                      "imperfecta": ["m3", "P5"]},
                "supremaManente": {"perfecta": [["P4", "M6"], ["M3", "P12"]],
                                   "imperfecta": [["P4", "m6"], ["m3", "P12"]]},
                "mediaManante": {"perfecta": [["m6", "m10"], ["P5", "M10"]],
                                 "imperfecta": [["M6", "M10"], ["P5", "m10"]]},
                "basisManente": {"perfecta": [["M10", "P12"], ["m3", "m6"]],
                                  "imperfecta": [["m10", "P12"], ["M3", "M6"]]},
                "omnesMoventur": {"perfecta": [["M3", "P12"], ["P5", "M17"], ["m3", "m13"]],
                                  "imperfecta": [["m3", "P12"], ["P5", "m17"], ["M3", "M13"]]}
    }
    triciniaTP = [
        ["M3", "P5"], ["P4", "M6"],
        ["M3", "P12"], ["m6", "m10"],
        ["P5", "M10"], ["M10", "P12"],
        ["m3", "m6"], ["M3", "P12"],
        ["P5", "M17"], ["m3", "m13"]
    ]

    triciniaTI = [
        ["m3", "P5"],
        ["P4", "m6"], ["m3", "P12"],
        ["M6", "M10"], ["P5", "m10"],
        ["m10", "P12"], ["M3", "M6"],
        ["m3", "P12"], ["P5", "m17"], ["M3", "M13"]
    ]

    quadriciniaTP = [
        ["M3", "P5", "P8"], ["P5", "M10", "P15"], ["M3", "P8", "P12"], ["P5", "P8", "M10"], ["P8", "M10", "P12"], ["P8", "P12", "M17"],
        ["m6", "m10", "m13"], ["m3", "m6", "m13"], ["m6", "m13", "m17"], ["P4", "M6", "P11"], ["P4", "P11", "M13"],

        ["M3", "P5", "P12"], ["P5", "M10", "P12"], ["m3", "m6", "m10"], ["m3", "m10", "m13"], ["P4", "M6", "P8"],
        ["M6", "P11", "P15"], ["P4", "P8", "M13"], ["P8", "P11", "M13"], ["M6", "P8", "P11"],
    ]

    quadriciniaTI = [
        ["m3", "P5", "P8"], ["P5", "m10", "P15"], ["m3", "P8", "P12"], ["P5", "P8", "m10"], ["P8", "m10", "P12"], ["P8", "P12", "m17"],
        ["M6", "M10", "M13"], ["M3", "M6", "M13"], ["M6", "M13", "M17"], ["P4", "m6", "P11"], ["P4", "P11", "m13"],

        ["m3", "P5", "P12"], ["P5", "m10", "P12"], ["M3", "M6", "M10"], ["M3", "M10", "M13"], ["P4", "m6", "P8"],
        ["m6", "P11", "P15"], ["P4", "P8", "m13"], ["P8", "P11", "m13"], ["m6", "P8", "P11"],
    ]

    quindriciniaTP = [
        ["M3", "P5", "P8", "P12"], ["P5", "M10", "P12", "P15"], ["M3", "P8", "P12", "P19"],
        ["P5", "P8", "M10", "P12"], ["P8", "M10", "P12", "P19"], ["P8", "P12", "M17", "P19"],
        ["M3", "P5", "P12", "P15"], ["M3", "P12", "P15", "P19"], ["P5", "P8", "P12", "M17"], ["P5", "P12", "P15", "M17"],

        ["M3", "P5", "P8", "P15"], ["M3", "P5", "M10", "P15"], ["M3", "P8", "M10", "P12"], ["P5", "M10", "P15", "M17"],
        ["P5", "P8", "M10", "M17"], ["P8", "M10", "P12", "M17"], ["M10", "P12", "P15", "M17"],

        ["M3", "P5", "M10", "P12"], ["M3", "P5", "P12", "M17"], ["M3", "M10", "P12", "P19"],
        ["P5", "M10", "P12", "M17"], ["P5", "M10", "M17", "P19"], ["M10", "P12", "M17", "P19"]
    ]

    quindriciniaTI = [
        ["m3", "P5", "P8", "P12"], ["P5", "m10", "P12", "P15"], ["m3", "P8", "P12", "P19"],
        ["P5", "P8", "m10", "P12"], ["P8", "m10", "P12", "P19"], ["P8", "P12", "m17", "P19"],
        ["m3", "P5", "P12", "P15"], ["m3", "P12", "P15", "P19"], ["P5", "P8", "P12", "m17"], ["P5", "P12", "P15", "m17"],

        ["m3", "P5", "P8", "P15"], ["m3", "P5", "m10", "P15"], ["m3", "P8", "m10", "P12"], ["P5", "m10", "P15", "m17"],
        ["P5", "P8", "m10", "m17"], ["P8", "m10", "P12", "m17"], ["m10", "P12", "P15", "m17"],

        ["m3", "P5", "m10", "P12"], ["m3", "P5", "P12", "m17"], ["m3", "m10", "P12", "P19"],
        ["P5", "m10", "P12", "m17"], ["P5", "m10", "m17", "P19"], ["m10", "P12", "m17", "P19"]
    ]

    syzygiaPerfecteCompositaTP = [["M3", "P5", "P8", "M10", "P12"]]
    syzygiaPerfecteCompositaTI = [["m3", "P5", "P8", "m10", "P12"]]

    def getAllSyzygiae():
        all = []
        all.append(SyzygiaeBaryphoni.triciniaTP)
        all.append(SyzygiaeBaryphoni.triciniaTI)
        all.append(SyzygiaeBaryphoni.quadriciniaTP)
        all.append(SyzygiaeBaryphoni.quadriciniaTI)
        all.append(SyzygiaeBaryphoni.quindriciniaTP)
        all.append(SyzygiaeBaryphoni.quindriciniaTI)
        all.append(SyzygiaeBaryphoni.syzygiaPerfecteCompositaTP)
        all.append(SyzygiaeBaryphoni.syzygiaPerfecteCompositaTI)
        allSyzygiae = [item for sublist in all for item in sublist]
        return allSyzygiae

    def getAllBaryphonianSyzygiae():
        all = []
        all.append(SyzygiaeBaryphoni.triciniaTP)
#        all.append(SyzygiaeBaryphoni.triciniaTI)
        all.append(SyzygiaeBaryphoni.quadriciniaTP)
#        all.append(SyzygiaeBaryphoni.quadriciniaTI)
        all.append(SyzygiaeBaryphoni.quindriciniaTP)
#        all.append(SyzygiaeBaryphoni.quindriciniaTI)
        all.append(SyzygiaeBaryphoni.syzygiaPerfecteCompositaTP)
#        all.append(SyzygiaeBaryphoni.syzygiaPerfecteCompositaTI)
        allSyzygiae = [item for sublist in all for item in sublist]
        return allSyzygiae

class VocalScoreDistributor:
    def __init__(self):
        self.part1 = stream.Part()
        self.part2 = stream.Part()
        bassclef = clef.BassClef()
        self.part2.insert(0, bassclef)

    def parseIntervalStructure(self, sounding, qL=4, splitNote="C4"):
        theSound = sounding.IntervallStruktur
        bass = note.Note("C3")
        bass.quarterLength = qL
        self._distributeNotes2VocalScore(theSound, bass, splitNote)

    def parseData(self, sounding, qL=2, splitNote="C4"):
        theSound = sounding.IntervallStruktur
        bassnotes = list(sounding.Bassnoten)
        bassschritte = sounding.Bassschritte
        followingSoundings = []
        for bs in bassschritte:
            for syz in bassschritte[bs]:
                followingSoundings.append((bs, syz))
        
        #print(followingSoundings)
        bass = note.Note(bassnotes[0])
        bass.quarterLength = qL

        for each in followingSoundings:
            self._distributeNotes2VocalScore(theSound, bass, splitNote)
            secondBass = interval.transposeNote(bass, each[0])
            self._distributeNotes2VocalScore(each[1], secondBass, splitNote)


    def _distributeNotes2VocalScore(self, listOfIntervals, bassNote, splitNote="C4"):
        cpBass = deepcopy(bassNote)
        if bassNote.pitch >= pitch.Pitch(splitNote):
            self.part1.append(cpBass)
        else:
            self.part2.append(cpBass)

        #offset setzen        
        offset = cpBass.offset

        #Akkorde hinzusetzen
        for intv in listOfIntervals:
            #print(intv)
            nNew = interval.transposeNote(bassNote, intv)
            if nNew.pitch >= pitch.Pitch(splitNote):
                self.part1.insert(offset, nNew)
            else:
                self.part2.insert(offset, nNew)
    
    def getVocalScore(self):
        vs = stream.Stream()
        vs.insert(0, self.part1)
        vs.insert(0, self.part2)
        return vs
    
    def clearResults(self):
        self.__init__()



class SyzygiaeAnalyser:
    def __init__(self):
        self.chordDict = {}
        self.progDict = {}


    def _getIntervalList(self, aChord):
        intListStr = []
        baseNote = aChord[0]
        for each in aChord:
            if baseNote != each:
                currentInterval = interval.Interval(aChord[0], each)
                intListStr.append(currentInterval.name)
        theKey = "--".join(intListStr)
        return intListStr, theKey


    def _getDisposition(self, intListStr):
        sortingList = ["P4","m6","M6","P11","m13","M13","P18","m20","M20"]
        bassDerivates = len([x for x in intListStr if x in ["P1","P8","P15","P22"]]) + 1
        thirdDerivates = len([x for x in intListStr if x in ["m3","M3","m10","M10","m17","M17"]])
        fifthDerivates = len([x for x in intListStr if x in ["P5","P12","P19"]])
        fourthDerivates = len([x for x in intListStr if x in ["P4","P11","P18"]])
        sixthDerivates = len([x for x in intListStr if x in ["m6","M6","m13","M13","m20","M20"]])
    
        classificationList = list(set(intListStr).intersection(sortingList))
        if classificationList == []:
            b = bassDerivates
            m = thirdDerivates
            s = fifthDerivates
            return [b, m, s]
        elif len(set(["P4","P11","P18"]) & set(classificationList)) > 0:
            b = fourthDerivates
            m = sixthDerivates
            s = bassDerivates
            return [b, m, s]
        elif len(set(["m6","M6","m13","M13","m20","M20"]) & set(classificationList)) > 0:
            b = sixthDerivates
            m = bassDerivates
            s = thirdDerivates
            return b, m, s
        return []


    def _getTrigaClass(self, sortedChord, intListStr):
        if sortedChord.isTriad():
            if sortedChord.isMajorTriad():
                if list(set(intListStr) - set(["P1","M3","P5"])) == []:
                    trigaClass = ["TP", "prop"]
                else:
                    if len(set(intListStr)) <= 3:
                        trigaClass = ["TP", "remota"]
                    else:
                        trigaClass = ["TP", "icomp"]
            elif sortedChord.isMinorTriad():
                if list(set(intListStr) - set(["P1","M3","P5"])) == []:
                    trigaClass = ["TI", "prop"]
                else:
                    if len(set(intListStr)) <= 3:
                        trigaClass = ["TI", "remota"]
                    else:
                        trigaClass = ["TI", "icomp"]
            else:
                trigaClass = ["TA", ""]
        elif len(sortedChord) <= 1:
            return ["M", "Einzeltoene"]
        elif len(sortedChord) == 2:
            return ["D", intListStr[0]]
        else:
            if sortedChord.isConsonant():
                return ["C", list(set(intListStr) - set(["P1","P8","P15","P22"]))]
            else:
                return ["TA", ""]
        return trigaClass


    def _generateSlicingStream(self, dataStream):
        shortestNote = note.Note()
        shortestNote.quarterLength = 8
        for each in dataStream.flat.notesAndRests:
            if shortestNote.quarterLength > each.quarterLength:
                shortestNote = each

        repeater = dataStream.flat.highestOffset / shortestNote.quarterLength
        slicingStream = stream.Stream()
        slicingStream.repeatAppend(shortestNote, int(repeater))
        return slicingStream
        #print("Kleinster Notenwert des Stückes:", shortestNote.quarterLength)

    def _writeBassProgression(self, lastKey, intListStr, bassNote, lastBassNote):
        bassProgInt = interval.Interval(note.Note(lastBassNote), note.Note(bassNote)).directedName
        if bassProgInt in self.chordDict[lastKey]["Bassschritte"]:
            self.chordDict[lastKey]["Bassschritte"][bassProgInt].append(intListStr)
        else:
            self.chordDict[lastKey]["Bassschritte"][bassProgInt] = []
            self.chordDict[lastKey]["Bassschritte"][bassProgInt].append(intListStr)

    def analyse(self, dataStream, storeProgressions=False, storeOccurrence=False, storeBass=False):
        piece = dataStream.filePath.name
        #print(piece)
        lastChordSorted = chord.Chord()
        lastKey = ""
        lastUnsortedKey = ""
        bassNote = ""
        lastBassNote = ""
        slicingStream = self._generateSlicingStream(dataStream)

        for each in slicingStream.flat.notesAndRests:
            innerDict = {}
            sliceOfStream = dataStream.flat.notes.allPlayingWhileSounding(each)

            aChord = chord.Chord([each for each in sliceOfStream.flat.notes])
            sortedChord = aChord.sortAscending()

            #Es muss etwas zum Analysieren geben.
            if len(sortedChord) != 0:
                intListStr, theKey = self._getIntervalList(sortedChord)
                bassNote = sortedChord[0].nameWithOctave

                #Fall 1: Die Syzygia ist schon da gewesen.
                if theKey in self.chordDict:
                    if sortedChord.pitches == lastChordSorted.pitches:
                        self.chordDict[theKey]["Dauer"] += each.quarterLength
                    else:
                        self.chordDict[theKey]["Anzahl"] += 1
                        self.chordDict[theKey]["Dauer"] += each.quarterLength
                        if storeBass:
                            if bassNote in self.chordDict[theKey]["Bassnoten"]:
                                self.chordDict[theKey]["Bassnoten"][bassNote] += 1
                            else:
                                self.chordDict[theKey]["Bassnoten"][bassNote] = 1
                        if storeOccurrence:                      
                            if piece in self.chordDict[theKey]["Stellen"]:
                                self.chordDict[theKey]["Stellen"][piece].append(each.offset)
                            else:
                                self.chordDict[theKey]["Stellen"][piece] = [each.offset]
                        if storeProgressions:
                            if lastKey != "" and lastBassNote != "":
                                self._writeBassProgression(lastKey, intListStr, bassNote, lastBassNote)

                #Fall 2: Die Syzygia ist noch nicht da gewesen und muss neu angelegt werden.
                elif theKey not in self.chordDict:
                    innerDict["StimmenZahl"] = len(intListStr) + 1
                    tC = self._getTrigaClass(sortedChord, intListStr)
                    innerDict["TrigaKlasse"] = tC[0]
                    innerDict["TrigaAttribut"] = tC[1]
                    if innerDict["TrigaKlasse"] in ["TP","TI"]:
                        b, m, s = self._getDisposition(intListStr)
                        innerDict["b"] = b
                        innerDict["m"] = m
                        innerDict["s"] = s
                        verteilung = [b, m, s]
                        if verteilung == [2,2,2] and len(set(intListStr)) == 5:
                            innerDict["TrigaAttribut"] = "pcomp"
                    innerDict["IntervallStruktur"] = intListStr
                    innerDict["Anzahl"] = 1
                    innerDict["Dauer"] = each.quarterLength
                    if storeBass:
                        innerDict["Bassnoten"] = {}
                        innerDict["Bassnoten"][sortedChord[0].nameWithOctave] = 1
                    if storeOccurrence:
                        innerDict["Stellen"] = {piece : [each.offset]}
                    if storeProgressions:
                        innerDict["Bassschritte"] = {}
                        if lastKey != "" and lastBassNote != "":
                            self._writeBassProgression(lastKey, intListStr, bassNote, lastBassNote)

                    self.chordDict[theKey] = innerDict

                lastBassNote = bassNote
                lastChordSorted = sortedChord
                lastKey = theKey
            else:
                pass #Nothing to analyse!


    def analyseProgs(self, dataStream):
        partList = [i for i in range(0, len(dataStream.parts))]
        lastChord = chord.Chord()
        lastKey = ""
        slicingStream = self._generateSlicingStream(dataStream)

        for each in slicingStream.flat.notesAndRests:
            vSon = chord.Chord()
            for thePart in range(-1, -len(partList)-1, -1):
                aNote = dataStream.parts[thePart].notesAndRests.get()



    def _analyseProgressions(self, son1, son2):
        if son1 in self.progDict:
            if son2 in self.progDict[son1]:
                self.progDict[son1][son2] += 1
            else:
                self.progDict[son1][son2] = 1
        else:
            self.progDict[son1] = {}
            self.progDict[son1][son2] = 1


    def getProgDict(self):
        return self.progDict


    def getChordDict(self):
        return self.chordDict


    def clearChordDict(self):
        self.chordDict = {}



class ProgressionAnalyser:
    def __init__(self):
        self.progDict = {}
        self.shortestNote = note.Note()
        self.bassProgDict = {}
        self.bassProgList = []


    def _generateSlicingStream(self, dataStream):
        self.shortestNote = note.Note()
        self.shortestNote.quarterLength = 8
        for each in dataStream.flat.notesAndRests:
            if self.shortestNote.quarterLength > each.quarterLength:
                self.shortestNote = each

        repeater = dataStream.flat.highestOffset / self.shortestNote.quarterLength
        slicingStream = stream.Stream()
        slicingStream.repeatAppend(self.shortestNote, int(repeater))
        return slicingStream
    
    def _getBassProgression(self, lastBassNote, bassNote):
        bassProg = interval.Interval(pitch.Pitch(lastBassNote), pitch.Pitch(bassNote)).directedName
        return bassProg
    
    def makeNgramObject(self, n=2):
        #ngram Bausteine erstellen
        for i in range(len(self.bassProgList[n:])):
            gramList = []
            for cntr in range(n):
                gramList.append(self.bassProgList[i+cntr])
            gram = "_".join(gramList)
            #print(gram)
            #self.bassProgDict[gram] = ["blubb"]
            if gram in self.bassProgDict:
                self.bassProgDict[gram]["Anzahl"] += 1
            else:
                self.bassProgDict[gram] = {}
                self.bassProgDict[gram]["Anzahl"] = 1
                self.bassProgDict[gram]["Folge"] = []
            self.bassProgDict[gram]["Folge"].append(self.bassProgList[i+n])
                


    def analyse(self, dataStream):
        lastChord = []
        slicingStream = self._generateSlicingStream(dataStream)
        numParts = len(dataStream.parts)
        lastBassNoteExists = False

        for each in slicingStream.flat.notesAndRests:
            aChord = []
            bassNoteSet = False
            bProg = "Beginn"

            for cPart in range(-1, -numParts-1, -1):
                aNoteStream = dataStream.parts[cPart].flat.allPlayingWhileSounding(each)
                if len(aNoteStream.flat.notes) > 0:
                    aNote = aNoteStream.flat.notes[0]
                    aChord.append(aNote.nameWithOctave)
                    if not bassNoteSet or aNote.pitch < note.Note(bassNote).pitch:
                        bassNoteSet = True
                        bassNote = aNote.nameWithOctave

            if lastBassNoteExists and bassNoteSet:
                print(bassNote)
                if int(each.offset) == each.offset:
                    bProg = self._getBassProgression(lastBassNote, bassNote)
                    self.bassProgList.append(bProg)
                    #print("Bassprogression: ", bProg, lastBassNote, bassNote)

            if aChord != lastChord and len(aChord) > 0:
                #print("Output", aChord)
                intList = []
                firstNote = aChord[0]
                for secondNote in aChord[1:]:
                    #print(firstNote, secondNote)
                    intList.append(interval.Interval(pitch.Pitch(firstNote), pitch.Pitch(secondNote)).name)
                if bProg in self.progDict:
                    self.progDict[bProg]["firstChord"].append(lastChord)
                    self.progDict[bProg]["secondChord"].append(aChord)
                else:
                    self.progDict[bProg] = {"firstChord": [], "secondChord": []}
                    self.progDict[bProg]["firstChord"].append(lastChord)
                    self.progDict[bProg]["secondChord"].append(aChord)
                #print(intList, "Bassnote: ", bassNote)
            if bassNoteSet:
                lastBassNote = bassNote
                lastBassNoteExists = True
            else:
                lastBassNoteExists = False
            lastChord = aChord

        
    def getProgDict(self):
        return self.progDict

    def clearProgDict(self):
        self.progDict = {}

    def getBassProgDict(self):
        return self.bassProgDict

    def clearBassProgDict(self):
        self.bassProgDict = {}

    def getProgList(self):
        return self.bassProgList

    def clearProgList(self):
        self.bassProgList = []