# Chess-Opening-Bias
This is a python pipeline aimed at isolating and quantifying selection bias in chess opening win rates using Lichess match data.
Standard opening statstics display aggregated win rates across an entire database or within generic average game rating buckets (eg. matches where avg player rating is 1800)
This introduces selection bias. Complex or aggressive openings are disproportionately favored by players who are highly rated. When a 2100 player defeats a 1700 player, naive math places the outcome into a 1900 avg bucket. The metric accidentally captures the player skill gap rather than the opening play's true utility within the overall match.


### Progress
 
Ingestion and Profiling: Loading raw CSV, checking how many columns we have (should be 4), and making sure data is loaded properly without anything missing. Columns are 'white_rating' , 'black_rating', 'winner', and 'opening_name'.

Baseline Win Rates: Calculating raw win, loss, and draw counts to see the basic breakdown for White vs. Black. Calculated distribution as a baseline to measure against calculated raw opening win rates to highlight how unadjusted statistics ignore player skill level.

Performance over expectation (POE): Applied ELO rating formula to calculate the expected game outcomes based on rating differences in order to isolate true opening advantage by removing player skill bias.

Predictive Modeling: Built a logistic regression classifier in sklearn using rating difference and one-hot encoded openings to test whether opening choice helps predict game outcomes on unseen data.

Dashboard Visualization: Built an interactive Streamlit application (app.py) to let users filter openings by minimum games played and analyze top performance metrics dynamically.

# Key Findings & Results
Analysis of 20,058 games from the Lichess dataset yields the following results:

Baseline Win Distribution: White wins 49.86% of games, Black wins 45.40%, and 4.74% end in draws.

Naive Win Rates vs. POE Differences:

Openings with high raw White win rates (like Zukertort Opening: Queen's Gambit Invitation at 69.81%) drop in true rank once adjusted for player ratings.

Scandinavian Defense: Main Line achieves the highest Performance Over Expectation (+0.1586 POE across 62 games), showing White outperforms Elo expectations by ~15.86 percentage points.

Other top performers include King's Pawn Game: Busch-Gass Gambit (+0.1534 POE) and Nimzowitsch Defense: Kennedy Variation (+0.1113 POE).

Predictive Power: Incorporating one-hot encoded opening selection alongside rating differentials yields a 63.76% classification accuracy in predicting game outcomes with Logistic Regression.
