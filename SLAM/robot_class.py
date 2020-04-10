# Robot Class
import numpy as np
import matplotlib.pyplot as plt
import random

#%matplotlib inline

class Robot:
    def __init__(self, world_grid=200.0, measurement_range=50.0,
                 motion_noise=5.0, measurement_noise=5.0):
        #self.measurement_noise = 0.0
        self.world_grid = world_grid
        self.measurement_range = measurement_range
        self.x = world_grid/2.0
        self.y = world_grid/2.0
        self.motion_noise = motion_noise
        self.measurement_noise = measurement_noise
        self.landmarks = []
        self.num_landmark = 0

    def rand(self):
        return random.random() * 2.0 - 1.0

    def move(self, dx, dy):
        x = self.x + dx + self.rand() * self.motion_noise
        y = self.y + dy + self.rand() * self.motion_noise

        if x < 0.0 or x > self.world_grid or y < 0.0 or y > self.world_grid:
            return False
        else:
            self.x = x
            self.y = y
            return True

    def sense(self):
        measurements = []

        for i, lm in enumerate(self.landmarks):
            dx = lm[0] - self.x + self.rand() * self.measurement_noise
            dy = lm[1] - self.y + self.rand() * self.measurement_noise

            if dx < self.measurement_range or dy < self.measurement_range:
                measurements.append([i, dx, dy])
        
        return measurements
        
    def make_landmarks(self, num_landmark):
        self.landmarks = []
        for i in range(num_landmark):
            self.landmarks.append([round(random.random() * self.world_grid),
                                   round(random.random() * self.world_grid)])
        self.num_landmark = num_landmark

    def __repr__(self):
        return 'Robot: [x=%.5f y=%.5f]' % (self.x, self.y)
