# 爬取途牛、携程、去哪儿机票信息

### 环境

1.  python3
2.  selenium
3.  mysql(数据库名字 air_ticket, 表结构在 res 文件夹下)
4.  firefox(win 平台下的驱动在 res 下, linux 需要重新配置)

### 运行

1.  发布运行

    ```
    python app.py
    ```

    无界面模式爬取数据,每次间隔 config.INTERVAL_TIME 时间获取一次机票信息

2.  开发运行
    ```
    python app_dev.py -h -t '2018-03-28'
    ```
    开发模式运行程序,-h 参数无界面模式,-t 指定获取的机票时间,运行一次不重复获取
