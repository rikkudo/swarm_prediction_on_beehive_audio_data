import matplotlib.pyplot as plt
import numpy as np


# def drawHeatMap(data, xlabel:str='', ylabel:str='', title:str=''):
#     plt.figure(figsize=(16, 8))
#     plt.imshow(data,cmap="hot_r")
#     plt.gca().invert_yaxis()
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.title(title)
#     plt.colorbar()
#     plt.show()


def drawHeatMap(data, xvalues, yvalues, xlabel: str = '', ylabel: str = '', title: str = '',
                save_fig:bool=False):
        plt.figure(figsize=(16, 8))
        plt.imshow(data, cmap="hot_r")
        plt.gca().invert_yaxis()
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        #plt.xticks(xvalues)
        #plt.yticks(yvalues)
        plt.colorbar()
        if save_fig:
            plt.savefig(f'hm_{title}.png')
        plt.show()

def drawTimeSeries(data: np.ndarray, xlabel, ylabel, text='', line_y:bool=False, save_fig:bool=False):
    plt.figure(figsize=(16, 8))
    if line_y:
        plt.axhline(y=0.0, color='r', linestyle='-')
    plt.plot(data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(text)

    if save_fig:
        plt.savefig(f'ts_{text}.png')
    plt.show()
