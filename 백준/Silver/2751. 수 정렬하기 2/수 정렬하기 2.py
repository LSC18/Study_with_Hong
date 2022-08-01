import sys
N = int(sys.stdin.readline())
srt = []
for i in range(N):
    srt.append(int(sys.stdin.readline()))
srt = sorted(set(srt))
for i in srt:
    print(i)