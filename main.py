from ffmpeg import FFmpeg
from sys import argv

def splice(name, start, end):
    command = (
        FFmpeg()
        .option("ss", start)
        .option("to", end)
        .input(argv[2])
        .output(name+".mp3")
    )
    command.execute()

def main():
    if len(argv) < 3:
        print("Please specify timestamps file and audio file")
        return
    with open(argv[1], "r") as timestampsfile:
        name = ""
        prevTime = ""
        for line in timestampsfile.read().splitlines():
            time = line.split()[0]
            if name != "":
                splice(name, prevTime, time)
            prevTime = time
            name = " ".join(line.split()[1:])
        
        



if __name__ == '__main__':
    main()
