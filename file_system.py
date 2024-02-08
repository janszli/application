# Wite a python program that simulates a file system. It should support ls, mkdir, cd, and touch

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


class File:
    def __init__(self, name):
        self.name = name
        self.content = ''
        

class TerminalEmulator:
    def __init__(self):
        self.root = Directory('~')
        self.curr_dir = self.root
        self.path_name = '~'
    
    def change_path_name(self, backwards=False):
        """
        Used only for printing out each terminal command line
        E.G. 'user@cpst-host01:~$ >? touch file.txt'
        """
        if backwards:
            self.path_name = self.path_name.split(f'/{self.curr_dir.name}')[0]
        else:
            self.path_name += f'/{self.curr_dir.name}'
    
    def ls_command(self):
        pass
    
    def mkdir_command(self):
        pass
    
    def cd_command(self):
        pass
    
    def touch_command(self):
        pass
    
    def rm_command(self):
        pass
    
    def run(self):
        while True:
            user_input = input(f'user@cpst-host01:{self.path_name}$ ').strip().split()
            if not user_input:
                continue
            command = user_input[0]
            args = user_input[1:] if len(user_input) > 1 else None

            match command:
                case 'ls':
                    self.ls_command()
                case 'mkdir':
                    self.mkdir_command()
                case 'cd':
                    self.cd_command()
                case 'touch':
                    self.touch_command()
                case '':
                    continue
                case 'exit':
                    print('logout')
                    exit()
                case _:
                    print('test')


# =====================================================================================================================
if __name__ == "__main__":
    emu = TerminalEmulator()
    emu.run()

