import re, os, sys, math, datetime, requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import PhotoImage
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
from tabulate import tabulate
import PIL
import PIL._tkinter_finder
from classE_Rates05 import ExchangeRates, Gui

def main():
    dataObj = ExchangeRates()
    dataObj.checkConnection()
    dataObj.createReportDir()
    dataObj.latestNBPreport()
    guiObj = Gui()
    guiObj.graphGui(dataObj.codeCurrencyDict)
    guiObj.exchangeRatesTabel(dataObj.effectiveDateList, dataObj.currencyList, dataObj.codeList, dataObj.valueList, dataObj.rates)
    guiObj.generateReportGui(dataObj.effectiveDateList)
    guiObj.emptyGraph()
    guiObj.winStyle(dataObj.filePath)
    guiObj.themeButton(dataObj.filePath)
    guiObj.win.mainloop()

main()
    
    





   


    


