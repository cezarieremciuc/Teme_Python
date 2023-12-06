import sys
import os

def renameFiles(dirPath):
    updateList = []  
    startNumber
    
    try:
        if not os.path.exists(dirPath):
            raise FileNotFoundError(f"Incorrect path: {dirPath}")
        filesList = os.listdir(dirPath)
        filesList.sort()
        startNumber = 1
        for i, name in enumerate(filesList, startNumber):
            existingPath = os.path.join(dirPath, name)
            newName = f"file{i}{os.path.splitext(name)[1]}"
            newPath = os.path.join(dirPath, newName)

            updateList.append((existingPath, newPath))
            
            print(f"Updated file {name} to new name {newName}")         
        for existingPath, newPath in updateList:
            try:
                os.rename(existingPath, newPath)
            except Exception as e:
                print(str(e))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    dirPath = sys.argv[1]
    renameFiles(dirPath)
