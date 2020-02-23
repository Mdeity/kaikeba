 # 打乱数据集
import random
x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']

def shuffle(x,y):
    
    xy = list(zip(x,y))
   
    random.seed(1)     # 指定随机的种子

    random.shuffle(xy)

    x,y = zip(*xy)  # ('快递太慢了！', '差评')  ('很划算', '好评') ('不好吃', '差评')

    return x,y
    
x,y = shuffle(x,y)
for i,j in zip(x,y):
    print(i,':',j)
