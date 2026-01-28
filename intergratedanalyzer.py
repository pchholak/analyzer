from .plotting import (
    GraphicalAnalyzer,
    PairedGraphicalAnalyzer,
    SignalGraphicalAnalyzer,
)
from .signalanalysis import SignalProcessor
from .stats import PairedStatisticalAnalyzer, StatisticalAnalyzer


class IntegratedPairedAnalyzer(PairedStatisticalAnalyzer, PairedGraphicalAnalyzer):

    def paired_histograms(
        self, col, bins=20, caption="", ax=None, labels=..., annotate_diff=None
    ):
        """
        Add optional statistical difference annotation to the plot.
        """
        ax = super().paired_histograms(col, bins, caption, ax, labels)
        if annotate_diff and annotate_diff is not None:
            different, pval, method = self.test_difference_col(col)
            caption = f"{method}: {'Significantly Different' if different else 'Not Significantly Different'} (p = {pval:0.2E})"
            ax.set_title(caption)
        return ax


class IntegratedAnalyzer(StatisticalAnalyzer, GraphicalAnalyzer):
    def histogram(self, col, bins=20, caption="", ax=None, annotate_normality=None):
        """
        Adds optional normality annotation to the plot.
        """
        ax = super().histogram(col, bins, caption, ax)
        if annotate_normality and annotate_normality is not None:
            normality, pval = self.normality[col]
            caption = f"Shapiro-Wilk: {'Normal Distribution' if normality else 'Non-Normal Distribution'}\n(p = {pval:0.2E})"
            ax.set_title(caption)
        return ax

    def scatter_plot(self, col1, col2, caption="", ax=None, annotate_corr=None):
        """
        Adds optional corr coef annotation to the plot.
        """
        ax = super().scatter_plot(col1, col2, caption, ax)
        if annotate_corr and annotate_corr is not None:
            corr, pval, corr_method = self.calculate_corr_cols(col1, col2)
            caption = f"{corr_method} corr. coef. = {corr:0.2f} (p = {pval:0.2E})"
            ax.set_title(caption)
        return ax


class IntegratedSignalAnalyzer(SignalProcessor, SignalGraphicalAnalyzer):
    pass
