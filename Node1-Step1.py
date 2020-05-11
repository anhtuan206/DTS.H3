# $language = "Python"

# $interface = "1.0"
def check_login():
	count = 1
	loginprompt = False
	loop = True
	while loop == True:
		crt.Screen.Send ("\n")
		loginprompt = crt.Screen.WaitForString("login: ",2)
		count += 1
		if count >= 5:
			loop = False
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
		loginprompt = crt.Screen.WaitForString(cliPrompt,2)
		count += 1
		if count >= 3:
			loop = False
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
		loginprompt = crt.Screen.WaitForString(showPrompt,2)
		count += 1
		if count >= 3:
			loop = False
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
		loginprompt = crt.Screen.WaitForString(configPrompt,2)
		count += 1
		if count >= 3:
			loop = False
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
    else:
        cliprompt = False
        while cliprompt == False:
            crt.Screen.Send("exit" + "\n")
            crt.Screen.Send("\n")
            cliprompt = crt.Screen.WaitForString(cliPrompt,2) 
        return True

def get_show(userName,hostName):
    loginPrompt = "login: "
    cliPrompt = userName + "@" + hostName + "% "
    showPrompt = userName + "@" +hostName + "> "
    configPrompt = userName + "@" +hostName + "# "
    if check_show(userName,hostName) == True:
        return True
    elif check_login() == True:
        if login(userName,hostName) == True:
			crt.Screen.Send("cli" + "\n")
			crt.Screen.WaitForString(showPrompt,2)
			if check_show(userName,hostName) == True:
				return True
			else: return False
    elif check_cli(userName,hostName) == True:
		crt.Screen.Send("cli" + "\n")
  		crt.Screen.WaitForString(showPrompt,2)
		if check_show(userName,hostName) == True:
			return True
    elif check_config(userName,hostName) == True:
        crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(showPrompt,2)
        if check_show(userName,hostName) == True:
            return True
    else:
        return False
    
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
			crt.Screen.WaitForString(showPrompt,2)
			if check_show(userName,hostName) == True:
				crt.Screen.Send("configure" + "\n")
				crt.Screen.WaitForString(configPrompt,2)
				if check_config(userName,hostName) == True:
					return True
			else: return False
    elif check_cli(userName,hostName) == True:
		crt.Screen.Send("cli" + "\n")
  		crt.Screen.WaitForString(showPrompt,2)
		if check_show(userName,hostName) == True:
				crt.Screen.Send("configure" + "\n")
				crt.Screen.WaitForString(configPrompt,2)
				if check_config(userName,hostName) == True:
					return True
				else: return False
		else: return False
    elif check_show(userName,hostName) == True:
		crt.Screen.Send("configure" + "\n")
		crt.Screen.WaitForString(configPrompt,2)
		if check_config(userName,hostName) == True:
			return True
		else: return False
    else:
        return False

def mount_usb(userName, hostName):
    cliPrompt = userName + "@" + hostName + "% "
    mountUsb = False
    count = 0
    while mountUsb == False:
        crt.Screen.Send("ls /dev/da1s*" + "\n")
        dev = crt.Screen.ReadString(cliPrompt,60)
        crt.Sleep(5000)
        count += 1
        for usb in range(1,10):
            devName = "da1s" + str(usb)
            if dev.find(devName)!=-1:
                crt.Screen.Send("mount_msdosfs /dev/"+ devName +" /mnt" + "\n")
                mountUsb = True
                break
        if count >= 5:
            mountUsb = True
    if mountUsb == True and count < 5:
        return True
    else:
        return False

def login(userName, hostName):
    cliPrompt = userName + "% "
    if hostName != "":
        cliPrompt = userName + "@" + hostName + "% "
    if check_login() == True:
        crt.Screen.Send("root" + "\n")
        crt.Screen.WaitForString("Password:",5)
        crt.Screen.Send("1234Aa@" + "\n")
        cliprompt = crt.Screen.WaitForString(cliPrompt,2)
        while cliprompt == False:
            crt.Screen.Send ("\n")
            crt.Screen.Send ("\n")
            crt.Screen.WaitForString("login: ",5)
            crt.Screen.Send ("root" + "\n")
            crt.Screen.WaitForString("Password: ",2)
            crt.Screen.Send ("1234Aa@" + "\n")
            cliprompt = crt.Screen.WaitForString(cliPrompt,15)
        if cliprompt == True:
            return True
    else: return False

def main():
    crt.Screen.Synchronous = True
    hostName = ""
    userName = ""
    result = crt.Dialog.MessageBox("Đã login vào thiết bị chưa?", "Logged-in?",  ICON_QUESTION | BUTTON_YESNO | DEFBUTTON2 )
    if result == IDNO:
        crt.Dialog.MessageBox("Vậy thì cút!")
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
    if check_cli(userName,hostName) != True or check_show(userName,hostName) != True or check_config(userName,hostName) != True:
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
        crt.Sleep(2000)
        crt.Screen.Send("exit" + "\n")
        crt.Screen.WaitForString(loginPrompt,60)
        crt.Sleep(2000)
        crt.Screen.Send("root" + "\n")
        crt.Screen.WaitForString("Password:",60)
        crt.Sleep(2000)
        crt.Screen.Send("1234Aa@" + "\n")
    else:
        crt.Dialog.MessageBox("Failed to change root password")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    #End change root password
    #Renew prompt with root
    userName = "root"
    cliPrompt = userName + "@" + hostName + "% "
    showPrompt = userName + "@" + hostName + "> "
    configPrompt = userName + "@" + hostName + "# "
    #End prompt variables
        
    #Mount USB
    if mount_usb() == True:
        crt.Sleep(2000)
        crt.Screen.Send("ls /mnt/" + "\n")
        usbContent = crt.Screen.ReadString(cliPrompt)
        crt.Sleep(1000)
        if usbContent.find("junos-srxsme-18.2R3.4.tgz")!=-1:
            crt.Screen.Send("mkdir /mnt/" + hostName + "\n")
            crt.Screen.WaitForString(cliPrompt)
            crt.Sleep(2000)
            crt.Screen.Send("cp /config/*.gz /mnt/" + hostName + "/" + "\n")
            crt.Screen.WaitForString(cliPrompt,20)
            crt.Sleep(2000)
            crt.Screen.Send("ls /mnt/" + hostName + "/" + "\n")
            crt.Screen.WaitForString(cliPrompt)
            backupContent = crt.Screen.ReadString(cliPrompt,60)
            if backupContent.find("juniper.conf.gz") != -1:
                crt.Screen.Send("cli" + "\n")
                crt.Screen.WaitForString(showPrompt)
                #Log configure to computer
                crt.Screen.Send ("file show /config/juniper.conf.gz | no-more" + "\n")
                configRead = crt.Screen.ReadString(showPrompt)
                crt.Sleep(1000)
                configFile = hostName + ".conf"
                fo = open(configFile ,"w+")
                fo.write(configRead)
                fo.close()
                crt.Sleep(1000)
                configFileTxt = hostName + ".txt"
                fo = open(configFile ,"r")
                fotxt = open(configFileTxt ,"w+")
                lines = fo.readlines()
                linecount = 0
                for line in lines:
                    if linecount >= 3:
                        fotxt.writelines(line)
                    linecount += 1
                crt.Sleep(2000)
                fotxt.close()
                fo.close()
                #End logging configure
                crt.Screen.Send("request system software add /mnt/junos-srxsme-18.2R3.4.tgz no-copy best-effort-load no-validate" + "\n")
                crt.Screen.WaitForString(showPrompt,3600)
                crt.Screen.Send("exit" + "\n")
                crt.Screen.WaitForString(cliPrompt,20)
                crt.Sleep(2000)
                crt.Screen.Send("umount /mnt" + "\n")
                crt.Sleep(3000)
                crt.Dialog.MessageBox("Hoàn thành cấu hình node 1"")
            else:
                crt.Dialog.MessageBox("Lỗi backup cấu hình ra USB")
                crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
        else:
            crt.Dialog.MessageBox("USB không chưa file Junos")
            crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
    else:
        crt.Dialog.MessageBox("Lỗi mount USB")
        crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
        
main()