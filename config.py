# coding: UTF-8
'''''''''''''''''''''''''''''''''''''''''''''''''''''
   file name: config.py
   create time: 2017年06月25日 星期日 10时56分55秒
   author: Jipeng Huang
   e-mail: huangjipengnju@gmail.com
   github: https://github.com/hjptriplebee
'''''''''''''''''''''''''''''''''''''''''''''''''''''
import tensorflow as tf
import numpy as np
import argparse
import os
import random
import time
import collections

batchSize = 64

learningRateBase = 0.001
learningRateDecayStep = 1000
learningRateDecayRate = 0.95

epochNum = 10                    # train epoch
generateNum = 5                   # number of generated poems per time

type = "poetryAll"                   # dataset to use, shijing, songci, etc
trainPoems = "../data/" + type + "/" + type + ".txt" # training file location
checkpointsPath = "./checkpoints/" + type # checkpoints location

saveStep = 1000                   # save model every savestep



# evaluate
trainRatio = 0.8                    # train percentage
evaluateCheckpointsPath = "./checkpoints/evaluate"

characters = ['笑傲江湖','生日快乐']