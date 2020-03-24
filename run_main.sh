#export CUDA_VISIBLE_DEVICES=0
#mkdir log
#nohup /root/anaconda3/envs/pytorch/bin/python3.6 main.py -m train >> log/train.log 2>&1 &
#nohup /root/anaconda3/envs/pytorch/bin/python3.6 main.py -m test >> log/test.log 2>&1 &
#nohup /root/anaconda3/envs/pytorch/bin/python3.6 main.py -m head >> log/head.log 2>&1 &

export CUDA_VISIBLE_DEVICES=1
nohup /root/anaconda3/envs/pytorch/bin/python3.6 main.py -m train >> log/train-emb.log 2>&1 &