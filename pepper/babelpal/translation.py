import naoqi

if __name__ == "__main__":
    print("hello")
    URL_START = "192.168.122.1:8080/start?language=de"
    result = urllib.request.urlopen(URL_START)
    print(result.read())
    URL_STOP = "192.168.122.1:8080/stop?language=ed"
    result = urllib.request.urlopen(URL_STOP)
