import os #cant move files to a different drive
import shutil
import subprocess   
import json 
import urllib.request   

#YOU WILL HAVE TO DO THESE YOURSELF AS I HAVENT PUSHED THE SOURCE WITH THIS
BEReplacement = ''
ACReplacement = ''
EOSReplacement = ''

class Network: #need to redo
    def DownloadFile(file, location):
        urllib.request.urlretrieve(file, location)

class File:
    def __init__(self) -> None:
        pass

    def Move(OldPath, NewPath): #NOTE moves one file/program at a time
        shutil.move(OldPath, NewPath)
    
    def MoveAll(FileOne, FileTwo, FileThree, NewPath): #NOTE moves three files/programs to the same location
        shutil.move(FileOne, NewPath)
        shutil.move(FileTwo, NewPath)
        shutil.move(FileThree, NewPath)

    def GetPath(): #get fortnite path 
        json_path = os.path.join(os.getenv('ProgramData'), 'Epic', 'UnrealEngineLauncher', 'LauncherInstalled.dat')
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

        str = ""
        installation_list = data.get('InstallationList', [])
        for jtoken in installation_list:
            if jtoken.get('AppName') == 'Fortnite':
                str = jtoken.get('InstallLocation', '')
        
        return str

class LaunchHelp: #just a class for launching in case I need to add anything else
    def __init__(self) -> None:
        pass

    def StartFortnite():
        command = r'cmd /C start com.epicgames.launcher://apps/Fortnite?action=launch'
        subprocess.run(command, shell=True)


fortPath = File.GetPath() #no more asking for a path :)

try: 
    #File.MoveAll('storage\\FortniteLauncher.exe', 'storage\\FortniteClient-Win64-Shipping_EAC.exe', 'storage\\FortniteClient-Win64-Shipping_EAC_EOS.exe', f'{fortPath}\\FortniteGame\\Binaries\\Win64\\')

    File.Move('storage\\FortniteLauncher.exe', f'{fortPath}\\FortniteGame\\Binaries\\Win64\\FortniteLauncher.exe')
    File.Move('storage\\FortniteClient-Win64-Shipping_EAC.exe', f'{fortPath}\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping_EAC.exe')
    File.Move('storage\\FortniteClient-Win64-Shipping_EAC_EOS.exe', f'{fortPath}\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping_EAC_EOS.exe')
    print('[+] Replaced files.')
except Exception as e:
    print(f'Failed to replace : {e}') #log the error
    input()


LaunchHelp.StartFortnite()
print('[+] Launched fortnite through epic')
input('Press "Enter" to close the console.')