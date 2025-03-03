# Add compatibility for matplotlib>=3.5.0 where register_cmap was moved
import matplotlib

if not hasattr(matplotlib.cm, 'register_cmap') and hasattr(matplotlib.colormaps, 'register'):
    def register_cmap_compat(name, cmap):
        matplotlib.colormaps.register(cmap=cmap, name=name)
    
    matplotlib.cm.register_cmap = register_cmap_compat

from .metrics import (catalog_coverage, intra_list_similarity,
                      make_confusion_matrix, mark, mse, novelty,
                      personalization, prediction_coverage,
                      recommender_precision, recommender_recall, rmse)
from .plots import (class_separation_plot, coverage_plot, long_tail_plot,
                    mapk_plot, mark_plot,  metrics_plot, precision_recall_plot, roc_plot)
