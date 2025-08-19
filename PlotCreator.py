import numpy as np
from FindFiles import findFilesWithEnding
import matplotlib.pyplot as plt
import os


def plotRuns(inputFolder, outputFolder, lowerCutoff, upperCutoffs, allSeries, title):
    os.makedirs(outputFolder, exist_ok=True)

    for filename in findFilesWithEnding(inputFolder, ".npz"):

        data = np.load("%s/%s.npz" % (inputFolder, filename), allow_pickle=True)
        meta = data["meta"].item()

        for upperCutoff in upperCutoffs:

            x_values = np.arange(lowerCutoff, upperCutoff)

            plt.figure(figsize=(12, 9))
            plt.rcParams.update({
                'font.size': 15,
                'axes.titlesize': 17,
                'axes.labelsize': 15,
                'xtick.labelsize': 13,
                'ytick.labelsize': 13,
                'legend.fontsize': 13,
                'lines.linewidth': 3,
            })

            for series in allSeries:
                if series["key"] in data:
                    plt.plot(x_values, data[series["key"]][lowerCutoff:upperCutoff], label=series["label"], marker=".")

            plt.xlabel('Number of iterations')
            plt.ylabel('Error measure')
            plt.title(title(meta['name'], meta['m'], meta['n']))
            plt.legend()

            fig_manager = plt.get_current_fig_manager()
            fig_manager.window.state('zoomed')
            plt.ylim(bottom=0)
            #plt.show()
            plt.savefig("%s/%s_%s.jpg" % (outputFolder, upperCutoff, meta['name']), bbox_inches='tight')
            plt.close()
