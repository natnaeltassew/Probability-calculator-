🎲 Probability Calculator – Hat Experiment (Python)

This project simulates drawing colored balls from a hat and estimating the probability of drawing a certain combination. It follows the specifications of the FreeCodeCamp Probability Calculator project.


---

🚀 Features

✅ Hat Class

The Hat class models a container filled with colored balls.

Initialize with any number of ball colors:

hat = Hat(red=3, blue=2, green=6)

Balls are stored in hat.contents

Supports random drawing of balls using:

hat.draw(num_balls)


Benefits:

Deep copy support for repeatable experiments

Draw method removes balls from the hat

Automatically handles cases where draw count exceeds available balls



---

🎯 Probability Experiment

The function:

experiment(hat, expected_balls, num_balls_drawn, num_experiments)

runs many experiments and estimates the probability of drawing a target ball combination.

Parameters:

Parameter	Type	Description

hat	Hat object	Initial hat setup
expected_balls	dict	Required colors & minimum counts, e.g. {"red": 2}
num_balls_drawn	int	How many balls to draw each trial
num_experiments	int	Number of repeated experiments


Return:

A float probability between 0 and 1.


---

🧠 Example Usage

from probability_calculator import Hat, experiment

hat = Hat(red=3, blue=2, green=6)

probability = experiment(
    hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)

Output example:

0.32


---

🔍 How It Works

1. A deep copy of the hat is made for each experiment


2. Balls are randomly drawn


3. The drawn set is checked against the expected_balls requirements


4. The experiment counts how often requirements are met


5. Probability = successful experiments ÷ total experiments




---

📂 File Included

probability_calculator.py – Contains the Hat class and experiment() function.



---

📜 Requirements

Python 3.6 or above



---

🤝 Contributing

Pull requests are welcome!
Open an issue if you want to discuss improvements or additional features (e.g., seeding, visualization, histogram of outcomes).


---

📄 License

This project is open-source and free to use.

