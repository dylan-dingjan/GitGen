
# GitGen

GitGen is a simple yet useful piece of code designed to make your university life a tiny bit easier by automating the organization, creation, and initialization of programming assignments.

## Overview

GitGen comes with two files: `GitGen-linux.py` and `GitGen-mac.py`, tailored for Linux and macOS respectively.

## Features

- **Organization**: GitGen organizes your programming assignments into folders based on your provided base location.
- **Creation**: It creates new assignments within designated course folders, with the option to add a remote git repository.
- **Initialization**: When creating a new assignment, GitGen always initializes an empty git repository. You'll be prompted to add a remote git, but this step is optional.
- **Quick Access**: GitGen enables faster access to assignments by opening a second terminal with the chosen assignment as the location.

## Install GitGen

Create a new folder in which you will retrieve the git repository, then follow these steps:
1. Open the terminal in the folder you just created.
2. Start a git using: `git init`
3. Add the remote git using: `git remote add origin git@github.com:dylan-dingjan/GitGen.git`
4. Rename your current branch using: `git branch -m master main`
5. Pull the repository using: `git pull origin main`
6. Now you have all needed files!

To make it easier to start the script, you can put the python script in the folder at which the terminal starts. Don't forget to change the base_location to specify where the courses will be created

## Usage

To run GitGen, follow these simple steps:

1. Open your terminal.
2. Navigate to the directory containing the GitGen file.
3. Use the following command to run GitGen on macOS:

   `python3 GitGen-mac.py`

   or on Linux:

   `python3 GitGen-linux.py`


4. Follow the on-screen prompts to organize, create, and access your programming assignments effortlessly.

## Example

Suppose your base location for all courses and assignments is `/Users/username/Documents/University`. Running GitGen will create course folders with the prefix `()` within this directory. For instance:

- `/()CSE101` for the Computer Science course.
- `/()MATH201` for the Mathematics course.

Within each course folder, GitGen will create assignments. For instance:

- `/()CSE101/Assignment1`
- `/()CSE101/Assignment2`

## Note

Ensure Python 3 is installed on your system before running GitGen.
