path_source=/search/odin/guobk/vpa/Poetry-master
path_target=./data/poetryAll.txt
mode=rawPeom
nohup python -u datapro.py $mode $path_source $path_target >> log/datapro.log 2>&1 &