# Write a python program that simulates a file system. It should support ls, mkdir, cd, and touch

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.content = {}

    def add_data(self, name, is_directory):
        if is_directory:
            if name not in self.content:
                self.content[name] = Directory(name, self)
            else:
                print(f"mkdir: cannot create directory '{name}': File exists")
        else:
            if name not in self.content:
                self.content[name] = File(name)  # else do nothing
            else:
                print(f"touch: cannot create file '{name}': File exists")

    def remove_data(self, name, toggle_directory=False):
        if name in self.content:
            if isinstance(self.content[name], Directory):
                if not toggle_directory:
                    print(f"rm: cannot remove '{name}': Is a directory")
                    return
                elif self.content[name].content:
                    print(f"rm: cannot remove '{name}': Directory not empty")
                    return
            del self.content[name]  # -d is toggled or is a file
        else:
            print(f"rm: cannot remove '{name}': No such file or directory")

    def list_content(self):
        return list(self.content.keys())


class File:
    def __init__(self, name):
        self.name = name
        self.content = ''


class TerminalEmulator:
    def __init__(self):
        self.root = Directory('~')
        self.curr_dir = self.root
        self.path_name = '~'

    def change_path_name(self, up=False):
        """
        Used only for printing out each terminal command line
        E.G. 'user@cpst-host01:~$ >? touch file.txt'
        """
        if up:
            self.path_name = self.path_name.split(f'/{self.curr_dir.name}')[0]
        else:
            self.path_name += f'/{self.curr_dir.name}'

    def return_to_root(self):
        """
        Used only to return to root directory under command 'cd ~' or 'cd /'
        """
        while self.curr_dir.parent is not None:
            self.change_path_name(True)
            self.curr_dir = self.curr_dir.parent

    def ls_command(self, args):
        """
        ls command - list content of current directory or one or more child directories
        Limitations: Only lists current directory or 1 level down of directories within current directory
        """
        if args is None:
            print('  '.join(sorted(self.curr_dir.list_content())))
        else:
            for dir_name in args:
                if dir_name in self.curr_dir.content and isinstance(self.curr_dir.content[dir_name], Directory):
                    print('  '.join(sorted(self.curr_dir.content[dir_name].list_content())))
                elif dir_name in self.curr_dir.content and isinstance(self.curr_dir.content[dir_name], File):
                    print(dir_name)
                else:
                    print(f"ls: cannot access '{dir_name}': No such file or directory")
        # else retrieve list_content of directory specified without changing directory?

    def mkdir_command(self, args):
        """
        mkdir command - make one or multiple directories
        Limitations: only creates directories in current directory
        """
        if args is None:  # No directory name is given
            print('mkdir: missing operand')
            return

        for dir_name in args:
            self.curr_dir.add_data(dir_name, is_directory=True)

    def cd_command(self, args):
        """
        cd command - change current directory
        Limitations: only changes to parent directory or 1 level down child directory
        """
        if args is None:  # no directory is passed
            return

        if len(args) > 1:  # mimics command line when too many arguments are input
            print('-bash: cd: too many arguments')
            return
        else:
            path = args[0]

        if path == '..':  # move upwards in directory
            if self.curr_dir.parent is not None:
                self.change_path_name(True)
                self.curr_dir = self.curr_dir.parent
        elif path == '~' or path == '/':  # change to root
            self.return_to_root()
        elif path in self.curr_dir.content and isinstance(self.curr_dir.content[path], Directory):  # is a directory
            self.curr_dir = self.curr_dir.content[path]
            self.change_path_name()
        else:
            print(f"-bash: cd: {path}: No such file or directory")

    def touch_command(self, args):
        """
        touch command - create one or multiple files
        Limitations: Only creates files in current directory
        """
        if args is None:  # no file name is passed
            print('touch: missing file operand')
            return

        for file_name in args:
            self.curr_dir.add_data(file_name, is_directory=False)

    def rm_command(self, args):
        """
        Bonus! rm command - delete a file or a directory
        Limitations: Does not delete non-empty directories
        """
        if args is None:  # no names are passed
            print('rm: missing operand')
            return

        if args[0].startswith('-') and args[0] != '-d' and len(args[0]) > 1:  # specific fail case when option != '-d'
            string_split = [i for i in args[0]]
            if string_split[1] == 'd':
                print(f"rm: invalid option -- '{string_split[2]}'")
            else:
                print(f"rm: invalid option -- '{string_split[1]}'")
            return

        if args[0] != '-d':  # when -d is not specified
            toggle = False
        elif args[0] == '-d' and len(args) == 1:  # -d command but no names are passed
            print('rm: missing operand')
            return
        else:
            args = args[1:]
            toggle = True  # -d to remove directories

        for name in args:
            self.curr_dir.remove_data(name, toggle)

    def run(self):
        while True:
            user_input = input(f'user@cpst-host01:{self.path_name}$ ').strip().split()
            if not user_input:
                continue
            command = user_input[0]
            args = user_input[1:] if len(user_input) > 1 else None

            match command:
                case 'ls':
                    self.ls_command(args)
                case 'mkdir':
                    self.mkdir_command(args)
                case 'cd':
                    self.cd_command(args)
                case 'touch':
                    self.touch_command(args)
                case 'rm':
                    self.rm_command(args)
                case 'exit':
                    print('logout')
                    exit()
                case _:
                    print(f"-bash: {command}: command not found")


# =====================================================================================================================
if __name__ == "__main__":
    emu = TerminalEmulator()
    emu.run()

