# cae-vocabulary
This script is developed for generating dictionary for specific range of words. 

## Environment 

### Operating System 
This project is for Debian/Ubuntu. 

## Dependency 

### Install python3和bs4, lxml

Install python3
```bash
sudo apt-get install python3
sudo apt-get install python3-pip
```

Under this project root directory, Create Python Venv.

```bash
python3 -m venv .venv
```

Activate it. 
```bash
source .venv/bin/activate 
```

Install dependencies.
```bash
sudo pip3 install bs4
sudo pip3 install lxml
```

### Install WuDao 

```bash
git clone https://github.com/chestnutheng/wudao-dict
cd ./wudao-dict/wudao-dict
sudo bash setup.sh
```

## Run

1. Open project directory in terminal.
2. Prepare sample word list file and place it in $PROJ_ROOT$/data.

For example, the ./data/c2:  
```txt
vanillar
sugar
apple
```

3. In terminal under $PROJ_ROOT$, run 

```shell
python3 ./main.py 
```

