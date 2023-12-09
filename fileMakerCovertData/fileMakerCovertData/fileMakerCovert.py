import os
import random
import time
import shutil
import logging
import subprocess

#logging.basicConfig(filename='logfile.txt', level=logging.INFO, 
#                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


directories = ['./dir1', './dir2', './dir3', './dir4','./dir5', './dir6', './dir7', './dir8', './dir9', './dir10']
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
    #logging.info(f"Directory created: {directory}")
# Function to randomly create, modify, or delete a file
def executeCovertChannel():
    subprocess.Popen(["python3", f'{os.getcwd()}/covert/coverta.py'], cwd = f'{os.getcwd()}/covert')
    time.sleep(0.5)
    subprocess.Popen(["python3", f'{os.getcwd()}/covert/covertb.py'],cwd = f'{os.getcwd()}/covert')
def random_file_operation(directory):
    filename = os.path.join(directory, f"file_{random.randint(1, 10000)}.txt")
    if os.path.exists(filename):
        operation = random.choice(['modify', 'delete'])
    else:
        operation = random.choice(['create', 'modify', 'delete'])

    if operation == 'create':
        with open(filename, 'w') as f:
            f.write("Hello, World!")
        #logging.info(f"File created: {filename}")
    elif operation == 'modify' and os.path.exists(filename):
        with open(filename, 'a') as f:
            f.write("\nModified!")
        #logging.info(f"File modified: {filename}")
    elif operation == 'delete' and os.path.exists(filename):
        os.remove(filename)
        #logging.info(f"File deleted: {filename}")

    return operation, filename
stop = random.randint(2000,8000)
print(stop)
for i in range(10000):
    if i == stop:
        executeCovertChannel()
    directory = random.choice(directories)
    operation, filename = random_file_operation(directory)

    # Wait a bit for inotify to catch up
    time.sleep(0.1)

    # Read and process events




for i in range(1,len(directories)+1):
    path_to_directory = "./dir" + str(i)
    try:
        shutil.rmtree(path_to_directory)
        logging.info(f"Directory removed: {path_to_directory}")
        print(f"The directory {path_to_directory} has been removed")
    except OSError as error:
        logging.info(f"Error removing {path_to_directory}")
        print(f"Error: {error.strerror}. The directory {path_to_directory} was not removed.")
