import os.path
import shutil
from enum import Enum, auto


class DesktopEnum(Enum):
    StartupWMClass = auto()
    Version = auto()
    Name = auto()
    Type = auto()
    Categories = auto()
    Exec = auto()
    Icon = auto()
    Path = auto()
    Comment = auto()
    Terminal = auto()
    StartupNotify = auto()


class CreateDesktop:
    def __init__(self, StartupWMClass: str, Version: int = 1.0, Name: str = '', Type: str = "Application"
                 , Categories: str = 'Utility', Exec: str = '', Icon: str = '', Path: str = os.getcwd(),
                 Comment: str = '',
                 Terminal: bool = False, StartupNotify: bool = True):
        self.desktop_element = "[Desktop Entry]"
        self.StartupWMClass = StartupWMClass
        self.Names = Name
        self.Version = Version
        self.Type = Type
        self.Categories = Categories
        self.Exec = Exec
        self.Icon = Icon
        self.Path = Path
        self.Comment = Comment
        self.Terminal = Terminal
        self.StartupNotify = StartupNotify
        self.python_loc = '/usr/bin/python3.13'

    def write_desktop(self):
        """
        create the desktop file
        """
        with open(os.path.join(os.getcwd(), self.StartupWMClass + '.desktop'), mode='w+') as desk:
            desk.writelines(self.desktop_element)
            desk.writelines(f"\n{DesktopEnum.StartupWMClass.name}={self.StartupWMClass}")
            desk.writelines(f"\n{DesktopEnum.Version.name}={self.Version}")
            desk.writelines(f"\n{DesktopEnum.Name.name}={self.Names}")
            desk.writelines(f"\n{DesktopEnum.Type.name}={self.Type}")
            desk.writelines(f"\n{DesktopEnum.Path.name}={self.Path}")
            desk.writelines(f"\n{DesktopEnum.Categories.name}={self.Categories}")
            desk.writelines(f"\n{DesktopEnum.Exec.name}={self.python_loc + ' ' + self.Exec}")
            desk.writelines(f"\n{DesktopEnum.Icon.name}={self.Icon}")
            desk.writelines(f"\n{DesktopEnum.Comment.name}={self.Comment}")
            desk.writelines(f"\n{DesktopEnum.Terminal.name}={str(self.Terminal).lower()}")
            desk.writelines(f"\n{DesktopEnum.StartupNotify.name}={str(self.StartupNotify).lower()}")

    @staticmethod
    def path_local(filename, AppPath):
        """
        move the icon work path
        """
        shutil.move(os.path.join(os.getcwd(), filename), AppPath)


if __name__ == "__main__":
    main_path = os.path.join("/", "home", "istarnight", ".local", "share", "applications")
    IconPath = os.path.join(os.getcwd(), "Icon", "bird-scepter.png")
    # desk_filepath = os.path.join("dockDesktop", "IconTest.desktop")
    DeskTest = CreateDesktop(StartupWMClass="IconSet", Name="IconSet",
                             Exec=os.path.join(os.getcwd(), "Iconfinish.py"),
                             Icon=IconPath, Comment="test finally file")
    DeskTest.write_desktop()
    DeskTest.path_local(filename="IconSet.desktop", AppPath=main_path)
