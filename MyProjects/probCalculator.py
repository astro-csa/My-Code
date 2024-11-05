import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, number):
        choices = []
        if number <= len(self.contents):
            for _ in range(number):
                choice = random.choice(self.contents)
                self.contents.remove(choice)
                choices.append(choice)
            return choices
        else:
            return 'Dio cane'

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        ball_counts = {}
        for ball in drawn_balls:
            if ball in ball_counts:
                ball_counts[ball] += 1
            else:
                ball_counts[ball] = 1

        if all(ball_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)