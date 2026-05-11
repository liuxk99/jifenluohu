from jifen_const import DEFAULT_FIGURE_FILE, DEFAULT_SCORE_DATA_CSV, \
    DEFAULT_LAST_YEAR_BASELINE, DEFAULT_PREDICTED_BASELINE
from jifen_plot import plot_scores

plot_scores(score_data_csv=DEFAULT_SCORE_DATA_CSV, figure_file=DEFAULT_FIGURE_FILE,
            last_year_baseline=DEFAULT_LAST_YEAR_BASELINE, predicted_baseline=DEFAULT_PREDICTED_BASELINE)
plot_scores(score_data_csv="jifen_data_2025.csv", figure_file=DEFAULT_FIGURE_FILE,
            last_year_baseline=114.46, predicted_baseline=117.33)
plot_scores(score_data_csv="jifen_data_2024.csv", figure_file=DEFAULT_FIGURE_FILE,
            last_year_baseline=109.92, predicted_baseline=114.46)
plot_scores(score_data_csv="jifen_data_2023.csv", figure_file=DEFAULT_FIGURE_FILE,
            last_year_baseline=105.38, predicted_baseline=109.92)
