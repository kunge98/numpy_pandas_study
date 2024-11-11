if __name__ == '__main__':

    #有一组从2006年到2016年1000部最流行的电影数据，我们想知道这些电影数据中评分的平均分，导演的人数等信息，
    #我们应该怎么获取

    import pandas as pd
    import string

    file_path = pd.read_csv('./IMDB-Movie-Data.csv')
    df = pd.DataFrame(file_path)
    print(df.info())
    print(df.head(1))
    print(df['Rating'].mean())  #获取评分的均值

    print(len(set(df['Director'].tolist())))   #算出导演的个数 用set去重复
    print(len(df['Director'].unique()))   #与上面的set结果相同，unique就是独一无二的意思

    #打印演员的个数
    temp_actors_list = df['Actors'].str.split(', ').tolist()
    actors_list = [i for j in temp_actors_list for i in j]
    print(len(set(actors_list)))

