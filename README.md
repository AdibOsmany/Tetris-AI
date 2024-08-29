1. What problem do we want to solve?
With the original 1989 Tetris recently being ”beaten” (getting a score so high the game
could not compute any further) we wanted to see if an AI was able to play Tetris up to a
human level or maybe even better.
2. What datasets did you use?
We have been using Jstris as our version of Tetris. We grab pixels on the board to keep
track of the pieces that are currently filling the board using the different colors of each
piece as the differentiation. The dataset used is its own past runs as it keeps track of
its previous results and compares it for improvement. The model takes in 4 types of
information: The current piece, the piece in the hold function, the next piece, and the
current board. This information is stored into a dictionary that the model reads from
each time a piece makes a move.
3. What models have you tried?
We have been using a reinforcement learning model, specifically the Proximal Policy
Optimization algorithm, where the AI plays a game being rewarded on the number of
blocks placed. We tried multiple different reward systems, but ultimately found the best
one for performance was a systems that rewarded +1 point for each block placed. It then
compares its own performance (number of points rewarded) of the past games its played
against one another to determine how it should play in the future.
4. How to evaluate the performance of the model on your dataset?
We evaluate the performance of its survivable based on the number of blocks placed. We
originally measured it by number of rows, but were not seeing good results. With the
switch to number of blocks placed we are seeing longer serviceability. After 48 hours of
testing we noticed our model begun to put pieces more horizontally. This allowed the
model to place many more pieces than it had since placing vertically caused the model
to lose the game quicker. After 65 hours the model continued to improve its horizontal
placements, but still has not consistently begun to clear rows. clearing rows will allow it
to place more blocks in the future leading to longer serviceability. We hope that if the
model was continued to be trained that it would find a consistent way to clear rows.
5. Any results you would like to share?
So far the model went from placing about 12 pieces on average to about 34 on average.
This was over the course of 65 hour of training. This shows promise, but we need a way to
more effectively spend time for quicker learning. Right now we are only able to play one game
at a time. If we could get many games running at the same time we believe the increase
Final Project Report-1
in performance will be much greater. Additionally we believe that once the model learns
about clearing rows we will see a large spike in performance. We think the way the model is
functioning, going from a weak performance to a decent performance will take some time, but
from a decent performance to a good one will be much quicker. Addtionally we believe that
if we shifted away from Jstris and instead made our own Tetris game that the model could
constantly be reading from, the model would function more efficiently and we may see a further
increase in performance.
