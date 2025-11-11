import os
import re
import shutil
from pathlib import Path
import typer
from typing_extensions import Annotated
app = typer.Typer()

def pwDir() -> str:
    return os.getcwd()


def InputValid(ctxStr: typer.Context, pram: typer.CallbackParam, value):
    if ctxStr.resilient_parsing:
        pass
    print(f"validating input parameter:{pram.name}")
    if re.search(r'[1-9?<>%$]+', value):
        raise typer.BadParameter("it's not valid string")
    return value


def createPath(path: str):
    return os.makedirs(path)


def createFile(fileName: str, path: str, context: str):
    paths = os.path.join(pwDir(), path, fileName)
    with open(paths, mode='w+') as f:
        f.write(context)
        f.writelines('\n')


def removeFile(fileName: str, path: str):
    if Path(os.path.join(pwDir(), path)).exists():
        os.remove(os.path.join(pwDir(), path, fileName))


def deterPath(path: str):
    if Path(os.path.join(pwDir(), path)).exists():
        shutil.rmtree(path)
    else:
        raise typer.BadParameter("it's not valid path")


def deterEmptyPath(path: str):
    if Path(os.path.join(pwDir(), path)).exists():
        os.rmdir(path)
    else:
        raise typer.BadParameter("it's not valid path")
def versionCil(mask:bool):
    __version__=0.01
    if mask:
     ver=typer.style(text=f"the tool version is :{__version__}", fg=typer.colors.CYAN)
     typer.secho(ver)
     raise typer.Exit()



@app.command()
def main(Pwd: Annotated[bool, typer.Option("--pwd", '-P', help='see the working directory',
                                           prompt='see the working directory')],
         buildPath: Annotated[bool, typer.Option('--createdir', '-C',
                                                 help='create the new dir sure',
                                                 prompt='are your sure create new directory'
             , confirmation_prompt=True)],
         deletePath: Annotated[
             bool, typer.Option('--deterDir', '-D', help='delete the directory', prompt='are your sure delete directory'
                 , confirmation_prompt=True)],
         deleteEmptyPath: Annotated[bool, typer.Option('--deterEmptyDir', '-E', help='delete the empty '
                                                                                     'directory',
                                                       prompt='are your sure delete empty directory')],
         FileName: Annotated[str, typer.Option('--FileName', '-N', help='setting the file name',
                                               prompt='please enter you want to write file name'
                                               )],
         settingPath: Annotated[str, typer.Option('--settingPath', '-S', help='setting file path'
             , prompt="setting file path", callback=InputValid)],
         context: Annotated[str, typer.Option('--context', '-T', help='setting the path with you setting path',
                                              prompt='please enter you want to write context')],
         writeFile: Annotated[
             bool, typer.Option('--writeFile', '-W', help='write the file', prompt='are your sure write the file')],
         rmFile: Annotated[bool, typer.Option('--remove', '-R', help='are your sure remove the file', prompt=True)],
         version:Annotated[bool,typer.Option('--version','-v',help='see the version of the tool',prompt='see the version of the tool',
                                             callback=versionCil)]



         ):
    if Pwd:
        dirInfo = typer.style(text=f"{pwDir()}", fg=typer.colors.GREEN, italic=True, underline=True)
        typer.secho(dirInfo)
    else:
        print("not see working directory")
    if buildPath:
        create_path = typer.style(text=f"{settingPath}", fg=typer.colors.BLUE, italic=True, underline=True)
        typer.secho(create_path)
        createPath(settingPath)
    if deletePath:
        deterPath(settingPath)
        delPathNotice=typer.style(text='successfully to delete path',fg=typer.colors.GREEN,italic=True,underline=True)
        typer.secho(delPathNotice)
    if deleteEmptyPath:
        delEmptyPathNotice = typer.style(text='successfully to delete empty directory', fg=typer.colors.GREEN, italic=True,underline=True)
        deterEmptyPath(settingPath)
        typer.secho(delEmptyPathNotice)
    if writeFile:
        writeNotice = typer.style(text='successfully to write context', fg=typer.colors.GREEN, italic=True, underline=True)
        createFile(fileName=FileName, path=settingPath, context=context)
        typer.secho(writeNotice)

    if rmFile:
        rmNotice = typer.style(text='successfully to delete remove file ', fg=typer.colors.GREEN,italic=True, underline=True)
        typer.secho(rmNotice)
        removeFile(fileName=FileName, path=settingPath)
    elif version:
        pass
    endingTool=typer.style(text="ending to the is tool",fg=typer.colors.GREEN,italic=True, underline=True)
    typer.secho(endingTool)


if __name__ == "__main__":
    app()
