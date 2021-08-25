# Stanford-Dogs-Dataset-Parser
Easy way to parse Stanford dogs dataset and have it ready to train on tensorflow or add more images and regenrate the dataset
Requirments:
- tqdm
- python3
Steps to run parser. (run all commands from root directory)
1. run `sh ./src/setup/creatPaths.sh`
2. run `sh ./src/setup/downloadStanfordDataset.sh`
3. run `python3 -m src.parser`


