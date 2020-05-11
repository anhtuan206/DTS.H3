#Đang viết...
Requirement: 
    Phần mềm SecureCRT
    File license: license.csv lưu ở thư mục Document trên máy tính
    File cấu hình template lưu ở thư mục Document trên máy tính. Tên file là hostname của thiết bị cũ.

1. MÔ TẢ SCRIPT
    Node0-Step1.py
    - Mount USB
    - Upgrade software 
    - Reboot Node 0 after upgraded
    Node0-Step2.py
    - Read configuration export from Node1-Step1.py script
    - Merge the configuration
    - Update the configuration with the template
    - Reboot after upgrade
    Node1-Step1.py
    - Mount USB
    - Export configuration to the local computer
    - Backup the configuration to the folder on USB. The folder name is the name of the site
    - Upgrade the software without reboot
2. CÁC BƯỚC CHẠY SCRIPT
    2.1. Login vào node 1, để con trỏ tại showprompt
    2.2. Chạy script Node1-Step1.py trên node1
    2.3. Nhập username đang dùng để đăng nhập vào thiết bị và hostname đang được cấu hình trên Node1

    2.4. Chuyển sang node 0, login vào bằng user root và để con trỏ tại cli prompt
    2.5. Chạy script Node0-Step1.py
