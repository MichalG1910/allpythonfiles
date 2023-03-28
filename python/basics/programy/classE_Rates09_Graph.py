import re, os, sys, math, datetime, requests, time
from tkinter import messagebox as mBox
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
from tabulate import tabulate
import PIL
import PIL._tkinter_finder
from classE_Rates09_Data import Data

import numpy as np

class Graph:
    agr_number = 0

    def __init__(self):
        self.filePath = os.path.dirname(sys.argv[0]) # ścieżka do naszego pliku exchange_rates
        self.today = datetime.date.today()
        
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
    
    def newGraph(self, currencyName, timeRange, root):
        dataObj.checkConnection()
        dataObj.getDataForGraph(currencyName, timeRange, 1)
        self.refreshGraph(root, timeRange)

    def refreshGraph(self, root, timeRange, xValues, yValues, codeOne, codeCurrencyDict):
        plt.clf()
        plt.close(self.fig)
        try:
            xValues 
        except AttributeError:
            xValues = None
        '''  
        if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            self.fig = plt.figure(figsize=(11,8), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
        '''
        self.fig = plt.figure(figsize=(11,8), facecolor = "lightcyan")
        
        if xValues == None:
            plt.clf()
            plt.close(self.fig)
            
            self.emptyGraph(root)
        else:
            self.listChVar = [0]
            self.axis = self.fig.add_subplot(111)
            self.axisCreate(16, timeRange, xValues, yValues, codeOne, 1, codeCurrencyDict, self.axis)
            self.fig.tight_layout()
            self.putGraph(root, 4, self.fig)
            self.listChVar.clear()
        
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
            '''if self.annotateVarMulti.get() == 1 and oneOrMultiGraph == 2:
                annotates()
            if self.trendLineVarMulti.get() == 1 and oneOrMultiGraph == 2:
                trendline()
            '''
        def tickListScale():
            if sum(self.listChVar) == 0: 
                a = round(xValuesLen / 25)
                self.tickList = list(range(0,xValuesLen, a))
            if sum(self.listChVar) == 1: 
                a = round(xValuesLen / 40)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 40: self.tickList.append(xValuesLen -1)
            if sum(self.listChVar) == 2 or sum(self.listChVar) == 3 or sum(self.listChVar) == 4: 
                a = round(xValuesLen / 20)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 20: self.tickList.append(xValuesLen -1)
            if sum(self.listChVar) == 5 or sum(self.listChVar) == 6: 
                a = round(xValuesLen / 16)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 16: self.tickList.append(xValuesLen-1)
            if sum(self.listChVar) == 7 or sum(self.listChVar) == 8 or sum(self.listChVar) == 9: 
                a = round(xValuesLen / 15)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 15: self.tickList.append(xValuesLen-1)
            if sum(self.listChVar) == 10 or sum(self.listChVar) == 11 or sum(self.listChVar) == 12: 
                a = round(xValuesLen / 14)
                self.tickList = list(range(0,xValuesLen, a))
                if len(self.tickList) < 14: self.tickList.append(xValuesLen-1)
            if sum(self.listChVar) == 13 or sum(self.listChVar) == 14 or sum(self.listChVar) == 15: 
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
        
    def multiGraphList(self, viewNum, rates, trvl, chvl, codeCurrencyList):
        self.listTR, self.listChVar, listCC, self.multiTimeRangeList, self.multiCodeCurrencyList = [], [], [], [], []
        
        
        if viewNum == 2:
            for a in range(15): 
                listCC.append(globals()['codeVar{}'.format(a)].get())
                self.listTR.append(globals()['timeRange{}'.format(a)].get())
                self.listChVar.append(globals()['chVar{}'.format(a)].get())
                if self.listChVar[a] == 1:
                    self.multiCodeCurrencyList.append(listCC[a])
                    self.multiTimeRangeList.append(self.listTR[a])
        else:
            for b in range(len(rates)):
                #self.listTR.append(globals()['timeRange{}'.format(b)].get())
                #self.listChVar.append(globals()['chVar{}'.format(b)].get())
                if chvl[b] == 1:      #if self.listChVar[b] == 1:
                    self.multiCodeCurrencyList.append(codeCurrencyList[b])
                    self.multiTimeRangeList.append(trvl[b])
         
        self.listTR.clear()
        listCC.clear()
    
dataObj = Data() 





   


    


