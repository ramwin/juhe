# juhe

# Install

    sudo pip3 install juhe
    from juhe import API


# Usage

* [汇率](https://www.juhe.cn/docs/api/id/80)

    ```
    API().query_exchange("输入你的Key")
    >>>
    {
    '加拿大元': {   '中行折算价': '521.49',
                '交易单位': '100',
                '现汇买入价': '517.59',
                '现钞买入价': '502.79',
                '现钞卖出价': '521.49',
                '货币名称': '加拿大元'},
    '新西兰元': {   '中行折算价': '462.26',
                '交易单位': '100',
                '现汇买入价': '458.81',
                '现钞买入价': '445.69',
                '现钞卖出价': '465.02',
                '货币名称': '新西兰元'},
    '日元': {   '中行折算价': '5.9834',
              '交易单位': '100',
              '现汇买入价': '5.9381',
              '现钞买入价': '5.7683',
              '现钞卖出价': '5.9834',
              '货币名称': '日元'},
    '欧元': {   '中行折算价': '780.75',
              '交易单位': '100',
              '现汇买入价': '775.54',
              '现钞买入价': '753.13',
              '现钞卖出价': '780.75',
              '货币名称': '欧元'},
    '港币': {   '中行折算价': '84.23',
              '交易单位': '100',
              '现汇买入价': '83.89',
              '现钞买入价': '83.3',
              '现钞卖出价': '84.23',
              '货币名称': '港币'},
    '澳大利亚元': {   '中行折算价': '501.03',
                 '交易单位': '100',
                 '现汇买入价': '497.28',
                 '现钞买入价': '483.06',
                 '现钞卖出价': '501.03',
                 '货币名称': '澳大利亚元'},
    '瑞典克朗': {   '中行折算价': '76.34',
                '交易单位': '100',
                '现汇买入价': '75.77',
                '现钞买入价': '73.61',
                '现钞卖出价': '76.34',
                '货币名称': '瑞典克朗'},
    '瑞士法郎': {   '中行折算价': '706.86',
                '交易单位': '100',
                '现汇买入价': '701.58',
                '现钞买入价': '681.51',
                '现钞卖出价': '706.86',
                '货币名称': '瑞士法郎'},
    '美元': {   '中行折算价': '655.7',
              '交易单位': '100',
              '现汇买入价': '653.02',
              '现钞买入价': '648.44',
              '现钞卖出价': '655.7',
              '货币名称': '美元'},
    '英镑': {   '中行折算价': '907.31',
              '交易单位': '100',
              '现汇买入价': '900.54',
              '现钞买入价': '874.78',
              '现钞卖出价': '907.31',
              '货币名称': '英镑'},
    '韩元': {   '中行折算价': '0.604',
              '交易单位': '100',
              '现汇买入价': '0.583',
              '现钞买入价': '0.5666',
              '现钞卖出价': '0.604',
              '货币名称': '韩元'}}
    ```

* [笑话](https://www.juhe.cn/docs/api/id/95)

    api.get_jokes(key)
    >>> 
        [
            "高中一班主任陈老师，因其身高比较矮，同学给起了个外号叫“武大郎”，后来被老师得知，要求同学带家长，同学跟家里说了原委，家长带着同学到老师办公室致歉，该同学家长进门就说:“武老师，小孩子不懂事，还忘您能海涵”，后来同学告诉我们班主任当时那表情都抽搐了，足足让我们笑了一学期。",
            "…给闺女买了一双小皮鞋，花了两张毛爷爷，小鞋很结实，闺女穿了好多天后要我给她买鞋，说不喜欢了，我就各种教育，比如要穿破之后买，要知道省钱……等等。今天再回去的时候，姑娘左手拎着残破的鞋子，右手拿着剪刀，跑过来说:爸爸，现在可以买新的鞋子了吧！来，过来，爸爸保证不打你，我的亲闺女。",
        ]
