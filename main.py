from jifen_const import DEFAULT_FIGURE_FILE, DEFAULT_SCORE_DATA_CSV, \
    DEFAULT_LAST_YEAR_BASELINE, DEFAULT_PREDICTED_BASELINE
from jifen_plot import plot_scores

plot_scores(score_data_csv=DEFAULT_SCORE_DATA_CSV, figure_file=DEFAULT_FIGURE_FILE,
            last_year_baseline=DEFAULT_LAST_YEAR_BASELINE, predicted_baseline=DEFAULT_PREDICTED_BASELINE)
