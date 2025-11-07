import os.path
from threading import Thread, Lock, Event
from typing import List
from urllib.request import urlopen



def DownloaderFile(url: str, downEvent: Event) ->None:
    print(f"download from the the {url}")
    pngData = None
    with urlopen(url) as Png:
        pngData = Png.read()
    if not pngData:
        raise Exception(f"Error: could not download the image from {url}")
    FileName = os.path.basename(url)
    #PngName, _ = request.urlretrieve(url, FileName)
    downEvent.set()
    print("Waiting for the PngFile to be downloaded...")
    with open(os.path.join('pjskPng', FileName), 'wb+') as pngFile:
        pngFile.write(pngData)
        print(f"{FileName} is download...")
    print("file download is competed")
    downEvent.wait()


def main(urls:List[str]) ->None:
    if urls:
     #urls = ['https://images5.alphacoders.com/130/thumb-1920-1307586.png','https://images4.alphacoders.com/129/thumb-1920-1299815.png']
     pngLock = Lock()
     pngEvent = Event()
    # PngThread = Thread(target=DownloaderFile, args=(urls[0], pngEvent))
     multiThreadDownload = (Thread(target=DownloaderFile, args=(urls[i], pngEvent)) for i in range(len(urls)))
     finish_list = []
     with pngLock:
        for pngThread in multiThreadDownload:
            finish_list.append(pngThread)
            pngThread.start()
        for pngFinish in finish_list:
            pngFinish.join()
        print(f"all thread download picture successfully")
    else:print('not support empty list')


if __name__ == "__main__":
    urlList=['https://images7.alphacoders.com/129/thumb-1920-1290300.jpg','https://images4.alphacoders.com/127/thumb-1920-1279984.png']
    main(urls=urlList)
