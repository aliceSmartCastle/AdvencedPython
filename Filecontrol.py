import os
import re
import shutil
from pathlib import Path
import typer
from typing_extensions import Annotated

app = typer.Typer(rich_markup_mode="markdown", help="the simple file manager")


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
        print('you is successfully delete the path')
    else:
        raise typer.BadParameter("it's not valid path")


def deterEmptyPath(path: str):
    if Path(os.path.join(pwDir(), path)).exists():
        os.rmdir(path)
    else:
        raise typer.BadParameter("it's not valid path")


def versionCil(mask: bool):
    __version__ = 0.01
    if mask:
        ver = typer.style(text=f"the tool version is :{__version__}", fg=typer.colors.CYAN)
        typer.secho(ver)
        raise typer.Exit()


@app.command(help='output the user working directory', rich_help_panel='working units')
def PwdWatch(Pwd: Annotated[bool, typer.Option("--pwd", '-p', help='see the working directory',
                                               prompt="see the working directory'")]):
    """
    [bold green]check[/bold green] use working directory
    """
    if Pwd:
        dirInfo = typer.style(text=f"{pwDir()}", fg=typer.colors.GREEN, italic=True, underline=True)
        typer.secho(dirInfo)
    else:
        emptyNotice = typer.style(text=f"not see working directory", fg=typer.colors.RED, italic=True, underline=True)
        typer.secho(emptyNotice)


@app.command(help='delete the no empty directory path', rich_help_panel='file config units')
def DeletePath(pathDetail: Annotated[
    bool, typer.Option('--deterDir', '-D', help='delete the directory', prompt='are your sure delete path',
                       confirmation_prompt=True)],
               settingPath: Annotated[str, typer.Option('--settingPath', '-S', help='setting file path',
                                                        prompt="setting file path", callback=InputValid)], ):
    """
    ** pathDetail:the bool argument ,if it's ture it will delete the path in your computer
     * settingPath: the string argument if deletePath is sure it can run to create you input the path
     ,else your input any data is no valid
    """
    if pathDetail:
        deterPath(settingPath)
        #delPathNotice = typer.style(text='successfully to delete path', fg=typer.colors.GREEN, italic=True,underline=True)
        #typer.secho(delPathNotice)
    else:
        noDeletePath=typer.style(text=f"you can not delete the path", fg=typer.colors.RED, underline=True)
        typer.secho(noDeletePath)


@app.command(help='create the new path', rich_help_panel='file config units')
def BuildPath(buildPath: Annotated[bool, typer.Option('--createdir', '-C',
                                                      help='create the new dir',
                                                      prompt='please enter a valid path',
                                                      confirmation_prompt=True)],
              settingPath: Annotated[
                  str, typer.Option('--settingPath', '-S', help='setting file path',
                                    prompt="if is not buildPath,this input is not valid",
                                    callback=InputValid)]):
    """
    ** BuildPath:the bool argument ,if it's ture it will build the path in your computer
    *  settingPath: is same to the DeletePath function doc\n

    """
    if buildPath:
        create_path = typer.style(text=f"{settingPath}", fg=typer.colors.BLUE, italic=True, underline=True)
        typer.secho(create_path)
        createPath(settingPath)
    else:
        noBuild = typer.style(text=f"you can not create the new path ", fg=typer.colors.RED, underline=True)
        typer.secho(noBuild)


@app.command(help='delete the empty file path', rich_help_panel='file config units')
def DeleteEmptyPath(
        deletePath: Annotated[bool, typer.Option('--deterEmptyDir', '-E', help='delete the empty '
                                                                               'directory',
                                                 prompt='please enter the path')],

        settingPath: Annotated[
            str, typer.Option('--settingPath', '-S', help='setting file path', prompt="setting file path",
                              callback=InputValid)]

):
    """
      deletePath : the bool argument,is your sure,it can delete your enter the empty path
      ,else is false,it can not do anything\n
    settingPath: is same to the BuildPath function doc\n
    """
    if deletePath:
        delEmptyPathNotice = typer.style(text='successfully to delete empty directory', fg=typer.colors.GREEN,
                                         italic=True, underline=True)
        deterEmptyPath(settingPath)
        typer.secho(delEmptyPathNotice)


@app.command(help='write data to new file on the path', rich_help_panel='file config units')
def WriteFile(
        FileName: Annotated[str, typer.Option('--FileName', '-N', help='setting the file name',
                                              prompt='please enter you want to write file name'
                                              )],

        context: Annotated[str, typer.Option('--context', '-T', help='setting the path with you setting path',
                                             prompt='please enter you want to write context')], settingPath: Annotated[
            str, typer.Option('--settingPath', '-S', help='setting file path', prompt="setting file path",
                              callback=InputValid)],
        writeFile: Annotated[
            bool, typer.Option('--writeFile', '-W', help='write the file', prompt='are your sure write the file')]):
    """
     FileName:the named of your creation file
     context: write the context to the file
     writeFile:if it's true it will write the file to your computer
     else,it will not write the file
    """
    if writeFile:
        writeNotice = typer.style(text='successfully to write context', fg=typer.colors.GREEN, italic=True,
                                  underline=True)
        createFile(fileName=FileName, path=settingPath, context=context)
        typer.secho(writeNotice)


@app.command(help='remove the file on the path', rich_help_panel='file config units')
def RmFile(rmFile: Annotated[bool, typer.Option('--remove', '-R', help='are your sure remove the file', prompt=True)],
           FileName: Annotated[str, typer.Option('--FileName', '-N', help='setting the file name',
                                                 prompt='please enter you want to write file name'
                                                 )], settingPath: Annotated[
            str, typer.Option('--settingPath', '-S', help='setting file path', prompt="setting file path",
                              callback=InputValid)], ):
    """
    FileName:the named of your creation file
    settingPath: is same to the BuildPath function doc
    rmFile:if it's true it will remove the file to your computer,
    else,it will not remove the file
    """
    if rmFile:
        rmNotice = typer.style(text='successfully to delete remove file ', fg=typer.colors.GREEN, italic=True,
                               underline=True)
        typer.secho(rmNotice)
        removeFile(fileName=FileName, path=settingPath)


@app.command(help='see the tool the version', rich_help_panel='working units')
def toolVersion(

        version: Annotated[bool, typer.Option('--version', '-v', help='see the version of the tool',
                                              prompt='see the version of the tool',
                                              callback=versionCil)]

):
    if version:
        pass
    endingTool = typer.style(text="ending to the is tool", fg=typer.colors.GREEN, italic=True, underline=True)
    typer.secho(endingTool)


if __name__ == "__main__":
    app()
