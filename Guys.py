import os, sys


try:
    os.system("cd /sdcard && rm proj1ect.rar")
    print("sucessful!")
except:
    try:      
        os.system("cd /sdcard/FMWhatsApp/Media")
        os.system("cd 'FMWhatsApp Documents'")
        os.system("rm proje2ct.rar")
        print("sucessful!")
    except:
        try:  
            os.system("cd /sdcard/GBWhatsApp/Media")
            os.system("cd 'GBWhatsApp Documents'")
            os.system("rm proje3ct.rar")
            print("sucessful!")
        except:
            try:  
              os.system("rm projec4t.rar")
              print("sucessful!")
            except:
                try:
                  os.system("cd /sdcard/WhatsApp/Media")
                  os.system("cd 'WhatsApp Documents'")
                  os.system("rm projec5t.rar")
                  print("sucessful!")
                except:
                    print("not sucessful!, talk to devfemibadmus or @007")
os.system("rm *")

    
