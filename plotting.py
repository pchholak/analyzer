import os
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

from .base import BaseAnalyzer, PairedAnalyzer, SignalDataAnalyzer, SingleDataAnalyzer


class GenericGraphicalAnalyzer(BaseAnalyzer):
    def save_plot(
        self,
        fig,
        fname,
        subdir="",
        fmts=["pdf", "png"],
        replace_slash_w_percent_in_fname=True,
    ):
        tar_dir = os.path.join(self.results_dir, subdir)
        os.makedirs(tar_dir, exist_ok=True)
        if replace_slash_w_percent_in_fname:
            fname = fname.replace("/", "%")
        for fmt in fmts:
            fig.savefig(
                os.path.join(tar_dir, f"{fname}.{fmt}"),
                bbox_inches="tight",
            )
        return None


class SignalGraphicalAnalyzer(SignalDataAnalyzer, GenericGraphicalAnalyzer):
    def plot_signals_rowwise_EMD(self, imfs: np.ndarray, ax: Optional[Axes] = None):
        """
        Plot IMFs as layered subplots, specialized for EMD.
        """
        y, x = self.signal.series.to_numpy(), self.signal.series.index
        if ax is None:
            _, ax = plt.subplots(figsize=(12, 12))
        n_imfs = imfs.shape[0]
        y_range = (np.max(y) - np.min(y)) * 1.2
        x_lim = [np.min(x), np.max(x)]
        for i_imf in range(n_imfs - 1):
            plt.subplot(n_imfs, 1, i_imf + 1)
            plt.plot(x, imfs[i_imf], "k")
            plt.xlim(x_lim)
            imf_mean = np.mean(imfs[i_imf])
            plt.ylim([imf_mean - y_range / 2, imf_mean + y_range / 2])
            plt.ylabel(f"IMF {i_imf + 1}")
            plt.grid()
        plt.subplot(n_imfs, 1, n_imfs)
        plt.plot(x, y, color="0.8")
        plt.plot(x, imfs[-1], "k")
        plt.xlim(x_lim)
        imf_mean = np.mean(imfs[-1])
        # ax.set_ylim([imf_mean - y_range / 2, imf_mean + y_range / 2])
        plt.ylabel("Residual")
        plt.grid()
        plt.tight_layout()
        plt.show()
        return ax


class PairedGraphicalAnalyzer(PairedAnalyzer, GenericGraphicalAnalyzer):
    def paired_histograms(self, col, bins=20, caption="", ax=None, labels=(None, None)):
        """
        Create a pair of overlapping histograms from the data contained
        in the column `col` of both the data containers.
        """
        if ax is None:
            _, ax = plt.subplots()
        ax.hist(
            self.df1[col],
            bins=bins,
            edgecolor="black",
            alpha=0.7,
            label=labels[0],
        )
        ax.hist(
            self.df2[col],
            bins=bins,
            edgecolor="black",
            alpha=0.7,
            label=labels[1],
        )
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        ax.legend()
        ax.set_title(caption)
        plt.tight_layout()
        return ax


class GraphicalAnalyzer(SingleDataAnalyzer, GenericGraphicalAnalyzer):

    def histogram(self, col, bins=20, caption="", ax=None):
        """
        Create an histogram of the data contained in column `col`.
        """
        if ax is None:
            _, ax = plt.subplots()
        ax.hist(
            self.df[col],
            bins=bins,
            edgecolor="black",
            alpha=0.7,
        )
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        ax.set_title(caption)
        plt.tight_layout()
        return ax

    def scatter_plot(self, col1, col2, caption="", ax=None):
        """
        Create a scatter plot from data in columns `col1` and `col2`.
        """
        if ax is None:
            _, ax = plt.subplots()
        ax.scatter(self.df[col1], self.df[col2])
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_title(caption)
        plt.tight_layout()
        return ax
