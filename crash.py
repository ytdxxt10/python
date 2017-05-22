import os

#组织拼接命令行
def handleList(list,cmdStr):
    for address in list[::-1]:
        if(address.startswith('0x')):
            cmdStr = cmdStr + address + ' '
    return cmdStr

#将终端解析的结果写入文件中
def handleCmdStr(cmdStr):
    crashStr = os.popen(cmdStr).read()
    print(crashStr)
    with open('crash.txt', 'a') as f:
        f.writelines(crashStr+'\n')

fileName = input('请输入你要打开的文件名称').strip()
appName = input('请输入你要解析的包名').strip()
cmdStrPre = 'xcrun atos --arch arm64 -o ' + appName +'.app/' + appName + ' -l '

#打开需要解析的文件进行解析
with open(fileName) as f:
    for line in f.readlines():
        if appName in line:
            cmdStr = handleList(line.strip().split(' '),cmdStrPre)
            handleCmdStr(cmdStr)
        if line.startswith('***'):
            with open('crash.txt','a') as f:
                f.writelines('----'*10 + '\n\n')
                f.writelines(line)
