import time


class Trafficlights:
    __color = ['красный', 'желтый', 'зеленый']
    timesleep = [7, 2, 8]
    cnt = 0

    def running(self):
        for i in Trafficlights.__color:
            print(i)
            time.sleep(Trafficlights.timesleep[Trafficlights.cnt])
            Trafficlights.cnt =Trafficlights.cnt + 1

tl = Trafficlights()
tl.running()
