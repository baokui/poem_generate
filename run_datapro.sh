path_source=/search/odin/guobk/vpa/Poetry-master
path_target=./data
mode=rawPeom
mkdir data
nohup python -u datapro $mode $path_source $path_target >> log/datapro.log 2>&1 &