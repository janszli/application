## CPST Assessment - File System Emulator

### How to use:
- Can be run locally on the terminal with `python file_system.py` if Python is installed. Should be able to run on py3.9+
- Alternatively, download the executable and run the program from there.

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
- Cannot `rm` files or directories

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
- `touch calico.txt tuxedo.txt tabby.txt orange.txt`
- `ls`
- `cd ~`
- `ls foo`
- `cd bar`
- `cd ..`
- `cd test`
- `cd /`
- `ls file.txt`

#### Bonus: rm command:
- `rm test`
- `rm -r`
- `rm -d`
- `rm -dt test`
- `rm - test`
- `rm -d test`
- `rm -d dog horse`
- `rm foo`
- `ls`
- `cd foo`
- `rm -d kitten foobar.txt`
- `ls`
- `cd cat`
- `rm orange.txt tuxedo.txt`
- `ls`

#### Cases to test errors :
- `ls blathers`
- `mkdir`
- `cd`
- `cd test touch`
- `touch`
- `random`
- `do as i say`
- `exit`
