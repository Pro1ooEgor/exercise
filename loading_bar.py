from tqdm import trange, tqdm
import time

for i in tqdm(range(10)):
    # print(i)
    time.sleep(1)


for i in trange(10):
    # print(i)
    time.sleep(1)
