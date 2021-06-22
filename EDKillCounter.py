# { "timestamp":"2021-02-25T11:30:26Z", "event":"FSDJump", "StarSystem":"Tascheter Sector ON-T a3-0", "SystemAddress":5366024522520, "StarPos":[-12.25000,-44.18750,-72.34375], "SystemAllegiance":"", "SystemEconomy":"$economy_None;", "SystemEconomy_Localised":"None", "SystemSecondEconomy":"$economy_None;", "SystemSecondEconomy_Localised":"None", "SystemGovernment":"$government_None;", "SystemGovernment_Localised":"None", "SystemSecurity":"$GAlAXY_MAP_INFO_state_anarchy;", "SystemSecurity_Localised":"Anarchy", "Population":0, "Body":"Tascheter Sector ON-T a3-0 A", "BodyID":1, "BodyType":"Star", "JumpDist":2.428, "FuelUsed":0.022178, "FuelLevel":12.511004 }

# { "timestamp":"2021-02-25T11:24:42Z", "event":"CommitCrime", "CrimeType":"murder", "Faction":"EXO", "Victim":"John Dickerson", "Bounty":689500 }

# { "timestamp":"2021-03-11T11:09:21Z", "event":"Bounty", "Rewards":[ { "Faction":"Pikum Public Group", "Reward":4515 } ], "Target":"eagle", "TotalReward":4515, "VictimFaction":"Dinda Bureau" }

# { "timestamp":"2021-03-11T12:36:05Z", "event":"SupercruiseExit", "StarSystem":"Yamahun", "SystemAddress":22958210566936, "Body":"Yamahun A 4", "BodyID":11, "BodyType":"Planet" }
# { "timestamp":"2021-03-11T12:40:01Z", "event":"FactionKillBond", "Reward":42025, "AwardingFaction":"SIRA Incorporated", "VictimFaction":"EXO" }
# { "timestamp":"2021-03-11T12:51:01Z", "event":"SupercruiseEntry", "StarSystem":"Yamahun", "SystemAddress":22958210566936 }

# { "timestamp":"2021-06-17T18:49:47Z", "event":"CommitCrime", "CrimeType":"onFoot_murder", "Faction":"BZ Ceti Justice Party", "Victim":"Antonio Garcia", "Bounty":1000 }

from EDJournalLib import *
import json
import time
import datetime
#debug
import sys
import os

VERSION = "0.0.6"

FOLDER_DATA = ".\\data\\"
FILE_SAVEPATH = ".\\savepath.txt"

TAG_EVENT = "event"
TAG_SYSTEM = "StarSystem"
TAG_CRIMETYPE = "CrimeType"
TAG_FACTION = "Faction"
TAG_BOUNTY = "Bounty"
TAG_REWARD = "Reward"
TAG_AWARDINGFACTION = "AwardingFaction"
TAG_TOTALREWARD = "TotalReward"
TAG_VICTIMFACTION = "VictimFaction"

EVENT_CRIME = "CommitCrime"
EVENT_FSD = "FSDJump"
EVENT_FACTIONKILLBOND = "FactionKillBond"
EVENT_SUPERCRUISEENTRY = "SupercruiseEntry"
EVENT_ASSAULT = "assault"
EVENT_MURDER = "murder"
EVENT_OFMURDER = "onFoot_murder"
EVENT_BOUNTY = "Bounty"

mSaveFile = ""
mData = []
mNowSystem = ""

# class clsWar:
#     def __init__(self):
#         self.SystemName = ""
#         self.FactionName = ""
#         self.KillCount = 0
#         self.Bond = 0
#
#     def __repr__(self):
#         return repr((self.SystemName, self.FactionName, self.KillCount))
#
#     def setData(self, pSystemName, pFactionName, pKillCount, pBond):
#         self.SystemName = pSystemName
#         self.FactionName = pFactionName
#         self.KillCount = pKillCount
#         self.Bond = pBond

class clsData:
    def __init__(self):
        self.SystemName = ""
        self.FactionName = ""
        self.KillCount = 0
        self.Bounty = 0
        self.Bond = 0
        self.OfKillCount = 0
        self.OfBounty = 0
        self.OfBond = 0
        # self.War = []

    def __repr__(self):
        return repr((self.SystemName, self.FactionName, self.KillCount, self.OfKillCount))
    # def addWar(self, pSystemName, pFactionName, pKillCount, pBond):
    #     aData = clsWar()
    #     aData.setData(pSystemName, pFactionName, pKillCount, pBond)
    #     self.War.append(aData)

def sortData(pData):
    return sorted(pData, key=lambda u: u.SystemName)

def getNowTimeFileName(pDebug):
    if pDebug != True:
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    else:
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".debug.json"

def writeData():
    global mData
    def json_method(pData):
        if isinstance(pData, object) and hasattr(pData, '__dict__'):
            return pData.__dict__
        # else:
        #     raise TypeError
    aData = sortData(mData)
    aStr = json.dumps(aData, default=json_method, indent=4)
    with open(FOLDER_DATA + mSaveFile, mode="w", encoding="utf-8") as aFNo:
        aFNo.write(aStr);

def dispKillData():
    global mData

    if len(mData) == 0:
        return

    def json_method(pData):
        if isinstance(pData, object) and hasattr(pData, '__dict__'):
            return pData.__dict__
        # else:
        #     raise TypeError
    aData = sortData(mData)
    aStr = json.dumps(aData, default=json_method, indent=4)
    print(aStr)




    # def getSpace(pVal, pCnt):
    #     return str(" " * (pCnt - len(str(pVal))))
    #
    # aData = sortData(mData)
    # aBSys = ""
    # for aD in aData:
    #     aOut = ""
    #     aSpace = 2
    #     if aBSys != aD.SystemName:
    #         aOut += "SYSTEM:" + aD.SystemName + "\n"
    #         aOut += "Bounty By:" + aD.FactionName + "\n"
    #     aOut += (" " * aSpace) + aD.FactionName + ":" + "{:,}".format(aD.KillCount) + "\n"
    #     if aBSys != aD.SystemName:
    #         aBSys = aD.SystemName
    #         if aD.Bounty != None:
    #             aOut += "TotalBounty:" + "{:,}".format(aD.Bounty) + "\n"
    #         if aD.Bond != None:
    #             aOut += "TotalBund:" + "{:,}".format(aD.Bond) + "\n"
    #         aOut += "\n"
    #
    # print(aOut)




    # aSC = 0
    # aFC = 0
    # aKC = 0
    # aBC = 0
    # for aD in aData:
    #     if aSC < len(aD.SystemName):
    #         aSC = len(aD.SystemName)
    #     if aFC < len(aD.FactionName):
    #         aFC = len(aD.FactionName)
    #     if aKC < len("{:,}".format(aD.KillCount)):
    #         aKC = len("{:,}".format(aD.KillCount))
    #     if aBC < len("{:,}".format(aD.Bounty)):
    #         aBC = len("{:,}".format(aD.Bounty))

    # print("bounty data")
    # for aD in aData:
    #     aOut = ""
    #     aOut += "system : " + aD.SystemName + getSpace(aD.SystemName, aSC)
    #     aOut += " : faction : " + aD.FactionName + getSpace(aD.FactionName, aFC)
    #     aOut += " : kill : " + str("{:,}".format(aD.KillCount)) + getSpace("{:,}".format(aD.KillCount), aKC)
    #     aOut += " : bounty : " + str("{:,}".format(aD.Bounty)) + getSpace("{:,}".format(aD.Bounty), aBC)
    #     print(aOut)
    print("\n")

#データを加算または追加する
def addData(pFactionName, pKill=None, pBounty=None, pBond=None, pOfKill=None, pOfBounty=None, pOfBond=None):
    global mData
    for i in range(len(mData)):
        if mData[i].SystemName == mNowSystem and mData[i].FactionName == pFactionName:
            #たまに値が飛んでこないのでその対策
            if pKill != None:
                mData[i].KillCount += pKill
            if pBounty != None:
                mData[i].Bounty += pBounty
            if pBond != None:
                mData[i].Bond += pBond
            if pOfKill != None:
                mData[i].OfKillCount += pOfKill
            if pOfBounty != None:
                mData[i].OfBounty += pOfBounty
            if pOfBond != None:
                mData[i].OfBond += pOfBond
            return
    aData = clsData()
    aData.SystemName = mNowSystem
    aData.FactionName = pFactionName
    if pKill != None:
        aData.KillCount += pKill
    if pBounty != None:
        aData.Bounty += pBounty
    if pBond != None:
        aData.Bond += pBond
    if pOfKill != None:
        aData.OfKillCount += pOfKill
    if pOfBounty != None:
        aData.OfBounty += pOfBounty
    if pOfBond != None:
        aData.OfBond += pOfBond
    mData.append(aData)

#ジャーナルイベント処理
def fncJrl(pJrl):
    global mNowSystem

    for i in range(len(pJrl) - 1):
        aJson = None
        try:
            aJson = json.loads(pJrl[i])
        except Exception:
            continue
        if aJson == None:
            continue

        #debug
        if aJson.get(TAG_EVENT) == EVENT_FSD or \
                aJson.get(TAG_EVENT) == EVENT_CRIME or \
                aJson.get(TAG_EVENT) == EVENT_BOUNTY:
            print(aJson)

        #星系移動時に移動先の星系名を保管する
        if aJson.get(TAG_EVENT) == EVENT_FSD:
            mNowSystem = aJson.get(TAG_SYSTEM)
            print("set new system name > " + mNowSystem)
            continue

        #
        #ship
        #

        #殺した判定
        if aJson.get(TAG_EVENT) == EVENT_CRIME:
            if aJson.get(TAG_CRIMETYPE) == EVENT_MURDER:
                addData(aJson.get(TAG_FACTION), pKill=1, pBounty=aJson.get(TAG_BOUNTY))
                dispKillData()
                writeData()
                continue
            if aJson.get(TAG_CRIMETYPE) == EVENT_ASSAULT:
                addData(aJson.get(TAG_FACTION), pBounty=aJson.get(TAG_BOUNTY))
                dispKillData()
                writeData()
                continue

        #ウォンテッドを殺した時の判定
        if aJson.get(TAG_EVENT) == EVENT_BOUNTY:
            if aJson.get(TAG_TOTALREWARD) != None and aJson.get(TAG_VICTIMFACTION) != None:
                addData(aJson.get(TAG_VICTIMFACTION), pKill=1, pBond=aJson.get(TAG_TOTALREWARD))
                dispKillData()
                writeData()
                continue

        #
        #on foot
        #

        #殺した判定
        if aJson.get(TAG_EVENT) == EVENT_CRIME:
            if aJson.get(TAG_CRIMETYPE) == EVENT_OFMURDER:
                addData(aJson.get(TAG_FACTION), pOfKill=1, pOfBounty=aJson.get(TAG_BOUNTY))
                dispKillData()
                writeData()
                continue

        # #戦争関連の判定
        # # SupercruiseExit
        # #     FactionKillBond
        # # SupercruiseEntry
        # if aJson.get(TAG_EVENT) == EVENT_FACTIONKILLBOND:
        #     print(aJson)    #debug
        #     pass

        # if aJson.get(TAG_EVENT) == EVENT_SUPERCRUISEENTRY:
        #     print(aJson)    #debug
        #     pass

def runDebug(pPath):
    for aP in pPath:
        if os.path.exists(aP) != True:
            # print("error:invalid path")
            continue

        aStr = None
        with open(aP, "rb") as f:
            aByte = f.read()
            aStr = aByte.decode()
        fncJrl(aStr.split("\r\n"))

def writeSavePath():
    with open(FILE_SAVEPATH, mode="w", encoding="utf-8") as aFNo:
        aFNo.write(FOLDER_DATA + mSaveFile)

def main():
    global mSaveFile

    print("Ver:" + VERSION)

    mSaveFile = getNowTimeFileName(False)
    print("start")

    #debug
    if len(sys.argv) > 1:
        print("debug")
        mSaveFile = getNowTimeFileName(True)
        dispKillData()
        writeData()

        args = sys.argv
        runDebug(args)
        return

    init()
    setInterval(200)
    setFnc(fncJrl)
    startJournal()

    dispKillData()
    writeData()

    writeSavePath()

if __name__ == "__main__":
    main()
