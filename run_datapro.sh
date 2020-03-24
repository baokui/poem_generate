path_source=/search/odin/guobk/vpa/Poetry-master
path_target=./data/poetryAll.txt
mode=rawPeom
#nohup python -u datapro.py $mode $path_source $path_target >> log/datapro.log 2>&1 &

path_source=../data/poetryAll/poetryAll.txt
path_target_shi=../data/poetryAll_shi/poetryAll_shi.txt
path_target_ci=../data/poetryAll_ci/poetryAll_ci.txt
mkdir ../data/poetryAll_shi
mkdir ../data/poetryAll_ci
mode=seprate
nohup python -u datapro.py $mode $path_source $path_target_shi $path_target_ci >> log/datapro-sep.log 2>&1 &