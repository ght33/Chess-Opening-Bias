# Chess-Opening-Bias
This is a python pipeline aimed at isolating and quantifying selection bias in chess opening win rates using Lichess match data.
Standard opening statstics display aggregated win rates across an entire database or within generic average game rating buckets (eg. matches where avg player rating is 1800)
This introduces selection bias. Complex or aggressive openings are disproportionately favored by players who are highly rated. When a 2100 player defeats a 1700 player, naive math places the outcome into a 1900 avg bucket. The metric accidentally captures the player skill gap rather than the opening play's true utility within the overall match.


### Progress
 
Ingestion and Profiling: Loading raw CSV, checking how many columns we have (should be 4), and making sure data is loaded properly without anything missing. Columns are 'white_rating' , 'black_rating', 'winner', and 'opening_name'.

Baseline Win Rates: Calculating raw win, loss, and draw counts to see the basic breakdown for White vs. Black. Calculated distribution as a baseline to measure against calculated raw opening win rates to highlight how unadjusted statistics ignore player skill level.

Performance over expectation (POE): Applied ELO rating formula to calculate the expected game outcomes based on rating differences in order to isolate true opening advantage by removing player skill bias.