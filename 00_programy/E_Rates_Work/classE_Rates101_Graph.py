import time, sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import PIL
import PIL._tkinter_finder
from classE_Rates101_Data import Data
from classE_Rates101_Database import Scenario
import tkinter as tk
import numpy as np

class Graph:
    agr_number = 0
    
    def figSizeGet(self):
        if sys.platform == 'linux': 
            self.figSizeA = 8.75
        else:
            self.figSizeA = 8.25    
    
    def emptyGraph(self, root):
        self.figSizeGet()
        if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.fig = plt.figure(figsize=(self.figSizeA,7), facecolor = "dimgray") 
            plt.style.use('dark_background')
            self.axis = self.fig.add_subplot(111) 
            self.axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
        else:
            self.fig = plt.figure(figsize=(self.figSizeA,7), facecolor = "white")
            plt.style.use('Solarize_Light2')
            self.axis = self.fig.add_subplot(111) 
            self.axis.grid(linestyle="solid", color="white",  linewidth=0.4)
        
        self.axis.set_xlabel("Data") 
        self.axis.set_ylabel("PLN Złoty")
        self.fig.tight_layout()
        self.putGraph(root, 4, self.fig)
    
    def getVar(self, trendLineVar, annotateVar, oneSubplotVarMulti = None):
        self.a = annotateVar
        self.t = trendLineVar
        self.oneSubplotVarMulti = oneSubplotVarMulti
    
    def refreshGraph(self, root, timeRange, xValues, yValues, codeOne, codeCurrencyDict):
        plt.clf()
        plt.close(self.fig)
        
        if xValues == None:
            self.emptyGraph(root)
        else:
            if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
                self.fig = plt.figure(figsize=(self.figSizeA,7), facecolor = "dimgray")
                plt.style.use('dark_background')
                self.axis = self.fig.add_subplot(111) 
                self.axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
            else:
                self.fig = plt.figure(figsize=(self.figSizeA,7), facecolor = "white")
                plt.style.use('Solarize_Light2')
                self.axis = self.fig.add_subplot(111) 
                self.axis.grid(linestyle="solid", color="white",  linewidth=0.4)

            self.sumChVar = 0
            self.drawGraph(16, timeRange, xValues, yValues, codeOne, 1, codeCurrencyDict)
            self.fig.tight_layout()
            self.putGraph(root, 4, self.fig)
        
    def drawGraph(self, fontSize, tRange, xValues, yValues, codeMulti, oneOrMultiGraph, codeCurrencyDict, progressbar=None):
        xValuesLen = len(xValues)
        yRange = (max(yValues) - min(yValues)) * 0.09 
        self.timeRangeGet = tRange
        def trendline():
            x = np.array(range(len(xValues)))
            y = np.array(yValues)
            z = np.polyfit(x, y, 1)
            p = np.poly1d(z)
            if p(x)[0] > p(x)[-1]:
                plt.plot(x, p(x), color='orangered', linewidth=0.7)
            elif p(x)[0] == p(x)[-1]:
                plt.plot(x, p(x), color='grey', linewidth=0.7)
            else:
                plt.plot(x, p(x), color='limegreen', linewidth=0.7)
            del x,y,z,p
        
        def annotates():
            self.axis.annotate(f"max {max(yValues)}", xy=(xValuesLen/2, max(yValues) + yRange * 0.1), color='grey')
            self.axis.annotate(f"min {min(yValues)}", xy=(xValuesLen/2, min(yValues) + yRange * 0.1), color='grey')
            t1 = self.axis.plot(xValues, [max(yValues)] * xValuesLen, linestyle="--", color="grey", linewidth=0.7)
            t2 = self.axis.plot(xValues, [min(yValues)] * xValuesLen, linestyle="--", color="grey", linewidth=0.7)
            del t1,t2
        
        def optionsStatus():
            
            if self.a == 1 and oneOrMultiGraph == 1:
                annotates()
            if self.t == 1 and oneOrMultiGraph == 1:
                trendline()
            if self.a == 1 and oneOrMultiGraph == 2:
                annotates()
            if self.t == 1 and oneOrMultiGraph == 2:
                trendline()
            
        def tickListScale():
            if self.sumChVar == 0 or self.sumChVar > 15: 
                a = round(xValuesLen / 40)
                if a == 0:
                    a = 1
                self.tickList = list(range(0,xValuesLen, a))
            if self.sumChVar == 1: 
                a = round(xValuesLen / 40)
                if a == 0:
                    a = 1
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 40: self.tickList.append(xValuesLen -1)
            if self.sumChVar == 2 or self.sumChVar == 3 or self.sumChVar == 4: 
                a = round(xValuesLen / 20)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 20: self.tickList.append(xValuesLen -1)
            if self.sumChVar == 5 or self.sumChVar == 6 or self.sumChVar == 9: 
                a = round(xValuesLen / 16)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 16: self.tickList.append(xValuesLen-1)
            if self.sumChVar == 7 or self.sumChVar == 8 : 
                a = round(xValuesLen / 12)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 12: self.tickList.append(xValuesLen-1)
            if self.sumChVar == 10 or self.sumChVar == 11 or self.sumChVar == 12: 
                a = round(xValuesLen / 12)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 12: self.tickList.append(xValuesLen-1)
            if self.sumChVar == 13 or self.sumChVar == 14 or self.sumChVar == 15: 
                a = round(xValuesLen / 11)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 11: self.tickList.append(xValuesLen-1)
        
        def axisLineCreate(codeCurrencyDict):
            if self.oneSubplotVarMulti == 1:
                colorpalette = ['red', 'green', 'blue', 'gold', 'lawngreen', 'cyan', 'darkorange', 'hotpink', 'yellow', 'darkcyan', 'deepskyblue', 'violet', 'cadetblue', 
                                'indigo', 'cornflowerblue', 'mediumblue', 'darkgoldenrod', 'pink', 'lightgreen', 'darkred', 'gray', 'lightgray', 'salmon', 'chocolate', 'maroon', 
                                'tan', 'olive', 'darkgreen', 'lightcyan', 'magenta', 'mediumorchid', 'thistle', 'crimson', ]
                limitList, lineName = [],[]
                self.agr = 0
                self.axis.set_title("Waluty wykres zbiorczy", fontsize=fontSize, color="silver")
                
                for code in self.multiCodeCurrencyList:

                    if self.workingMode == 'Online_No_Database':
                        dataObj.getDataForGraph(code, self.multiTimeRangeList[self.agr], 2, self.firstloopEDL)
                        self.xValuesMultiGraph = dataObj.xValuesMultiGraph
                        self.yValuesMultiGraph = dataObj.yValuesMultiGraph
                        

                    if self.workingMode == 'Database':
                        scenObj.getDataForGraphDB(code, self.multiTimeRangeList[self.agr], 2, self.username, self.password, self.hostname, self.port, self.firstloopEDL) 
                        self.xValuesMultiGraph = scenObj.xValuesMultiGraph
                        self.yValuesMultiGraph = scenObj.yValuesMultiGraph
                        
                    locals()['line{}'.format(code[0:3])], = self.axis.plot(self.xValuesMultiGraph, self.yValuesMultiGraph, color=colorpalette[self.agr], linewidth=1)
                    limitList += self.yValuesMultiGraph
                    lineName.append(locals()['line{}'.format(code[0:3])])
                    progressbar() # po każdym przejściu pętli uruchamia funkcję Main.progress() w celu zaktualizowania progressbar
                    self.agr += 1
                
                if self.winFull.tk.call("ttk::style", "theme", "use") == "azure-dark":
                    self.figFS.legend(lineName, self.multiCodeCurrencyList, bbox_to_anchor=(0.995, 0.97), labelcolor='white')
                else:
                    self.figFS.legend(lineName, self.multiCodeCurrencyList, bbox_to_anchor=(0.995, 0.97), labelcolor='black')
                
                xaxis = self.axis.get_xaxis()
                xaxis.set_ticks(self.tickList)
                plt.xticks(rotation=45, fontsize=8)
                plt.ylim(min(limitList) - yRange, max(limitList) + yRange)
                self.axis.set_xlabel("Data") 
                self.axis.set_ylabel("PLN Złoty")
    
                del limitList
            else:
                self.axis.set_title(f"{codeMulti.upper()} {codeCurrencyDict[codeMulti.upper()]} ({tRange})", fontsize=fontSize, color="silver")
                t0 = self.axis.plot(xValues, yValues, linewidth=1)
                xaxis = self.axis.get_xaxis()
                xaxis.set_ticks(self.tickList)
                plt.xticks(rotation=45, fontsize=8)
                plt.ylim(min(yValues) - yRange, max(yValues) + yRange)
                self.axis.set_xlabel("Data") 
                self.axis.set_ylabel("PLN Złoty")
                del t0
        
        tickListScale()
        optionsStatus()
        axisLineCreate(codeCurrencyDict)
        
        del self.axis, xValues, yValues, self.tickList
    
    def putGraph(self, window, col, fig):
        self.canvas = FigureCanvasTkAgg(fig, master=window) 
        self.canvas._tkcanvas.grid(column=col, row=5, columnspan=11, padx=5, pady=5, sticky=tk.W) 
        window.update()
        window.deiconify()

    @classmethod # testowe użycie metody klasowej
    def printInformation(cls): 
        cls.agr_number +=1
        return cls.agr_number 
    
    def saveGraphPNG(self, graphNum, codeOne, timeRange):
        dataObj.createReportDir()
        if graphNum == 1: graphName = f"{codeOne.upper()} ostatnie {timeRange}.png"
        else: 
            dateTimeNow = time.localtime()
            num = Graph.printInformation()
            graphName = f"multi_Graph_{num}_{time.strftime('%d-%m-%Y %H%M%S',dateTimeNow)}.png"

        plt.savefig(f"{dataObj.filePath}/reports/{graphName}", dpi=200)
        del graphName

    ############################    fullscreenGraphWindow   #######################################################    
        
    def multiGraphList(self, viewNum, lenCurrencyList, trvl, chvl = None, codevl = None, codeCurrencyList = None):
        self.multiTimeRangeList, self.multiCodeCurrencyList = [], []
        
        if viewNum == 2:
            for a in range(15): 
                if chvl[a] == 1:
                    self.multiCodeCurrencyList.append(codevl[a])
                    self.multiTimeRangeList.append(trvl[a])
    
        else:
            for b in range(lenCurrencyList):
                if chvl[b] == 1:      
                    self.multiCodeCurrencyList.append(codeCurrencyList[b])
                    self.multiTimeRangeList.append(trvl[b])
    
        self.sumChVar = sum(chvl)
        trvl.clear()
        chvl.clear()
        codevl.clear()
        
    def _quit(self):
            plt.clf()
            plt.close(self.figFS)
            self.winFull.quit()
            self.winFull.destroy()
            
    def runSaveGraphPNG2(self):
            self.saveGraphPNG(2, codeOne=None, timeRange=None )
        
    def winFullSet(self):
        self.winFull = tk.Tk()
        self.winFull.overrideredirect(True)
        self.winFull.geometry("{0}x{1}+0+0".format(self.winFull.winfo_screenwidth(), self.winFull.winfo_screenheight()))
        #self.winFull.attributes("-fullscreen", True)
    
    def themeSet(self, root):    
        if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            self.figFS = plt.figure(figsize=(19,10), facecolor = "dimgray")
            self.gridColor = "darkslategrey"
        else:
            self.winFull.tk.call("set_theme", "light")
            plt.style.use('Solarize_Light2')
            self.figFS = plt.figure(figsize=(19,10), facecolor = "white")
            self.gridColor = "white"
    
    def drawGraphLoop(self, codeCurrencyDict, firstloopEDL, progressbar, workingMode, username, password, hostname, port):
        self.firstloopEDL = firstloopEDL
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.workingMode = workingMode
        self.agr = 0
        self.listTrSum = len(self.multiCodeCurrencyList)
        
        if workingMode == 'Online_No_Database':
            dataObj.checkConnection()
        
        def addGraph():
            self.axis.grid(linestyle="solid", color=self.gridColor,  linewidth=0.4)
            
            if workingMode == 'Online_No_Database':
                dataObj.getDataForGraph(code, self.multiTimeRangeList[self.agr], 2, firstloopEDL)
                self.xValuesMultiGraph = dataObj.xValuesMultiGraph
                self.yValuesMultiGraph = dataObj.yValuesMultiGraph
                codeMulti = dataObj.codeMulti
            elif workingMode == 'Database':
                scenObj.getDataForGraphDB(code, self.multiTimeRangeList[self.agr], 2, username, password, hostname, port, firstloopEDL) 
                self.xValuesMultiGraph = scenObj.xValuesMultiGraph
                self.yValuesMultiGraph = scenObj.yValuesMultiGraph
                codeMulti = scenObj.codeMulti  

            self.drawGraph(fSize, self.multiTimeRangeList[self.agr], self.xValuesMultiGraph, self.yValuesMultiGraph, codeMulti, 2,codeCurrencyDict, progressbar)
            if self.oneSubplotVarMulti  == 0:
                self.figFS.tight_layout() # wykresy nie nachodzą na siebie
            else:
                self.figFS.tight_layout( rect=[0, 0, 0.869, 1.0])
                self.putGraph(self.winFull, 0, self.figFS)
            self.agr += 1
        
        if self.oneSubplotVarMulti  == 1:
            self.axis = self.figFS.add_subplot(111)
            fSize = 16
            code = self.multiCodeCurrencyList[0]
            addGraph()
            self.oneSubplotVarMulti  = 0
        else:
            for code in self.multiCodeCurrencyList:
                if self.listTrSum == 1: self.axis = self.figFS.add_subplot(111)
                elif self.listTrSum == 2: self.axis = self.figFS.add_subplot(121 + self.agr) 
                elif self.listTrSum == 3: self.axis = self.figFS.add_subplot(221 + self.agr) 
                elif self.listTrSum == 4: self.axis = self.figFS.add_subplot(221 + self.agr)  
                elif self.listTrSum == 5: self.axis = self.figFS.add_subplot(231 + self.agr)  
                elif self.listTrSum == 6: self.axis = self.figFS.add_subplot(231 + self.agr)  
                elif self.listTrSum == 7: self.axis = self.figFS.add_subplot(241 + self.agr)  
                elif self.listTrSum == 8: self.axis = self.figFS.add_subplot(241 + self.agr) 
                elif self.listTrSum == 9: self.axis = self.figFS.add_subplot(331 + self.agr)  
                elif self.listTrSum == 10: self.axis = self.figFS.add_subplot(3,4,1 + self.agr)  
                elif self.listTrSum == 11: self.axis = self.figFS.add_subplot(3,4,1 + self.agr)  
                elif self.listTrSum == 12: self.axis = self.figFS.add_subplot(3,4,1 + self.agr) 
                elif self.listTrSum == 13: self.axis = self.figFS.add_subplot(3,5,1 + self.agr) 
                elif self.listTrSum == 14: self.axis = self.figFS.add_subplot(3,5,1 + self.agr) 
                elif self.listTrSum == 15: self.axis = self.figFS.add_subplot(3,5,1 + self.agr)

                if self.listTrSum >0 and self.listTrSum <= 4: fSize = 16 
                elif self.listTrSum > 4 and self.listTrSum <= 6: fSize = 14    
                elif self.listTrSum > 6 and self.listTrSum <= 12: fSize = 12  
                elif self.listTrSum > 12: fSize = 10
                addGraph()
                progressbar()
                
            self.putGraph(self.winFull, 0, self.figFS)
            self.xValuesMultiGraph.clear() 
            self.yValuesMultiGraph.clear()
            del self.xValuesMultiGraph, self.yValuesMultiGraph
            
    def clearList(self):
        self.multiCodeCurrencyList.clear() 
        self.multiTimeRangeList.clear()
          
dataObj = Data() 
scenObj = Scenario()




   


    


