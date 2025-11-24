import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        
        drawn = []
        for _ in range(num_balls):
            ball_index = random.randrange(len(self.contents))
            drawn.append(self.contents.pop(ball_index))
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Check if the drawn balls meet the expected criteria
        meets_criteria = True
        for color, expected_count in expected_balls.items():
            if drawn_balls.count(color) < expected_count:
                meets_criteria = False
                break
        
        if meets_criteria:
            success_count += 1
    
    return success_count / num_experiments
