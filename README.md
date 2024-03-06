## Check Point's Take Home Assessment - File System Emulator

### How to use:
- Option 1: Run the `file_system.py` file locally with `python file_system.py` if Python 3 is installed. Python can be installed here: https://www.python.org/downloads/ or using homebrew
- Option 2: Run the executable `file_system.exe` on a Windows device.

### Functionality:
- Can handle ls, mkdir, cd, touch
- Can create multiple directories on a single command
- Can create multiple files on a single command
- Can use `cd ..` as well as `cd ~` and `cd /`
- Mimics terminal with Username `user` on host `cpst-host01`

### Limitations:
- Cannot handle parent directories in the commands. E.g `ls foo/bar parent/child/node` or `mkdir foo/bar`
- Cannot change to a separate directory when already in another directory. Needs to return to root first.
- Does not have content in files or ability to add content to files

-----

 ### Test Cases:
- `mkdir child`
- `ls`
- `mkdir foo bar test dog horse`
- `ls`
- `touch file.txt`
- `ls`
- `cd foo`
- `mkdir cat kitten`
- `touch foobar.txt`
- `ls`
- `cd cat`
- `touch calico.txt tuxedo.md tabby.txt orange.yaml`
- `ls`
- `cd ~`
- `ls foo`
- `cd bar`
- `cd ..`
- `cd test`
- `cd /`
- `ls file.txt`

#### Cases to test errors :
- `ls blathers`
- `mkdir`
- `cd`
- `cd test touch`
- `touch`
- `random`
- `do as i say`

#### BONUS: rm command:
- `rm test`
- `rm -r`
- `rm -d`
- `rm -dt test`
- `rm - test`
- `rm -d test`
- `rm -d dog horse`
- `rm -d foo`
- `ls`
- `cd foo`
- `rm -d kitten foobar.txt`
- `ls`
- `cd cat`
- `rm orange.yaml tuxedo.md`
- `ls`

#### Exit
 - `exit`
