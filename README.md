# DRL_CollaborationAndCompetition
This project is a part of:  
 [Deep Reinforcement Learning Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893
 )

The project uses DDPG algorithm to solve 'Tennis' environment.  

![tennis app](./data/tennis.gif)

# Environment details
Goal is to move play tennis using two rockets. If the ball hits the grund or goes out-of-bounds the reward is -0.01. If the rocket hits the ball the reward is 0.1. The goal is to write cooperative agent that will reach score of 0.5 within 100 consecutive episodes by bouncing the ball as long as possible.

* There are 2 rockets
* Each arm rocket contains 24 local observations
* Action space contains 8 contunuous values in range from -1 to 1.


# Requirements
Below you can find a list of requirements required to run train.py script:

## Resources
- python 3.6
- Tennis app (this is delivered by Udacity Team) - I was using [headless linux client](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux_NoVis.zip) to be able to run it seamlesly on any environment (even without display)

## Python packages
- torch 
- numpy 
- tqdm
- matplotlib
- unityagents

# Usage
## Training
```bash
python3 train.py
```

 # Details
Implementation uses DDPG algorithm - the details and metrics can be found in [report](./Report.md) file.