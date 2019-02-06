from graphics import *


    class Hand(Line):
         def __init__(self):
            Line.__init__(self, Point(250, 250), Point(250, 250))
            self.value = 0
            self.max_value = 60
            self.color = 'black'



    def draw(self, win):
        self.hand.draw(win)


    class HourHand(Hand):
        def __init__(self):
            Hand.__init__(self)
            self.max_value = 12

    class MinuteHand(Hand):


    class SecondHand(Hand):
        def __init__(self):
            Hand.__init__(self)
            self.color = 'red'


    pass


class Analog():

    def __init__(self):
        self.win = None
        self.face = Circle(Point(250, 250), 200)
        self.face.setFill('lightgray')
        self.face.setWidth(5)
        self.hour_hand = HourHand()
        self.minute_hand = MinuteHand()
        self.second_hand = SecondHand()


    def draw(self, win):
        self.win = win
        self.face.draw(win)
        # self.hour_hand.draw(win)
        # self.minute_hand.draw(win)
        # self.second_hand .draw(win)

    def animate(self):
        self.win.after(250, self.animate)

if __name__== "__main__":
    clock  = analog()

    win = GraphWin('Clock', 500, 500)
    clock.draw(win)
    clock.animate
    win.mainloop()