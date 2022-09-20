import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

#%% plot confusion matrix
def plotConfusionMatrix(confusion_matrix, fig_title, saving_path):
    plt.figure(figsize=(4, 4.1))
    plt.title(fig_title)
    sns.heatmap(confusion_matrix, annot=True, cbar=False)
    plt.savefig(saving_path, bbox_inches="tight")