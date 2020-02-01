import sys
import argparse
import time
import os
from subprocess import Popen,PIPE,STDOUT


def get_parser():
    parser = argparse.ArgumentParser(description='Test Runner')
    parser.add_argument("-git",type=str)
    parser.add_argument("-file",type=str)
    return parser.parse_args()


def git_clone(git_url,location):
    command = str.format("git clone --branch=master --progress -v {0} {1}",
        git_url,
        location)
    exec_command([command])


def exec_command(commands:list):
    """
    list of command to execute
    """
    for command in commands:
        process = Popen(command,
                        shell=True,
                        stdin=PIPE,
                        stdout=PIPE,
                        stderr=STDOUT)
        output, errors = process.communicate()
        if errors:
            print(errors)    
        if output:
            print(output) 

def file_exist(location):
	return os.path.isfile(location)

if __name__=="__main__":
    
    git_dir = "/opt/source/project"
    
    parser = get_parser()

    git_url = parser.git

    exec_file = parser.file
    
    print("GIT URL:"+git_url)
    
    git_clone(git_url,git_dir)
    
    requirements_location = git_dir+"/requirements.txt"
    
    if file_exist(requirements_location):
        print("Using Requirement File At:"+requirements_location)
        command = str.format("{0} {1}","pip install -r",requirements_location)
        exec_command([command])

    exec_location = git_dir+"/"+exec_file

    if file_exist(exec_location):
        print("Running:"+exec_location)
        command = str.format("python {0}",exec_location)
        exec_command([command])