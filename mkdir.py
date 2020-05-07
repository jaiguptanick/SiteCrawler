import os

def create_dir(directory):    #to create a dir for each site
    if not os.path.exists(directory): #to check if dir already exist
        os.makedirs(directory)

def write_file(path, data):   #fxn to write data in the file
    f = open(path, 'w')
    f.write(data)
    f.close()