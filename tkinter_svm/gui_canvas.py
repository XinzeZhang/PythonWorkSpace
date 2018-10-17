import tkinter as tk
import random
import numpy as np


class PointsClassification:
    def __init__(self):
        self.blueSet = []
        self.greenSet = []
        # self.trainSet=[]
        # self.testSet=[]

        window = tk.Tk()
        window.title('2-Class Points Classification')
        # window.geometry('600x600')

        # create a menu bar for choosing kernels
        menubar = tk.Menu(window)
        # create a pull-down menu, and add it to the menu bar
        kernelsMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Kernels", menu=kernelsMenu)
        kernelsMenu.add_command(label="Linear", command=self.test)
        kernelsMenu.add_command(label="demo1", command=self.test)
        kernelsMenu.add_command(label="demo2", command=self.test)
        kernelsMenu.add_command(label="demo3", command=self.test)
        kernelsMenu.add_command(label="demo4", command=self.test)

        # create more pull-down menus
        operationMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operation", menu=operationMenu)
        operationMenu.add_command(label="Predict", command=self.predict)
        operationMenu.add_separator()
        operationMenu.add_command(label="Quit", command=window.quit)
        window.config(menu=menubar)  # display the menu

        self.canvas = tk.Canvas(window, bg='white', height=500, width=500)
        self.canvas.create_line(
            0, 250, 500, 250, tags="horizontal", fill="gray", dash=(5, 5))
        self.canvas.create_line(
            250, 0, 250, 500, tags="vertical", fill="gray", dash=(5, 5))
        self.canvas.pack()

        # create start and end points button
        frame_bt = tk.Frame(window)
        frame_bt.pack()
        self.pointingStatue = False
        start_in = tk.Button(frame_bt, text="Start Points",
                             command=self.start_points)
        end_in = tk.Button(frame_bt, text="End Points",
                           command=self.end_points)
        # create label radio button
        self.pointsLabel = tk.IntVar()
        self.greenPoints = tk.Radiobutton(frame_bt, text="blue", foreground="blue",
                                          variable=self.pointsLabel, value=1, state="disabled", command=self.test)
        self.redPoints = tk.Radiobutton(frame_bt, text="red", foreground="red",
                                        variable=self.pointsLabel, value=-1, state="disabled", command=self.test)
        start_in.grid(row=1, column=1)
        end_in.grid(row=1, column=2)
        self.greenPoints.grid(row=1, column=3)
        self.redPoints.grid(row=1, column=4)

        self.canvas.bind("<Button 1>", self.printCoords)

        window.mainloop()

    def start_points(self):
        self.greenPoints.config(state="active")
        self.redPoints.config(state="active")
        self.greenPoints.select()
        self.pointingStatue = True

    def end_points(self):
        self.greenPoints.deselect()
        self.greenPoints.config(state="disabled")
        self.redPoints.deselect()
        self.redPoints.config(state="disabled")
        self.pointingStatue = False
        # print(self.dataset)

    def test(self):
        print(self.pointsLabel.get())

    def printCoords(self, event):
        try:
            # there will be a _tkinter.TclError: expected floating-point number but got "" without try/except
            if self.pointingStatue:
                if self.pointsLabel.get() == 1:
                    print("label = blue")
                    self.canvas.create_text(
                        event.x, event.y, text='*', fill="blue")
                    self.canvas.pack()
                    self.blueSet.append(
                        [event.x, event.y, self.pointsLabel.get()])
                elif self.pointsLabel.get() == -1:
                    print("label = red")
                    self.canvas.create_text(
                        event.x, event.y, text='*', fill="red")
                    self.canvas.pack()
                    self.greenSet.append(
                        [event.x, event.y, self.pointsLabel.get()])
        except:
            pass
        # output the x and y coords to terminal
        print(event.x, event.y)

    def getDataset(self):
        # random shuffling
        def randomShuffling(lists):
            matrix = lists
            for row in range(len(matrix)):
                i = random.randint(0, len(matrix)-1)
                # swap the matrix with matrix
                matrix[row], matrix[i] = matrix[i], matrix[row]
            return matrix

        print(self.blueSet)
        self.blueSet = randomShuffling(self.blueSet)
        blueArray = np.array(self.blueSet)
        blueTrainNum = len(self.blueSet)*0.8
        blueTraining = blueArray[:blueTrainNum, :]
        blueTest = blueArray[blueTrainNum:, :]
        print(self.blueSet)

        self.greenSet = randomShuffling(self.greenSet)
        greenArray = np.array(self.greenSet)
        greenTrainNum = len(self.greenSet)*0.8
        greenTraining = greenArray[:greenTrainNum, :]
        greenTest = greenArray[greenTrainNum:, :]

        trainSet = np.concatenate((blueTraining,greenTraining),axis = 0)
        testSet = np.concatenate((blueTest,greenTest),axis = 0)

        return trainSet, testSet
    
    def predict(self):
        trainSet, testSet = self.getDataset()


PointsClassification()
