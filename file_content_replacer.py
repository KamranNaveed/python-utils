import os
folderPath = r''  # Insert file path

for filename in os.listdir(folderPath):
    split_tuple = os.path.splitext(filename)
    if split_tuple[1] == '.txt':
        # Read in the file
        with open(filename, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('1 ', '0 ')

        # Write the file out again
        with open(filename, 'w') as file:
            file.write(filedata)
