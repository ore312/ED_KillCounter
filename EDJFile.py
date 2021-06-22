from EDJConst import *
import os

#����`�ʥ�ե������ȡ��
def getFolderList(pSortFlag = False):
    aFiles = os.listdir(FOLDER_JRL)

    #ʹ��ʤ��ե������ȡ�����
    aList = []
    for i in range(len(aFiles)):
        if(aFiles[i].find(".log") != -1):
            if pSortFlag == True:
                aList.append({"Name":aFiles[i], "Date":os.path.getmtime(FOLDER_JRL + aFiles[i])})
            else:
                aList.append(aFiles[i])
    if pSortFlag != True:
        return aList

    #���`�Ȥ���
    aList = sorted(aList, key=lambda x:x['Date'])
    aOut = []
    for i in range(len(aList)):
        aOut.append(aList[i].get("Name"))
    aOut.reverse()
    return aOut


#���٤ƤΥ���`�ʥ�ξt������ȡ��
def getFolderSize():
    aOut = 0
    aFiles = getFolderList()
    for aF in aFiles:
        if(aF.find(".log") != -1):
            aOut += os.path.getsize(FOLDER_JRL + aF)
    return aOut


#ָ�����줿�Х��������i�ߤ��Ƴ���
def getByteFile(pPath, pByte = None):
    aOut = None
    with open(pPath, "rb") as f:
        if pByte != None:
            f.seek(os.path.getsize(pPath) - pByte)
        aOut = f.read()

    return aOut.decode()


#ָ�������Х������Υ���`�ʥ��ȡ�ä���
def getJson(pByte):
    aOut = ""

    #Ԫ�΂���仯�����Ƥ��ޤ��Τǉ������ä��Q����
    aBCnt = pByte

    #���`�Ȥ��줿�ե�����ꥹ�Ȥ�ȡ��
    aFiles = getFolderList(True)

    #�����ĥե�������i���z���Ŀ�ĤΥХ������˵��_���뤫
    aFCnt = 0
    aACnt = 0
    for aFCnt in range(len(aFiles)):
        if aACnt >= pByte:
            break
        aACnt += os.path.getsize(FOLDER_JRL + aFiles[aFCnt])

    #�⤷aFCnt=2���������Ϥ�2�ĥե����뤬����
    #n��Ŀ�����ᤫ�����Х��Ȥ��i���z��
    #0~n-1��Ŀ�Ϥ��٤��i���z��

    # print("B_FCnt :" + str(aFCnt))
    # print("B_BCnt :" + str(aBCnt))

    #�ե����뤬1�Ĥ���Y���Ƥ������
    if aFCnt == 1:
        aOut += getByteFile(FOLDER_JRL + aFiles[0], aBCnt)
    else:
        #�ꥹ�ȥ�����Ȥˉ�Q0���饹���`�ȤʤΤ�-1
        aFCnt -= 1
        #�ե������ޤ����Ǥ������
        #һ���Ť��ե������;�Ф�������ޤ��i���z��
        # print("fast:" + str((aBCnt - aACnt) + os.path.getsize(FOLDER_JRL + aFiles[aFCnt])))
        aFByte = (aBCnt - aACnt) + os.path.getsize(FOLDER_JRL + aFiles[aFCnt])
        aOut += getByteFile(FOLDER_JRL + aFiles[aFCnt], aFByte)

        #�Фä��ե������Ť�혤Ǥ��٤��i���z��
        for i in reversed(range(aFCnt)):
            aOut += getByteFile(FOLDER_JRL + aFiles[i])

    # print("A_FCnt :" + str(aFCnt))
    # print("A_BCnt :" + str(aBCnt))

    #�ꥹ����ʽ�ˤ���
    return aOut.split("\r\n")
