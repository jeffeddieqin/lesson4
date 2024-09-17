import sys
import re

def grep(pattern, file):
    try:
        with open(file, 'r') as f:
            for i, line in enumerate(f, 1):  # 使用enumerate时，起始索引为1
                if re.search(pattern, line):
                    print(f"{file}:{i}: {line}", end="")
    except FileNotFoundError:
        print(f"File not found: {file}")

if __name__ == '__main__':
    if len(sys.argv) < 4:  # 至少需要4个参数：脚本名、重复次数、模式和至少一个文件名
        print("Usage: python script.py <times> <pattern> <file> [...]")
        sys.exit(1)

    times = int(sys.argv[1])
    pattern = sys.argv[2]
    files = sys.argv[3:]

    for _ in range(times):
        for file in files:
            grep(pattern, file)