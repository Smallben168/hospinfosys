
def isError(msgList):
    #檢查是否為錯誤訊息
    if '_status' in msgList[0]:
        if msgList[0]['_status'] == "error":
            return msgList[0]['_status_doc']
    else:
        return ""