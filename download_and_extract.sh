wget http://files.srl.inf.ethz.ch/data/py150_files.tar.gz

mkdir py150_files
tar -C py150_files -zxvf py150_files.tar.gz
rm py150_files.tar.gz

cd py150_files
tar -zxvf data.tar.gz
rm data.tar.gz
