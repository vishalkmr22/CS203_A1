# Simulation of Bertrand's Paradox
The simulation employs *10 lakh* random cases to calculate the necessary probabilities. It revolves around a unit circle (with a radius of 1) and an inscribed equilateral triangle with a side length of sqrt(3).

**It comprises 4 functions:**
1. **actual_prob function:** Simulates the actual problem statement of the paradox, determining whether the length of the chord exceeds the side of the equilateral triangle. This simulation yields a probability of approximately **0.33** for the chord exceeding the triangle's side length.
2. **prob_midpoint_approach function:** Simulates the distance of the midpoint of the chord and compares it with 1/2. This simulation yields a probability of around **0.25** for the chord exceeding the triangle's side length.
3. **prob_fixedpt_approach function:** Simulates chords by fixing one point and varying the other on the circumference of the circle. This simulation yields a probability of approximately **0.33** for the chord exceeding the triangle's side length.
4. **prob_parallel_chords_approach function:** Simulates by taking parallel lines and checks the probability of the chord being longer than the side of the equilateral triangle. This simulation yields a probability of around **0.50** for the chord exceeding the triangle's side length.