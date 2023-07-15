# Name: Tarun Ajjarapu

import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk


class Find:

    def __init__(self):
        """
        This initializes the lists of players for all positions
        """


def main():
    url = 'https://www.pro-football-reference.com/years/2022/fantasy.htm'
    curr = Find()
    curr.web_scrape(url)
    origin = Tk()
    # Setting up the frame of the program
    origin.title("NFL Fantasy Assistant")
    origin.resizable(False, False)
    lbl_frame = ttk.Frame(origin, padding="75 15 15 15")
    origin.geometry("690x770")
    lbl_frame.grid(row=13, column=2)
    pts = Label(lbl_frame, font='Courier 20', text='Points')
    pts.grid(row=0, column=1, padx=2, pady=2, sticky='W')
    control_label = Label(lbl_frame, font='Courier 40 bold', text='QB')
    control_label.grid(row=0, column=1, padx=215, pady=2, sticky='W')

if __name__ == '__main__':
    main()