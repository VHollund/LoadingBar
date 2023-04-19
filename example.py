from loadingBar import LoadingBar
import time

if __name__ == '__main__':
    k=LoadingBar(20, fill=" ", color="bgGreen", emptycolor="bgRed", start="{", end="}")
    starttime=time.time()
    for x in range(0, 101):
        k.LoadingBar(x)
        time.sleep(0.1)
    print("Time elapsed: " + str(time.time()-starttime))