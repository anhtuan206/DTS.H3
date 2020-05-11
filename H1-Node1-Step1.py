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
    cliPrompt = userName + "@" + hostName + "% "
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
    showPrompt = userName + "@" + hostName + "> "
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
    cliPrompt = userName + "@" + hostName + "% "
    showPrompt = userName + "@" +hostName + "> "
    configPrompt = userName + "@" +hostName + "# "
    if check_cli(userName,hostName) == True:
        return True
    elif check_login() == True:
        if login(userName,hostName) == True:
            return True
    elif:
        cliprompt = False
        while cliprompt == False:
            crt.Screen.Send("exit" + "\n")
            cliprompt = crt.Screen.WaitForString(cliPrompt,60) 
            crt.Sleep(2000)
        return True
    else: return False

def get_show(userName,hostName):
    loginPrompt = "login: "
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
    else: return False
    
def get_config(userName,hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@" + hostName + "% "
    showPrompt = userName + "@" +hostName + "> "
    configPrompt = userName + "@" +hostName + "# "
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
    hostName = ""
    userName = ""
    result = crt.Dialog.MessageBox("Đã login vào thiết bị chưa?", "Logged-in?",  ICON_QUESTION | BUTTON_YESNO | DEFBUTTON2 )
    if result == IDNO:
        crt.Dialog.MessageBox("Đăng nhập bằng tài khoản dts trước khi chạy script!")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    else:
        confirm = False
        while confirm == False:
            userName = crt.Dialog.Prompt("Nhập user đang đăng nhập vào thiết bị (phân biệt chữ hoa và chữ thường): ","Logged in user")
            hostName = crt.Dialog.Prompt("Nhập hostname của thiết bị (phân biệt chữ hoa và chữ thường):","Hostname ")
            message = "Hostname: " + str(hostName) + "\n"+ "Username: " + str(userName) + "\n\n" + "Hostname và Username đang đăng nhập vào thiết bị đúng chưa?"
            result = crt.Dialog.MessageBox(message, "Confirm!", ICON_QUESTION | BUTTON_YESNOCANCEL | DEFBUTTON1 )
            if result == IDYES:
                confirm = True
            elif result == IDCANCEL:
                confirm = True
                crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    #Prompt variables with input username    
    loginPrompt = "login: "
    cliPrompt = userName + "@" + hostName + "% "
    showPrompt = userName + "@" + hostName + "> "
    configPrompt = userName + "@" + hostName + "# "
    #End prompt variables

    #Check prompt
    if check_cli(userName,hostName) != True and check_show(userName,hostName) != True and check_config(userName,hostName) != True:
        crt.Dialog.MessageBox("Không thể tìm thấy Prompt! Kiểm tra lại user và hostname vừa nhập!")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    #End check prompt

    #Change root password
    if get_config(userName,hostName) == True:
        crt.Screen.Send("set system root-authentication plain-text-password" + "\n")
        crt.Screen.WaitForString("New password:",60)
        crt.Sleep(2000)
        crt.Screen.Send("1234Aa@" + "\n")
        crt.Screen.WaitForString("Retype new password:",60)
        crt.Sleep(2000)
        crt.Screen.Send("1234Aa@" + "\n")
        crt.Screen.WaitForString(configPrompt,60)
        crt.Sleep(2000)
        crt.Screen.Send("commit and-quit" + "\n")
        crt.Screen.WaitForString("commit complete")
        crt.Sleep(2000)
        crt.Screen.Send("exit" + "\n")
        if userName == "root":
            crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(loginPrompt)
        crt.Sleep(2000)
        crt.Screen.Send("root" + "\n")
        crt.Screen.WaitForString("Password:")
        crt.Sleep(2000)
        crt.Screen.Send("1234Aa@" + "\n")
        
        #Renew prompt with root
        userName = "root"
        cliPrompt = userName + "@" + hostName + "% "
        showPrompt = userName + "@" + hostName + "> "
        configPrompt = userName + "@" + hostName + "# "
        #End prompt variables
            
        #Mount USB
        crt.Sleep(15000)
        crt.Screen.Send("\n")
        crt.Screen.WaitForString(cliPrompt)
        if mount_usb(userName, hostName) == True:
            crt.Sleep(10000)
            crt.Screen.Send("ls /mnt/ | grep junos" + "\n")
            usbContent = crt.Screen.ReadString(cliPrompt)
            if usbContent.find("junos-srxsme-18.2R3.4.tgz")!=-1:
                crt.Dialog.MessageBox("Kiểm tra file Junos thành công!")
            else:
                crt.Dialog.MessageBox("Kiểm tra file Junos thất bại")
            crt.Sleep(10000)
            crt.Screen.Send("mkdir /mnt/" + hostName + "\n")
            crt.Screen.WaitForString(cliPrompt)
            crt.Sleep(2000)
            crt.Screen.Send("cp /config/*.gz /mnt/" + hostName + "/" + "\n")
            crt.Screen.WaitForString(cliPrompt)
            crt.Sleep(2000)
            crt.Screen.Send("ls /mnt/" + hostName + "/" + "\n")
            #crt.Screen.WaitForString(cliPrompt)
            backupContent = crt.Screen.ReadString(cliPrompt)
            if backupContent.find("juniper.conf.gz") != -1:
                crt.Dialog.MessageBox("Backup cấu hình thành công!")
                crt.Sleep(1000)
                crt.Screen.Send("cli" + "\n")
                crt.Screen.WaitForString(showPrompt)
                #Log configure to computer
                crt.Screen.Send ("show configuration | no-more | display set" + "\n")
                configRead = crt.Screen.ReadString(showPrompt)
                crt.Sleep(5000)
                configFile = hostName + ".conf"
                fo = open(configFile ,"w+")
                fo.write(configRead)
                fo.close()
                crt.Sleep(1000)
                configFileTxt = hostName + ".export.txt"
                fo = open(configFile ,"r")
                fotxt = open(configFileTxt ,"w+")
                lines = fo.readlines()
                linecount = 0
                for line in lines:
                    if linecount >=1:
                        fotxt.write(line)
                    linecount += 1
                crt.Sleep(2000)
                fotxt.close()
                fo.close()
                #End logging configure
                crt.Screen.Send("request system software add /mnt/junos-srxsme-18.2R3.4.tgz no-copy best-effort-load no-validate" + "\n")
                crt.Screen.WaitForString(showPrompt)
                crt.Screen.Send("\n")
                crt.Screen.WaitForString(showPrompt)
                crt.Screen.Send("exit" + "\n")
                crt.Screen.WaitForString(cliPrompt)
                crt.Sleep(2000)
                crt.Screen.Send("umount /mnt" + "\n")
                crt.Sleep(3000)
                crt.Dialog.MessageBox("Hoàn thành cấu hình node 1")
            else:
                crt.Dialog.MessageBox("Backup cấu hình KHÔNG thành công!")
                crt.Sleep(1000)
                crt.Screen.WaitForString(showPrompt)
                #Log configure to computer
                crt.Screen.Send ("show configuration | no-more | display set" + "\n")
                configRead = crt.Screen.ReadString(showPrompt)
                crt.Sleep(5000)
                configFile = hostName + ".conf"
                fo = open(configFile ,"w+")
                fo.write(configRead)
                fo.close()
                crt.Sleep(1000)
                configFileTxt = hostName + ".export.txt"
                fo = open(configFile ,"r")
                fotxt = open(configFileTxt ,"w+")
                lines = fo.readlines()
                linecount = 0
                for line in lines:
                    if linecount >=1:
                        fotxt.write(line)
                    linecount += 1
                crt.Sleep(2000)
                fotxt.close()
                fo.close()
                #End logging configure
                crt.Screen.Send("request system software add /mnt/junos-srxsme-18.2R3.4.tgz no-copy best-effort-load no-validate" + "\n")
                crt.Screen.WaitForString(showPrompt)
                crt.Screen.Send("\n")
                crt.Screen.WaitForString(showPrompt)
                crt.Screen.Send("exit" + "\n")
                crt.Screen.WaitForString(cliPrompt)
                crt.Sleep(2000)
                crt.Screen.Send("umount /mnt" + "\n")
                crt.Sleep(3000)
                crt.Dialog.MessageBox("Hoàn thành cấu hình node 1")
        else:
            crt.Dialog.MessageBox("Lỗi mount USB")
            crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    else:
        crt.Dialog.MessageBox("Failed to change root password")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    #End change root password
    
        
main()