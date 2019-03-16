# generate-random-numbers-subject-to-the-specified-distribution
# 生成服从指定分布的随机数


在项目中需要用到生成指定分布的随机数，查找了一些方法，分享如下：

###  一、基础算法 

* 1.Inverse Transform Method 

    最简单的生成算法是Inverse Transform Method（下文简称ITM）。如果我们可以给出概率分布的累积分布函数（下文简称CDF）及其逆函数的解析表达式，则可以非常简单便捷的生成指定分布随机数。

    #### ITM算法描述 

```
    生成一个服从均匀分布的随机数U∼Uni(0,1) ;
    设F(X)为指定分布的CDF，F−1(Y)是其逆函数;
    返回X=F−1(U)作为结果
    
 ```

* 2.Acceptance-Rejection Method 

    一般来说ITM是一种很好的算法，简单且高效，如果可以使用的话，是第一选择。但是ITM有自身的局限性，就是要求必须能给出CDF逆函数的解析表达式，有些时候要做到这点比较困难，这限制了ITM的适用范围。

    当无法给出CDF逆函数的解析表达式时，Acceptance-Rejection Method（下文简称ARM）是另外的选择。ARM的适用范围比ITM要大，只要给出概率密度函数（下文简称PDF）的解析表达式即可，而大多数常用分布的PDF是可以查到的。

    #### ARM算法描述 

```
    设PDF为f(x);
    首先生成一个均匀分布随机数X∼Uni(xmin,xmax) ,独立的生成另一个均匀分布随机数Y∼Uni(ymin,ymax) ;
    如果Y≤f(X)，则返回X，否则回到第1步
```



*参考文献*

    http://blog.codinglabs.org/articles/methods-for-generating-random-number-distributions.html -https://github.com/sea-boat/MachineLearning_Lab/blob/master/distribution_gen.py
