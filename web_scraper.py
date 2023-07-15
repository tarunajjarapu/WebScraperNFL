#Name: Tarun Ajjarapu

import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk


class Find:

    def __init__(self):
        """
        This initializes the lists of players for all positions
        """
        self.__all_lists = None

    def web_scrape(self, url):
        """
        Scrapes the pro football reference website for all its data from
        pro NFL players. Creates lists based on the players position and
        ranked based on NFL fantasy points
        :param url: website to be searched for data
        :return: None
        """
        current_page = requests.get(url)
        soup = BeautifulSoup(current_page.text, 'html.parser')
        for a in soup.findAll('a'):
            a.replaceWithChildren()
        players = soup.find_all('tr')
        players = players[2:]
        fantasy_list_qb = []
        fantasy_list_rb = []
        fantasy_list_wr = []
        fantasy_list_te = []
        for player in players:
            if not player.get_text(strip=True).startswith("RkPlayer"):
                if player.findAll('td')[25].contents \
                        and player.findAll('td')[2].contents:
                    if player.findAll('td')[2].contents[0] == 'QB':
                        fantasy_list_qb.append(
                            [int(player.findAll('td')[25].contents[0]),
                             player.findAll('td')[0].contents[0],
                             player.findAll('td')[2].contents[0]])
                    if player.findAll('td')[2].contents[0] == 'RB':
                        fantasy_list_rb.append(
                            [int(player.findAll('td')[25].contents[0]),
                             player.findAll('td')[0].contents[0],
                             player.findAll('td')[2].contents[0]])
                    if player.findAll('td')[2].contents[0] == 'WR':
                        fantasy_list_wr.append(
                            [int(player.findAll('td')[25].contents[0]),
                             player.findAll('td')[0].contents[0],
                             player.findAll('td')[2].contents[0]])
                    if player.findAll('td')[2].contents[0] == 'TE':
                        fantasy_list_te.append(
                            [int(player.findAll('td')[25].contents[0]),
                             player.findAll('td')[0].contents[0],
                             player.findAll('td')[2].contents[0]])
        #Sorts the data based on fantasy points
        fantasy_list_qb.sort(key=lambda x: x[0], reverse=True)
        fantasy_list_rb.sort(key=lambda x: x[0], reverse=True)
        fantasy_list_wr.sort(key=lambda x: x[0], reverse=True)
        fantasy_list_te.sort(key=lambda x: x[0], reverse=True)
        self.__all_lists = [fantasy_list_qb, fantasy_list_rb, fantasy_list_wr,
                            fantasy_list_te]

    def get_lists(self):
        """
        Allows user to access the data of the ranked players
        :return: the instance variable for ranked players
        """
        return self.__all_lists


def main():
    """
    Creates all the necessary buttons, labels, etc. for a new tkinter
    instance. This creates the foundation, and creates the program set for
    QBs in 2022. It shows the fantasy scores on the left side of the players
    names. It also allows the user to switch which year they want to search.
    :return: None
    """
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
    # Sets up the labels for the top 10 players being displayed currently
    all_labels = []
    for row in range(1, 11):
        label = Label(lbl_frame, font='Courier 30',
                      text=str(curr.get_lists()[0][row - 1][
                                   0]) + "  " + str(
                          curr.get_lists()[0][row - 1][1]))
        label.grid(row=row, column=1, padx=2, pady=2, sticky='W')
        all_labels.append(label)
    instructions = Label(lbl_frame, font='Courier 12 bold',
                         text='Choose a position to rank or select a year '
                              'above',
                         borderwidth=1, relief="solid")
    instructions.grid(row=12, column=1, padx=4, pady=10, sticky='W')
    choices = ['QB', 'RB', 'WR', 'TE']
    low_frame = ttk.Frame(origin)
    low_frame.grid(row=2, column=1, columnspan=2, sticky='W', pady=2)
    spacer = Label(low_frame, font='Arial 20 bold', text=' ')
    spacer.grid(row=0, column=1, padx=80, pady=2, sticky='W')
    # Setting up the buttons to allow user to select a different position
    qb_button = Button(low_frame, font='Arial 20 bold',
                       text=choices[0],
                       command=lambda: change_position(all_labels,
                                                       control_label,
                                                       curr.get_lists(),
                                                       0, instructions))
    qb_button.grid(row=0, column=2, padx=2, pady=2)
    rb_button = Button(low_frame, font='Arial 20 bold',
                       text=choices[1],
                       command=lambda: change_position(all_labels,
                                                       control_label,
                                                       curr.get_lists(),
                                                       1, instructions))
    rb_button.grid(row=0, column=3, padx=2, pady=2)
    wr_button = Button(low_frame, font='Arial 20 bold',
                       text=choices[2],
                       command=lambda: change_position(all_labels,
                                                       control_label,
                                                       curr.get_lists(),
                                                       2, instructions))
    wr_button.grid(row=0, column=4, padx=2, pady=2)
    te_button = Button(low_frame, font='Arial 20 bold',
                       text=choices[3],
                       command=lambda: change_position(all_labels,
                                                       control_label,
                                                       curr.get_lists(),
                                                       3, instructions))
    te_button.grid(row=0, column=5, padx=2, pady=2)
    # Creating a drop down menu and button to select a year
    test_val = StringVar()
    test_val.set('2022')
    years = []
    for i in range(2000, 2023):
        years.append(i)
    options = OptionMenu(low_frame, test_val, *years)
    options.grid(row=3, column=3, padx=2, pady=5)
    options.configure(font='Arial 10 bold')
    btn_options = Button(low_frame, font='Arial 10 bold',
                         text='Select Year',
                         command=lambda: set_lists(test_val, curr,
                                                   instructions))
    btn_options.grid(row=3, column=4, padx=2, pady=5)
    origin.mainloop()


def set_lists(test_val, curr, instructions):
    """
    Creates a new url to be searched for since the user wants to choose a new
    year
    :param test_val: the year being chosen
    :param curr: instance of the find so that new data can be accessed
    :param instructions: output so that the user can understand what to do
    :return: None
    """
    url = 'https://www.pro-football-reference.com/years/' + str(
        test_val.get()) + '/fantasy.htm'
    instructions['text'] = 'Select a position to update list'
    curr.web_scrape(url)


def change_position(all_labels, control_label, all_lists, index, instructions):
    """
    Button pressed, user wants to switch to a new position. Displays the new
    players at each position ranked.
    :param all_labels: the list of labels to be changed for the new position
    :param control_label: label being used to display current position at top
    :param all_lists: list of all lists of players at all positions
    :param index: index for the position being chosen
    :param instructions: output so that the user can understand what to do
    :return:
    """
    choices = ['QB', 'RB', 'WR', 'TE']
    control_label['text'] = choices[index]
    for i in range(0, 10):
        all_labels[i]['text'] = str(all_lists[index][i][0]) + "  " + str(
            all_lists[index][i][1])
    instructions[
        'text'] = 'To change years, select from menu and click select year'


if __name__ == '__main__':
    main()
