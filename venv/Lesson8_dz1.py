import time


class Trafic_light:
    color_list = ['\033[41m{}', '\033[43m{}', '\033[42m{}']
    __color = '\033[41m{}'

    def running(self):
        x_t = 7
        for col in Trafic_light.color_list:
            print('{}'.format(col), end='')
            time.sleep(x_t)
            x_t = 2


a = Trafic_light()
a.running()
