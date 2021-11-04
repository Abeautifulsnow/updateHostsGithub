# updateHostsGithub

A script to automatically update the github's proxy IP in hosts file. Now only Mac and Linux are supported. (脚本自动更新本地hosts文件,目前仅支持Mac和linux系统。)

## Reference

The data comes from this repository - [GitHub520](https://github.com/521xueweihan/GitHub520).

## Usage(使用)

You need to have a python3 environment and use `python3 -m pip install -r requirements.txt` command to install  necessary third-party library.

## How to run it(如何运行)

```bash
python3 main.py
```

## Schedule it to run at any time(定时任务)

You need to create a crontab task to run it at any time. Such as:

```bash
0 */4 * * * echo [password] | sudo -S sh -c 'cd /Users/dapeng/Desktop/code/python3 && /Users/dapeng/.virtualenvs/py39/bin/python main.py >> crontask.log 2>&1'
```

I set this script to be run at **minute 0 past every 4th hour.**

## Crontab Syntax(Crontab 语法)

|Field|Description|Allowed Value|
|-|-|-|
|MIN|Minute field|0 to 59|
|HOUR|Hour field|0 to 23|
|DOM|Day of Month|1 to 31|
|MON|Month field|1 to 12|
|DOW|Day Of Week|0 to 6|
|CMD|Command|Any command to be executed.|

There are some usefull websites:

- https://www.geeksforgeeks.org/crontab-in-linux-with-examples/ - crontab examples and grammar focus.
- https://crontab.guru/ - Grammar Checking.
