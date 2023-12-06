import sys
import os

def readDirFiles(dirPath, ext):
    try:
        if not os.path.exists(dirPath):
            raise FileNotFoundError(f"Incorrect path: {dirPath}")

        for filename in os.listdir(dirPath):
            if filename.endswith(ext):
                file_path = os.path.join(dirPath, filename)
                try:
                    file = open(file_path, 'r')
                    content = file.read()
                    print(f"Filename: {filename}\ntext:\n{content}\n")
                except Exception as e:
                    print(str(e))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    dirPath = sys.argv[1]
    ext = sys.argv[2]
    readDirFiles(dirPath, ext)
