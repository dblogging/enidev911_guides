from pathlib import Path 

p = Path.cwd()
userpath = Path.home()
print(userpath)


def get_path(path: str) -> str:
	print(path+10)


get_path(10)