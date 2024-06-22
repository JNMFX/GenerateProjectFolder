from pathlib import Path

#Grab folder location
launchPath = Path(__file__).resolve()

workingPath = launchPath.parent

#Function that checks if the folder already exists
def folderCheck(folderPath):
    folder = Path(folderPath)
    if folder.is_dir():
        return True
    else:
        return False

#Function that checks for a yes or no input
def yes_no_input():
    while True:
        userInput = input().upper()
        if userInput in ['YES', "Y", "1", "NO", "N", "0"]:
            return userInput
        else:
            print("Invalid input. Please enter yes or no: ")

#Project title
projectName = input("Project name: ")

masterPath = Path(workingPath) / projectName
shotsPath = Path(masterPath) / "SHOTS"

#__TESTING
print(f"master path is: {masterPath}")

#Check if that project folder already exists
while folderCheck(masterPath) == True:
    print(f"The {projectName} folder already exists.")
    projectName = input("Please chooses a different name: ")
    masterPath = Path(workingPath) / projectName

#__TESTING
print(f"Folder exists? {folderCheck(masterPath)}")

masterPath.mkdir()
shotsPath.mkdir()
print(f"{masterPath} folder created.")

#Create sequence folders
def makeSequenceFolders():
    sequenceCount = int(input("Number of sequences: "))

    while sequenceCount > 999:
        print("Please enter a 3 digit number only.")
        sequenceCount = int(input("Number of sequences: "))

    #__TESTING
    print(f"count is: {sequenceCount}")

    for seq in range(1, sequenceCount + 1):
        padAmount = f"{seq:03}"
        sequenceFolder = Path(shotsPath) / f"SEQ-{padAmount}"
        sequenceFolder.mkdir()
        print(f"{sequenceFolder} created.")

        #Create shot folders
        shot_count = int(input(f"Number of shots in SEQ-{padAmount}: "))

        for shot in range(1, shot_count + 1):
            shotPadding = f"{shot:04}"
            shotFolder = Path(shotsPath) / sequenceFolder / f"sh{shotPadding}"
            shotFolder.mkdir()
            print(f"{shotFolder} created.")

makeSequenceFolders()

#Generate globals
print("Create Globals folder? y/n")
globalsCheck = yes_no_input()
        
if globalsCheck == True:
    globalsFolder = Path(masterPath) / 'GLOBALS'
    globalsFolder.mkdir
    globals_cg_char = Path(globalsFolder) / 'cg' / 'char'
    globals_cg_char.mkdir(parents=True)
    globals_cg_env = Path(globalsFolder) / 'cg' / 'env'
    globals_cg_env.mkdir
    globals_cg_fx = Path(globalsFolder) / 'cg' / 'fx'
    globals_cg_fx.mkdir
    globals_cg_library = Path(globalsFolder) / 'cg' / 'library'
    globals_cg_library.mkdir
    globals_cg_prop = Path(globalsFolder) / 'cg' / 'prop'
    globals_cg_prop.mkdir
    globals_Dev = Path(globalsFolder) / 'Dev'
    globals_Dev.mkdir
    print("Globals folder created.")
    
else:
    print("Globals folder not created")

print("Generate Editorial folder?")
editorialCheck = yes_no_input()

if editorialCheck == True:
    globalsFolder = Path(masterPath) / 'EDITORIAL'
    globalsFolder.mkdir

else:
    print("Editorial folder not created")

input("Folders created. Press enter to finish.")