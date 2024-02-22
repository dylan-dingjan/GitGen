```markdown
# GitGen

GitGen is a simple yet useful piece of code designed to make your university life a tiny bit easier by automating the organization, creation, and initialization of programming assignments.

## Overview

GitGen comes with two files: `GitGen-linux.py` and `GitGen-mac.py`, tailored for Linux and macOS respectively.

## Features

- **Organization**: GitGen organizes your programming assignments into folders based on your provided base location.
- **Creation**: It creates new assignments within designated course folders, with the option to add a remote git repository.
- **Initialization**: When creating a new assignment, GitGen always initializes an empty git repository. You'll be prompted to add a remote git, but this step is optional.
- **Quick Access**: GitGen enables faster access to assignments by opening a second terminal with the chosen assignment as the location.

## Usage

To run GitGen, follow these simple steps:

1. Open your terminal.
2. Navigate to the directory containing the GitGen file.
3. Use the following command to run GitGen on macOS:
   ```
   python3 GitGen-mac.py
   ```
   or on Linux:
   ```
   python3 GitGen-linux.py
   ```

4. Follow the on-screen prompts to organize, create, and access your programming assignments effortlessly.

## Example

Suppose your base location for all courses and assignments is `/Users/username/Documents/University`. Running GitGen will create course folders with the prefix `()` within this directory. For instance:

- `(/CSE101)` for the Computer Science course.
- `(/MATH201)` for the Mathematics course.

Within each course folder, GitGen will create assignments. For instance:

- `(/CSE101/Assignment1)`
- `(/CSE101/Assignment2)`

## Note

Ensure Python 3 is installed on your system before running GitGen.
