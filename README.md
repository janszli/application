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
- `ls`
- `mkdir foo bar test`
- `touch file.txt`
- `cd foo`
- `mkdir cat`
- `touch foobar.txt`
- `ls`
- `cd ..`
- `ls`
