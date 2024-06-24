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
        userInput = input()
        userInput = userInput.upper()
        if userInput in ["YES", "Y", "1", "NO", "N", "0"]:
            if userInput in ["YES", "Y", "1",]:
                return True
            else:
                return False
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
print(f"{masterPath} folder created.")

#Function to create sequence folders
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
            shotFolder_cg = Path(shotFolder) / 'cg'
            shotFolder_cg.mkdir()
            shotFolder_comp_script = Path(shotFolder) / 'comp' / 'script'
            shotFolder_comp_script.mkdir(parents=True)
            shotFolder_comp_write = Path(shotFolder) / 'comp' / 'write'
            shotFolder_comp_write.mkdir()
            shotFolder_ingest = Path(shotFolder) / 'ingest'
            shotFolder_ingest.mkdir()
            shotFolder_lighting = Path(shotFolder) / 'lighting'
            shotFolder_lighting.mkdir()
            shotFolder_plate = Path(shotFolder) / 'plate'
            shotFolder_plate.mkdir()
            shotFolder_rotoPaint = Path(shotFolder) / 'rotoPaint'
            shotFolder_rotoPaint.mkdir()
            print(f"{shotFolder} created.")

#Create SHOTS folders
print("Create Shots folder?")
shotsCheck = yes_no_input()

if shotsCheck == True:
    shotsPath.mkdir()
    makeSequenceFolders()
else:
    print("Shots folder not created.")

#Generate globals
print("Create Globals folder? y/n")
globalsCheck = yes_no_input()
        
if globalsCheck == True:
    globalsFolder = Path(masterPath) / 'GLOBALS'
    globalsFolder.mkdir()
    globals_cg_char = Path(globalsFolder) / 'cg' / 'char'
    globals_cg_char.mkdir(parents=True)
    globals_cg_env = Path(globalsFolder) / 'cg' / 'env'
    globals_cg_env.mkdir()
    globals_cg_fx = Path(globalsFolder) / 'cg' / 'fx'
    globals_cg_fx.mkdir()
    globals_cg_library_HDRI = Path(globalsFolder) / 'cg' / 'library' / 'HDRI'
    globals_cg_library_HDRI.mkdir(parents=True)
    globals_cg_library_textures = Path(globalsFolder) / 'cg' / 'library' / 'textures'
    globals_cg_library_textures.mkdir()
    globals_cg_prop = Path(globalsFolder) / 'cg' / 'prop'
    globals_cg_prop.mkdir()
    globals_Dev = Path(globalsFolder) / 'Dev'
    globals_Dev.mkdir()
    print("Globals folder created.")
    
else:
    print("Globals folder not created")

print("Generate Editorial folder?")
editorialCheck = yes_no_input()

if editorialCheck == True:
    editorialFolder = Path(masterPath) / 'EDITORIAL'
    editorialFolder.mkdir()
    editorialFolder_audio_music = Path(editorialFolder) / 'audio' / 'music'
    editorialFolder_audio_music.mkdir(parents=True)
    editorialFolder_audio_sfx = Path(editorialFolder) / 'audio' / 'sfx'
    editorialFolder_audio_sfx.mkdir()
    editorialFolder_audio_vo = Path(editorialFolder) / 'audio' / 'vo'
    editorialFolder_audio_vo.mkdir()
    editorialFolder_DELIVERY = Path(editorialFolder) / 'DELIVERY'
    editorialFolder_DELIVERY.mkdir()
    editorialFolder_footage = Path(editorialFolder) / 'footage'
    editorialFolder_footage.mkdir()
    editorialFolder_Resolve = Path(editorialFolder) / 'Resolve'
    editorialFolder_Resolve.mkdir()

else:
    print("Editorial folder not created")

input("Task complete. Press enter to finish.")