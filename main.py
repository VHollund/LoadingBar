class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class LoadingBar:
    def __init__(self, width=10, fill="█"):
        self.width = width
        self.fill = fill
        self.multiplier = 100/width

    def LoadingBar(self, percent):
        content = "[" + bcolors.OKGREEN
        for i in range(0, self.width):
            if i*self.multiplier < percent:
                content += self.fill
            else:
                content += " "
        content += bcolors.ENDC + "]" + str(percent) + "%"
        print(content, end="\r")
        if percent == 100:
            print()


if __name__ == '__main__':
    k=LoadingBar(20, "█")
    for x in range(0, 101):
        k.LoadingBar(x)
