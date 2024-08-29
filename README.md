### Tetris AI Bot

- Engineered an advanced AI bot using OpenAI Gym, NumPy, and the Proximal Policy Optimization (PPO) algorithm in Stable Baselines3, achieving superior gameplay performance in Tetris by optimizing real-time decision-making and piece placement.
- Integrated EasyOCR for real-time image recognition, effectively overcoming challenges related to dynamic game board assessment, which enabled the bot to rapidly analyze and respond to evolving gameplay conditions.
- The project earned recognition for excellence at the 2024 SES Symposium on Generative AI in Teaching and Learning, demonstrating innovative applications of AI in gaming and serving as a valuable teaching tool for AI and machine learning principles.


1. **What problem do I want to solve?**  
   With the original 1989 Tetris recently being "beaten" (achieving a score so high that the game could not compute any further), I wanted to explore whether an AI could play Tetris at a human level or perhaps even better.

2. **What datasets did I use?**  
   I have been using Jstris as my version of Tetris. I capture pixels on the board to track the pieces currently filling the board, using the different colors of each piece for differentiation. The dataset is composed of its own past runs, which are tracked and compared for improvement. The model takes in four types of information: the current piece, the piece in the hold function, the next piece, and the current board. This information is stored in a dictionary that the model reads from each time a piece makes a move.

3. **What models have I tried?**  
   I have been using a reinforcement learning model, specifically the Proximal Policy Optimization algorithm, where the AI plays a game and is rewarded based on the number of blocks placed. I experimented with different reward systems, but ultimately found that the best performance was achieved with a system that rewarded +1 point for each block placed. The model then compares its own performance (number of points rewarded) from past games to determine how it should play in the future.

4. **How do I evaluate the performance of the model on my dataset?**  
   I evaluate the model's performance based on the number of blocks placed before losing. Initially, I measured performance by the number of rows cleared, but this did not yield good results. After switching to counting the number of blocks placed, I observed longer survival times. After 48 hours of testing, the model began to place pieces more horizontally, which allowed it to place more pieces overall. After 65 hours, the model continued to improve its horizontal placements but has not yet consistently cleared rows. Clearing rows would allow it to place more blocks in the future, leading to longer survivability. I believe that with continued training, the model would eventually find a consistent strategy for clearing rows.

5. **Any results I would like to share?**  
   So far, the model has improved from placing about 12 pieces on average to about 34 on average over the course of 65 hours of training. This shows promise, but I need a way to more effectively spend time for quicker learning. Currently, I am only able to play one game at a time. If I could run multiple games simultaneously, I believe performance would increase more rapidly. Additionally, I think that once the model learns how to clear rows, there will be a significant spike in performance. I also believe that if I shifted away from Jstris and instead developed my own Tetris game that the model could continuously read from, the model would function more efficiently, potentially leading to further performance improvements.
