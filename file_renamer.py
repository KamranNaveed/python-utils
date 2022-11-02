import os
folderPath = r''  # insert file path
fileNumber = 200


for filename in os.listdir(folderPath):
    split_tuple = os.path.splitext(filename)
    if split_tuple[1] == '.jpg':
        os.rename(folderPath + '\\' + filename, folderPath +
                  '\\' + "Image" + str(fileNumber) + ".jpg")
        fileNumber += 1
