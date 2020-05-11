# $language = "Python"

# $interface = "1.0"


def check_login():
    count = 1
    loginprompt = False
    loop = True
    while loop == True:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString("login: ",60)
        count += 1
        if loginprompt == True:
            loop = False
        elif count >= 3:
            loop = False
        else: loop = True
        crt.Sleep(10000)
    if loginprompt == True:
        return True
    else: return False

def check_cli(userName, hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "% "
    showPrompt = userName + "> "
    configPrompt = userName + "# "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "                                    
    count = 1
    loginprompt = False
    loop = True
    while loop == True:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString(cliPrompt,60)
        count += 1
        if loginprompt == True:
            loop = False
        elif count >= 3:
            loop = False
        else: loop = True
    if loginprompt == True:
        return True
    else: return False

def check_show(userName, hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@%"
    showPrompt = userName + "> "
    configPrompt = userName + "# "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + ":~ # "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "                    
    count = 1
    loginprompt = False
    loop = True
    while loop == True:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString(showPrompt,60)
        count += 1
        if loginprompt == True:
            loop = False
        elif count >= 3:
            loop = False
        else: loop = True
    if loginprompt == True:
        return True
    else: return False

def check_config(userName, hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@%"
    showPrompt = userName + "> "
    configPrompt = userName + "# "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + ":~ # "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "
    count = 1
    loginprompt = False
    loop = True
    while loop == True:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString(configPrompt,60)
        count += 1
        if loginprompt == True:
            loop = False
        elif count >= 3:
            loop = False
        else: loop = True
    if loginprompt == True:
        return True
    else: return False

def get_cli(userName,hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@% "
    showPrompt = userName + "> "
    configPrompt = userName + "# "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "
    if check_cli(userName,hostName) == True:
        return True
    elif check_login() == True:
        if login(userName,hostName) == True:
            return True
    elif:
        cliprompt = False
        while cliprompt == False:
            crt.Screen.Send("exit" + "\n")
            crt.Screen.Send("\n")
            cliprompt = crt.Screen.WaitForString(cliPrompt,60) 
            crt.Sleep(2000)
        return True
    else: return False

def get_show(userName,hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@% "
    showPrompt = userName + "> "
    configPrompt = userName + "# "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "
    if check_show(userName,hostName) == True:
        return True
    elif check_login() == True:
        if login(userName,hostName) == True:
            crt.Screen.Send("cli" + "\n")
            crt.Screen.WaitForString(showPrompt,60)
            if check_show(userName,hostName) == True:
                return True
            else: return False
    elif check_cli(userName,hostName) == True:
        crt.Screen.Send("cli" + "\n")
        crt.Screen.WaitForString(showPrompt,60)
        if check_show(userName,hostName) == True:
            return True
        else: return False
    elif check_config(userName,hostName) == True:
        crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(showPrompt,60)
        if check_show(userName,hostName) == True:
            return True
        else: return False
    else:
        return False

def get_config(userName,hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@% "
    showPrompt = userName + "> "
    configPrompt = userName + "# "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "
    if check_config(userName,hostName) == True:
        return True
    elif check_login() == True:
        if login(userName,hostName) == True:
            crt.Screen.Send("cli" + "\n")
            crt.Screen.WaitForString(showPrompt,60)
            if check_show(userName,hostName) == True:
                crt.Screen.Send("configure" + "\n")
                crt.Screen.WaitForString(configPrompt,60)
                if check_config(userName,hostName) == True:
                    return True
                else: return False
            else: return False
        else: return False
    elif check_cli(userName,hostName) == True:
        crt.Screen.Send("cli" + "\n")
        crt.Screen.WaitForString(showPrompt,60)
        if check_show(userName,hostName) == True:
                crt.Screen.Send("configure" + "\n")
                crt.Screen.WaitForString(configPrompt,60)
                if check_config(userName,hostName) == True:
                    return True
                else: return False
        else: return False
    elif check_show(userName,hostName) == True:
        crt.Screen.Send("configure" + "\n")
        crt.Screen.WaitForString(configPrompt,60)
        if check_config(userName,hostName) == True:
            return True
        else: return False
    else:
        return False

def mount_usb(userName, hostName):
    cliPrompt = userName + "@" + hostName + "% "
    mountUsb = False
    while mountUsb == False:
        crt.Screen.Send("ls /dev/da1s*" + "\n")
        dev = crt.Screen.ReadString(cliPrompt,60)
        crt.Sleep(5000)
        for usb in range(1,10):
            devName = "da1s" + str(usb)
            if dev.find(devName)!=-1:
                crt.Screen.Send("mount_msdosfs /dev/"+ devName +" /mnt" + "\n")
                mountUsb = True
                break
    if mountUsb == True:
        return True
    else:
        return False

def login(userName, hostName):
    cliPrompt = userName + "% "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
    if check_login() == True:
        crt.Screen.Send("root" + "\n")
        crt.Screen.WaitForString("Password:",60)
        crt.Sleep(5000)
        crt.Screen.Send("1234Aa@" + "\n")
        cliprompt = crt.Screen.WaitForString(cliPrompt,60)
        crt.Sleep(5000)
        while cliprompt == False:
            crt.Screen.Send ("\n")
            crt.Sleep(1000)
            crt.Screen.Send ("\n")
            crt.Sleep(1000)
            crt.Screen.WaitForString("login: ",60)
            crt.Sleep(3000)
            crt.Screen.Send ("root" + "\n")
            crt.Screen.WaitForString("Password: ",60)
            crt.Sleep(3000)
            crt.Screen.Send ("1234Aa@" + "\n")
            cliprompt = crt.Screen.WaitForString(cliPrompt,60)
            crt.Sleep(3000)
        if cliprompt == True:
            return True
    else: return False

def reboot_system():
    crt.Screen.Send ("request system reboot" + "\n")
    crt.Screen.WaitForString("Reboot the system ? [yes,no] (no) ",5)
    crt.Screen.Send ("yes" + "\n")
    crt.Screen.WaitForString("login: ")
    if check_login() == True:
        return True
    else: return False

def commit_check():
    crt.Screen.Send("commit check" + "\n")
    commitCheck = crt.Screen.ReadStrings("configuration check succeeds",300)
    if commitCheck == True:
        return True
    else: return False

def commit():
    crt.Screen.Send("commit" + "\n")
    commit = crt.Screen.ReadString("commit complete",300)
    if commit == True:
        return True
    else: return False



def main():
    crt.Screen.Synchronous = True
    loginPrompt = "login: "
    cliPrompt = "root@% "
    showPrompt = "root> "
    configPrompt = "root# "
    userName = "root"
    hostName = ""
    hostNameOld = ""
    loggedIn = False
    confirm = False
    mergeresult = False
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "                
    while confirm == False:
        hostNameOld = crt.Dialog.Prompt("Nhập hostname của thiết bị (phân biệt chữ hoa và chữ thường):","Hostname ")
        message = "Hostname: " + str(hostNameOld) + "\n\n" + "Hostname của thiết bị đúng chưa?"
        result = crt.Dialog.MessageBox(message, "Confirm!", ICON_QUESTION | BUTTON_YESNOCANCEL | DEFBUTTON1 )
        if result == IDYES:
            confirm = True
        elif result == IDCANCEL:
            confirm = True
            crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    # if get_cli(userName,hostName) == True:
        # Mount USB
        # if mount_usb(userName,hostName) == False:
            # crt.Dialog.MessageBox("Lỗi mount USB")
            # crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    # else:
        # crt.Dialog.MessageBox("Lỗi get cli prompt")
        # crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    #Move to configure mode
    # if get_config(userName,hostName) == True:
    #Load configuration from file from computer
    #crt.Dialog.MessageBox("Read Old Config")
    configFileTxt = hostNameOld + ".export.txt"
    fo = open(configFileTxt ,"r")
    lines = fo.readlines()
    #crt.Dialog.MessageBox("Read Old Config 1")
    crt.Screen.Send("load merge terminal" + "\n")
    crt.Sleep(5000)
    #crt.Dialog.MessageBox("Read Old Config 2")
    for line in lines:
        crt.Screen.Send(line)
        #crt.Sleep(1000)
    crt.Sleep(5000)
    crt.Screen.Send("\n\n")
    crt.Screen.Send("\004")
    #End Load configuration from file from computer

    #Load configuration from file from USB
    # crt.Screen.Send("load merge /mnt/"+hostNameOld+"/juniper.conf.gz")
    # mergeResult = crt.Screen.ReadString(configPrompt,60)
    # if mergeResult.find("load complete")!=-1 and mergeResult.find("errors")==-1:
    #     mergeresult = True
    #End load configuration from file from USB

    crt.Screen.WaitForString("load complete")
    crt.Screen.WaitForString(configPrompt)
    crt.Sleep(15000)
    fo.close()
    editConfigTxt = hostNameOld + ".txt"
    fo = open(editConfigTxt, "r")
    lines = fo.readlines()
    for line in lines:
        crt.Screen.Send(line + "\n")
        crt.Screen.WaitForString(configPrompt)
        crt.Sleep(1000)
    crt.Sleep(5000)
    fo.close()
    crt.Screen.Send("commit" + "\n")
    #Wait for commit success
    crt.Screen.WaitForString("commit complete")
    crt.Sleep(10000)
    if get_show(userName,hostNameOld) == True:
        if reboot_system() == True:
            if login(userName,hostNameOld) == True:
                #Redefine variables 
                loginPrompt = "login: "
                cliPrompt = userName + "@" + hostNameOld + "% "
                showPrompt = userName + "@" + hostNameOld + "> "
                configPrompt = userName + "@" + hostNameOld + "# "
                crt.Sleep(60000)
                #Get show prompt
                if get_show(userName,hostNameOld) == True:
                    #Get cluster ready
                    clusterStatus = False
                    while clusterStatus == False:
                        crt.Screen.Send ("\n")
                        clusterResult = crt.Screen.ReadString(showPrompt,10)
                        if str(clusterResult).find("{primary:node0}") != -1:
                            clusterStatus = True
                        crt.Sleep(5000)
                    #Get serial number
                    crt.Sleep(5000)
                    serialCheck = False
                    while serialCheck == False:
                        crt.Screen.Send("show chassis hardware | match chassis" + "\n")
                        readOutput = crt.Screen.ReadString("{primary:node0}",10)
                        readoutput = str(readOutput)
                        if readoutput.find("CY") != -1:
                            serialCheck = True
                        elif readoutput.find("CW") != -1:
                            serialCheck = True
                        elif readoutput.find("CZ") != -1:
                            serialCheck = True
                        else: crt.Sleep(5000)
                    crt.Sleep(10000)
                    serialNumber = readOutput.split()
                    serialnumber = str(serialNumber[7])
                    licenseFile = open("license.csv",'r')
                    lines = licenseFile.readlines()
                    licenseKey = ""
                    for line in lines:
                        if str(line.find(serialnumber)) != -1:
                            data = line.split(",")
                            licenseKey = data[1]
                            break
                    #End getting serial number

                    #Install license key
                    crt.Screen.Send("request system license add terminal" + "\n")
                    crt.Sleep(10000)
                    crt.Screen.Send(licenseKey + "\n\n")
                    crt.Sleep(10000)
                    crt.Screen.Send("\004")
                    crt.Sleep(10000)
                    #End install license key
                    crt.Screen.WaitForString("add license complete (no errors)")
                    crt.Screen.Send("request system autorecovery state save" + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    crt.Screen.Send("request system snapshot slice alternate node local " + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    #Wait for node1 become cluster secondary node
                    crt.Dialog.MessageBox("Chuyển dây và test! Sau khi hoàn thành gõ #checkcluster để tiếp tục")
                    crt.Sleep(300000)
                    crt.Screen.WaitForString("#checkcluster")
                    clusterStatus = False
                    while clusterStatus == False:
                        crt.Screen.Send ("show chassis cluster status | match node1" + "\n")
                        clusterResult = crt.Screen.ReadString(showPrompt,10)
                        if clusterResult.find("node1") != -1 and clusterResult.find("secondary") != -1 and clusterResult.find("100") != -1 and clusterResult.find("None") != -1 and clusterResult.find("CF") == -1:
                            clusterStatus = True
                        crt.Sleep(5000)
                
                    #Finallize 
                    crt.Screen.Send ("request system configuration rescue save" + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send ("request routing-engine login node 1" + "\n")
                    crt.Screen.WaitForString(cliPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send ("cli" + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send("request system autorecovery state save" + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send("exit" + "\n")
                    crt.Screen.WaitForString(cliPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send("exit" + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send ("request system snapshot slice alternate node 1" + "\n")
                    crt.Screen.WaitForString(showPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send ("configure" + "\n")
                    crt.Screen.WaitForString(configPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send ("set interface ge-0/0/3 description Internet" + "\n")
                    crt.Screen.WaitForString(configPrompt)
                    crt.Sleep(1000)
                    crt.Screen.Send ("commit" + "\n")
                    crt.Screen.WaitForStrings(["warning: L2 global mode is changed from non-l2 mode to switching mode. Please use the command request system reboot on current node or all nodes in case of HA cluster!","commit complete"])
                    crt.Screen.Send ("run request system reboot node 1" + "\n")
                    crt.Dialog.MessageBox("Hoàn thành! Backup cấu hình và thực hiện các bài test!")
                else: 
                    crt.Dialog.MessageBox("Lỗi get_show sau khi đăng nhập!")
            else:
                crt.Dialog.MessageBox("Lỗi kiểm tra đăng nhập")
        else:
            crt.Dialog.MessageBox("Lỗi gọi hàm reboot")
    else:
        crt.Dialog.MessageBox("Lỗi get_show trước khi reboot!")
main()