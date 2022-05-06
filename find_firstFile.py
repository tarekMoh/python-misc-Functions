import os
import win32security

def findFirstFile(filepath):
    for path, subdirs, files in os.walk(filepath):
        for name in files:
            f_name = os.path.join(path, name)
            if os.path.exists(f_name):
                if os.path.isfile(f_name):
                    ###### get file domain ######
                    sd = win32security.GetFileSecurity (f_name, win32security.OWNER_SECURITY_INFORMATION)
                    owner_sid = sd.GetSecurityDescriptorOwner ()
                    ownername, domain, type = win32security.LookupAccountSid (None, owner_sid)
                    ###### get file extension ######
                    root, extension = os.path.splitext(f_name)
                    ###### get file size #######
                    file_size = os.path.getsize(f_name)
                    if ((domain == "AD" or ownername == "Administrators") and (extension == ".exe") and (file_size < 1835008)):
                        return name
    return False                
                    
def test_findFile1():
    file_path = ".\\test_data1"
    assert findFirstFile(file_path) == "find_firstFile.exe"

def test_findFile2():
    file_path = ".\\test_data2"
    assert findFirstFile(file_path) == False

def test_findFile3():
    file_path = ".\\test_data3"
    assert findFirstFile(file_path) == False

def test_findFile4():
    file_path = ".\\test_data4"
    assert findFirstFile(file_path) == False