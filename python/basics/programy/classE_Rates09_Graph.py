import re, os, sys, math, datetime, requests, time
from tkinter import messagebox as mBox
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
from tabulate import tabulate
import PIL
import PIL._tkinter_finder
from classE_Rates09_Data import Data
import tkinter as tk
from tkinter import ttk

import numpy as np

class Graph:
    agr_number = 0
        
    def emptyGraph(self, root):
        if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            self.fig = plt.figure(figsize=(11,8), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
            self.fig = plt.figure(figsize=(11,8), facecolor = "lightcyan")
        
        axis = self.fig.add_subplot(111) 
        axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
        axis.set_xlabel("Data") 
        axis.set_ylabel("PLN Złoty")
        self.fig.tight_layout()
        self.putGraph(root, 4, self.fig)
    
    def getVar(self, trendLineVar, annotateVar):
        self.a = annotateVar
        self.t = trendLineVar
        print("self a:", self.a, "\nself t:", self.t )   
    '''
    def newGraph(self, currencyName, timeRange, root):
        dataObj.checkConnection()
        dataObj.getDataForGraph(currencyName, timeRange, 1)
        self.refreshGraph(root, timeRange)
    '''
    def refreshGraph(self, root, timeRange, xValues, yValues, codeOne, codeCurrencyDict):
        plt.clf()
        plt.close(self.fig)
        #try:
        #    xValues 
        #except AttributeError:
        #    xValues = None
          
        if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            self.fig = plt.figure(figsize=(11,8), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
        
            self.fig = plt.figure(figsize=(11,8), facecolor = "lightcyan")
        
        if xValues == None:
            plt.clf()
            plt.close(self.fig)
            
            self.emptyGraph(root)
        else:
            self.sumChVar = 0
            self.axis = self.fig.add_subplot(111)
            self.axisCreate(16, timeRange, xValues, yValues, codeOne, 1, codeCurrencyDict, self.axis)
            self.fig.tight_layout()
            self.putGraph(root, 4, self.fig)
            del self.sumChVar
        
    def axisCreate(self, fontSize, tRange, xValues, yValues, code, oneOrMultiGraph, codeCurrencyDict, selfAxis):
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
            selfAxis.annotate(f"max {max(yValues)}", xy=(xValuesLen/2, max(yValues) + yRange * 0.1), color='grey')
            selfAxis.annotate(f"min {min(yValues)}", xy=(xValuesLen/2, min(yValues) + yRange * 0.1), color='grey')
            t1 = selfAxis.plot(xValues, [max(yValues)] * xValuesLen, linestyle="--", color="grey", linewidth=0.7)
            t2 = selfAxis.plot(xValues, [min(yValues)] * xValuesLen, linestyle="--", color="grey", linewidth=0.7)
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
            if self.sumChVar == 0: 
                a = round(xValuesLen / 25)
                self.tickList = list(range(0,xValuesLen, a))
                print('xvalueslen', xValuesLen, '\nticklist', self.tickList)

            if self.sumChVar == 1: 
                a = round(xValuesLen / 40)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 40: self.tickList.append(xValuesLen -1)
            if self.sumChVar == 2 or self.sumChVar == 3 or self.sumChVar == 4: 
                a = round(xValuesLen / 20)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 20: self.tickList.append(xValuesLen -1)
            if self.sumChVar == 5 or self.sumChVar == 6: 
                a = round(xValuesLen / 16)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 16: self.tickList.append(xValuesLen-1)
            if self.sumChVar == 7 or self.sumChVar == 8 or self.sumChVar == 9: 
                a = round(xValuesLen / 15)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 15: self.tickList.append(xValuesLen-1)
            if self.sumChVar == 10 or self.sumChVar == 11 or self.sumChVar == 12: 
                a = round(xValuesLen / 14)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 14: self.tickList.append(xValuesLen-1)
            if self.sumChVar == 13 or self.sumChVar == 14 or self.sumChVar == 15: 
                a = round(xValuesLen / 11)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 11: self.tickList.append(xValuesLen-1)
        
        def drawGraph(codeCurrencyDict):
            selfAxis.set_title(f"{code.upper()} {codeCurrencyDict[code.upper()]} ({tRange})", fontsize=fontSize, color="silver") # {dataObj.codeCurrencyDict[code.upper()]}
            selfAxis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
            t0 = selfAxis.plot(xValues, yValues, linewidth=1)
            xaxis = selfAxis.get_xaxis()
            xaxis.set_ticks(self.tickList)
            plt.xticks(rotation=45, fontsize=8)
            plt.ylim(min(yValues) - yRange, max(yValues) + yRange)
            selfAxis.set_xlabel("Data") 
            selfAxis.set_ylabel("PLN Złoty")
            del t0
        
        tickListScale()
        optionsStatus()
        drawGraph(codeCurrencyDict)
        
        del selfAxis, xValues, yValues, self.tickList
    
    def putGraph(self, window, col, fig):
        self.canvas = FigureCanvasTkAgg(fig, master=window) 
        self.canvas._tkcanvas.grid(column=col, row=3, columnspan=11, padx=5, pady=5) 
        window.update()
        window.deiconify()

    @classmethod 
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
        
    def multiGraphList(self, viewNum, rates, trvl, chvl = None, codevl = None, codeCurrencyList = None):
        self.listTR, self.listChVar, listCC, self.multiTimeRangeList, self.multiCodeCurrencyList = [], [], [], [], []
        print('class Graph - multigraphlist')
        print(trvl)
        print(chvl)
        print(codevl)
        
        if viewNum == 2:
            for a in range(15): 
                #listCC.append(globals()['codeVar{}'.format(a)].get())
                #self.listTR.append(globals()['timeRange{}'.format(a)].get())
                #self.listChVar.append(globals()['chVar{}'.format(a)].get())
                if chvl[a] == 1:
                    self.multiCodeCurrencyList.append(codevl[a])
                    self.multiTimeRangeList.append(trvl[a])
        else:
            for b in range(len(rates)):
                #self.listTR.append(globals()['timeRange{}'.format(b)].get())
                #self.listChVar.append(globals()['chVar{}'.format(b)].get())
                if chvl[b] == 1:      #if self.listChVar[b] == 1:
                    self.multiCodeCurrencyList.append(codeCurrencyList[b])
                    self.multiTimeRangeList.append(trvl[b])
         
        #self.listTR.clear()
        #listCC.clear()
        self.sumChVar = sum(chvl)
        trvl.clear()
        chvl.clear()
        codevl.clear()
        
    def _quit(self):
            self.figFS.clear()
            plt.close(self.figFS)
            self.winFull.quit()
            self.winFull.destroy()
            
    def runSaveGraphPNG2(self):
            self.saveGraphPNG(2, codeOne=None, timeRange=None )
        
    def winFullSet(self):
        self.winFull = tk.Tk()
        self.winFull.attributes("-fullscreen", True)
    
    def themeSet(self, root):    
        if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            self.figFS = plt.figure(figsize=(19,10), facecolor = "dimgray")
        else:
            self.winFull.tk.call("set_theme", "light")
            plt.style.use('Solarize_Light2')
            self.figFS = plt.figure(figsize=(19,10), facecolor = "lightcyan")

    def drawGraphLoop(self, codeCurrencyDict, firstloopEDL):
        self.agr = 0
        self.listTrSum = len(self.multiCodeCurrencyList)
           
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
            
            dataObj.getDataForGraph(code, self.multiTimeRangeList[self.agr], 2, firstloopEDL)
            self.axisCreate(fSize, self.multiTimeRangeList[self.agr], dataObj.xValuesMultiGraph, dataObj.yValuesMultiGraph, dataObj.codeMulti, 2,codeCurrencyDict, self.axis)
            self.figFS.tight_layout()# wykresy nie nachodzą na siebie
            self.putGraph(self.winFull, 0, self.figFS)
            self.agr += 1
            
            dataObj.xValuesMultiGraph.clear() 
            dataObj.yValuesMultiGraph.clear()
            del dataObj.xValuesMultiGraph, dataObj.yValuesMultiGraph

    def clearList(self):
        self.listChVar.clear()
        self.multiCodeCurrencyList.clear() 
        self.multiTimeRangeList.clear()
          
dataObj = Data() 





   


    


