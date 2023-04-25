bcolors = {
    "HEADER": '\033[95m',
    "blue": '\033[94m',
    "cyan": '\033[96m',
    "green": '\033[92m',
    "red": '\033[91m',
    "yellow": '\033[93m',
    "fullGreen": '\033[1;32;40m',
    "fullRed": '\033[1;31;40m',
    "bgGreen": '\033[1;30;42m',
    "bgRed": '\033[1;30;41m',
    "bgGrey": '\033[6;30;47m',
    "bgBlue": '\033[1;30;44m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}

class LoadingBar:
    def __init__(self, width=10, fill="█", color="green", emptycolor="", start="", end=""):
        if color in bcolors.keys():
            self.color = bcolors[color]
        else:
            self.color = bcolors["green"]
        if emptycolor in bcolors.keys():
            self.emptycolor = bcolors[emptycolor]
        else:
            self.emptycolor = ""

        self.width = width
        self.fill = fill
        self.multiplier = 100/width
        self.start = start
        self.end = end

    def update(self, percent):
        content = self.start + self.color
        for i in range(0, self.width):
            if i*self.multiplier < percent:
                content += self.fill
            else:
                content += self.emptycolor + " " + bcolors["ENDC"] if self.emptycolor != "" else " "
        content += bcolors["ENDC"] + self.end + str(percent) + "%"
        print("\r", content, end="")
        if percent == 100:
            print()
