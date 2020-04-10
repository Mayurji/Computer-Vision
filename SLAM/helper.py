from robot_class import Robot
from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

path = os.getcwd()

def display_world(world_grid, position, landmarks=None):
    
    sns.set_style("dark")
    world_size = np.zeros((world_grid+1, world_grid+1))
    ax=plt.gca()
    cols = world_grid+1
    rows = world_grid+1
    
    ax.set_xticks([x for x in range(1,cols)], minor=True)
    ax.set_yticks([y for y in range(1,rows)], minor=True)
    
    plt.grid(which='minor', ls='-', lw=1, color='white')
    plt.grid(which='major', ls='-', lw=2, color='white')
    
    ax.text(position[0], position[1], 'o', ha='center',
            va='center', color='r', fontsize=30)
    
    if (landmarks is not None):
        for pos in landmarks:
            if (pos != position):
                ax.text(pos[0], pos[1], 'x', ha='center', va='center',
                        color='purple', fontsize=20)
    
    plt.show()
    

def save_display_world(i,world_grid, position, landmarks=None, next_point=None):

    sns.set_style("dark")
    world_size = np.zeros((world_grid+1, world_grid+1))
    ax = plt.gca()
    cols = world_grid+1
    rows = world_grid+1

    ax.set_xticks([x for x in range(1, cols)], minor=True)
    ax.set_yticks([y for y in range(1, rows)], minor=True)

    plt.grid(which='minor', ls='-', lw=1, color='white')
    plt.grid(which='major', ls='-', lw=2, color='white')

    ax.text(position[0], position[1], 'o', ha='center',
            va='center', color='r', fontsize=30)

    if (landmarks is not None):
        for pos in landmarks:
            if (pos != position):
                ax.text(pos[0], pos[1], 'x', ha='center', va='center',
                        color='purple', fontsize=20)

    if next_point[0] != 0:
        plt.plot([position[0], next_point[0]], [
                 position[1], next_point[1]], linewidth=3)
        plt.annotate(i, (position[0],position[1]), textcoords='offset points',
                    xytext=(0,10), ha='center', fontsize=30)
        plt.tick_params(axis='both', labelsize=20)
        #plt.arrow(position[0], position[1], next_point[0]/2, next_point[1]/2)
        

    plt.savefig(path+"/2d movement/world_"+i+".png")

    return "2d World is Covered"


def make_data(N, num_landmarks, world_grid, measurement_range,
              motion_noise, measurement_noise, distance):

    complete = False
    while not complete:
        data = []
        R = Robot(world_grid, measurement_range, motion_noise, measurement_noise)
        R.make_landmarks(num_landmarks)
        seen = [False for row in range(num_landmarks)]
        
        orientation = random.random() * 2.0 * pi
        dx = cos(orientation) * distance
        dy = sin(orientation) * distance
        
        for k in range(N-1):
            Z = R.sense()
            for i in range(len(Z)):
                seen[Z[i][0]] = True
            while not R.move(dx, dy):
                orientation = random.random() * 2.0 * pi
                dx = cos(orientation) * distance
                dy = sin(orientation) * distance
                
            data.append([Z, [dx, dy]])
            
        complete = (sum(seen) == num_landmarks)
    print(' ')
    print('Landmarks: ', R.landmarks)
    print(R)
    
    return data
                
    
