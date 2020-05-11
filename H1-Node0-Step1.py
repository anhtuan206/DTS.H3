# $language = "Python"

# $interface = "1.0"
def check_login():
    count = 1
    while count <= 2:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString("login: ",2)
        count = count+1
        if loginprompt == True:
            return True
    return False
def check_show():
    count = 1
    while count <= 2:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString("root> ",2)
        count = count+1
        if loginprompt == True:
            return True
    return False
def check_conf():
    count = 1
    while count <= 2:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString("root# ",2)
        count = count+1
        if loginprompt == True:
            return True
    return False
def check_cli():
    count = 1
    while count <= 2:
        crt.Screen.Send ("\n")
        loginprompt = crt.Screen.WaitForString("% ",2)
        count = count+1
        if loginprompt == True:
            return True
    return False

def mount_usb():
    cliPrompt = "% "
    mountUsb = False
    while mountUsb == False:
        #Test git commit
        crt.Screen.Send("ls /dev/da1s*" + "\n")
        dev = crt.Screen.ReadString(cliPrompt)
        crt.Sleep(3000)
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

def reboot_system():
    cliPrompt = False
    if check_login() == True:
        crt.Screen.Send ("root" + "\n")
    elif check_cli() == True:
        crt.Screen.Send ("cli" + "\n")
    elif check_show() == True:
        crt.Screen.Send ("\n")
    elif check_conf() == True:
        crt.Screen.Send ("exit" + "\n")
    crt.Screen.WaitForString("root> ",2)
    crt.Screen.Send ("request system reboot" + "\n")
    crt.Screen.WaitForString("Reboot the system ? [yes,no] (no) ",2)
    crt.Screen.Send ("yes" + "\n")
    crt.Screen.WaitForString("login: ",1800)
    crt.Screen.Send ("root" + "\n")
    crt.Screen.WaitForString("Password: ",60)
    crt.Screen.Send ("1234Aa@" + "\n")
    cliPrompt = crt.Screen.WaitForString("root@:~ # ",60)
    if cliPrompt == False:
        return False
    else: return True	

def main():
    crt.Screen.Synchronous = True
    loginPrompt = "login: "
    cliPrompt = "% "
    showPrompt = "root> "
    configPrompt = "root# "

    #Get Cli prompt
    currentCli = False
    if check_login == True:
        crt.Screen.Send("root" + "\n")
        crt.Screen.WaitForString(cliPrompt,2)
        currentCli = True
    elif check_show() == True:
        crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(cliPrompt,2)
        currentCli = True
    elif check_conf() == True:
        crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(showPrompt,2)
        crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(cliPrompt,2)
        currentCli = True
    elif check_cli() == True:
        currentCli = True
    else:
        crt.Dialog.MessageBox("Getting cli prompt failed!")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
        
    #Mount USB
    if mount_usb() == True:
        #Delete configuration, config cluster, upgrade software then reboot system
        crt.Screen.Send("cli" + "\n")
        crt.Screen.WaitForString(showPrompt)
        crt.Sleep(2000)
        crt.Screen.Send("configure" + "\n")
        crt.Screen.WaitForString(configPrompt)
        crt.Sleep(2000)
        crt.Screen.Send("delete" + "\n")
        crt.Screen.WaitForString("Delete everything under this level? [yes,no] (no) ")
        crt.Sleep(2000)
        crt.Screen.Send("yes" + "\n")
        crt.Screen.WaitForString(configPrompt)
        crt.Sleep(2000)
        crt.Screen.Send("set system root-authentication plain-text-password" + "\n")
        crt.Screen.WaitForString("New password:")
        crt.Sleep(2000)
        crt.Screen.Send("1234Aa@" + "\n")
        crt.Screen.WaitForString("Retype new password:")
        crt.Sleep(500)
        crt.Screen.Send("1234Aa@" + "\n")
        crt.Screen.WaitForString(configPrompt)
        crt.Sleep(2000)
        crt.Screen.Send("commit and-quit" + "\n")
        crt.Screen.WaitForString(showPrompt)
        crt.Sleep(30000)
        crt.Screen.Send("set chassis cluster cluster-id 1 node 0" + "\n")
        crt.Screen.WaitForString(showPrompt)
        crt.Sleep(500)
        crt.Screen.Send("configure" + "\n")
        crt.Screen.WaitForString(configPrompt,60)
        crt.Sleep(500)
        crt.Screen.Send("set chassis cluster redundancy-group 0 node 0 priority 200" + "\n")
        crt.Screen.WaitForString(configPrompt,60)
        crt.Sleep(500)
        crt.Screen.Send("set chassis cluster redundancy-group 0 node 1 priority 100" + "\n")
        crt.Screen.WaitForString(configPrompt,60)
        crt.Sleep(500)
        crt.Screen.Send("commit and-quit" + "\n")
        crt.Screen.WaitForString(showPrompt,120)
        crt.Sleep(500)
        crt.Screen.Send("request system software add /mnt/junos-srxsme-18.2R3.4.tgz no-copy reboot best-effort-load no-validate" + "\n")
        #Check the reboot completed then login
        currentCli = False
        crt.Screen.WaitForString(loginPrompt,1800)
        crt.Sleep(10000)
        crt.Screen.Send ("\n")
        crt.Screen.Send ("root" + "\n")
        crt.Screen.WaitForString("Password: ",30)
        crt.Sleep(1000)
        crt.Screen.Send ("1234Aa@" + "\n")
        currentCli = crt.Screen.WaitForString(cliPrompt,30)
        crt.Sleep(1000)
        while currentCli == False:
            if check_cli(userName,hostName) == True:
                currentCli = True
            else:
                crt.Screen.Send ("\n")
                crt.Sleep(1000)
                crt.Screen.Send ("\n")
                crt.Screen.WaitForString("login: ",60)
                crt.Sleep(1000)
                crt.Screen.Send ("root" + "\n")
                crt.Screen.WaitForString("Password: ",2)
                crt.Sleep(1000)
                crt.Screen.Send ("1234Aa@" + "\n")
                currentCli = crt.Screen.WaitForString(cliPrompt,2)
                crt.Sleep(1000)
        #Check cluster status
        crt.Screen.Send ("cli" + "\n")
        crt.Screen.WaitForString(showPrompt,60)
        crt.Sleep(1000)
        clusterStatus = False
        while clusterStatus == False:
            crt.Screen.Send ("\n")
            clusterResult = crt.Screen.ReadString(showPrompt,30)
            if str(clusterResult).find("{primary:node0}") != -1:
                clusterStatus = True
            else:
                crt.Sleep(5000)
        if clusterStatus == True:
            crt.Dialog.MessageBox("Cluster is up! Kiểm tra file cấu hình và chạy script thứ 2!")
    else:
        crt.Dialog.MessageBox("Lỗi mount USB")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
main()