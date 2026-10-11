# Project 2 Report: Adversarial Search & Tic-Tac-Toe AI

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Primary AI Algorithm:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information
- **Name:** Khin Yadanar Aung
- **MMDT ID:** MMDT002
---

## Section 1: AI Agent Configuration
- **Primary AI Algorithm:**  Minimax with Alpha-Beta Pruning
- **Pruning Technique:**  Alpha-Beta Pruning with Depth Penalty 
- **Heuristic Strategy:**  Win > Block > Center > Corners > Edges

---

## Section 2: Complexity & Search Tree Analysis
- **Maximum Search Depth (Empty 3x3 Board):** 549,946
- **Total Possible Board States:** 10
- **Unbeatable Minimax Guarantee:** Yes

---

## Section 3: Local Verification & Agent Checklist
*Check the algorithms, agents, and features you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Minimax Search Algorithm with Depth Penalty
- [x] Alpha-Beta Pruning Optimization
- [x] Rule-Based Heuristic Agent
- [x] Uniform Random Baseline Agent
- [x] Interactive Web Visualizer with Move Matrix & Metrics
- [x] Bot vs Bot Simulation Benchmark

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://ttt-mmdt002.onrender.com
- **Video Presentation Link:** https://drive.google.com/file/d/1rb2GgYt-MJFFp2Ivn_VSPOmgps3CVvSp/view?usp=sharing

---

## Section 5: Discussion
*Provide your written analysis for each point by replacing the bracket placeholders below:*
- **Explain how Alpha-Beta pruning reduces the number of evaluated game tree nodes without changing the minimax decision.**
In the Minimax agent, the first player tries to choose the move with the highest score, while the second player tries to choose the move with the lowest score. Alpha is the best score the first player can guarantee so far, while beta is the best score the second player can guarantee so far. As the algorithm explores the game tree, the bounds become tighter. When alpha is greater than or equal to beta, the algorithm stops exploring that branch because it cannot produce a better decision. Alpha-Beta pruning therefore evaluates fewer nodes while producing the same optimal move as standard Minimax, provided both use the same evaluation function and search depth.

- **Compare classical Adversarial Search (Minimax / Alpha-Beta) with modern Tree Search approaches in Generative AI (e.g., Monte Carlo Tree Search, Tree of Thoughts, or Process Reward Models).**
Classical AI uses explicit rules, algorithms, and predefined evaluation functions to search for solutions. It can use Alpha-Beta pruning to preserve the Minimax decision while skipping unnecessary branches. In contrast, modern AI often uses machine learning and LLMs to generate or evaluate solutions. It often faces larger search spaces and uses learned evaluation functions or sampling to guide exploration and improve computational efficiency.

