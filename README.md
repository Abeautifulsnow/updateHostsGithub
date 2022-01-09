# updateHostsGithub

A script to automatically update the github's proxy IP in hosts file. Now only Mac and Linux are supported.

## 1 Reference

The data comes from this repository - [GitHub520](https://github.com/521xueweihan/GitHub520).

## 2 Usage

You need to have a python3 environment and use `python3 -m pip install -r requirements.txt` command to install necessary third-party libraries.

## 3 How to run it

Before you run this script, you need to export `PYHTONPATH` variable to global environment.

### 3.1 Linux or MacOS

```bash
export PYHTONPATH=[your local current project root path.]
```

```bash
python3 main.py
```

#### 3.1.1 Schedule it to run at any time

You need to create a crontab task to run it at any time. Such as:

```bash
0 */4 * * * echo [password] | sudo -S sh -c 'cd /Users/dapeng/Desktop/code/python3 && /Users/dapeng/.virtualenvs/py39/bin/python main.py >> crontask.log 2>&1'
```

I set this script to be run at **minute 0 past every 4th hour.**

#### 3.1.2 Crontab Syntax

|Field|Description|Allowed Value|
|-|-|-|
|MIN|Minute field|0 to 59|
|HOUR|Hour field|0 to 23|
|DOM|Day of Month|1 to 31|
|MON|Month field|1 to 12|
|DOW|Day Of Week|0 to 6|
|CMD|Command|Any command to be executed.|

There are some useful websites:

- [crontab-in-linux-with-examples](https://www.geeksforgeeks.org/crontab-in-linux-with-examples/) - crontab examples and grammar focus.
- [crontab.guru](https://crontab.guru/) - Grammar Checking.

### 3.2 Windows

1. [Right Click]Computer > Properties >Advanced System Settings > Environment Variables
2. Click [New] under "System Variable"
3. Variable Name: **PYHTONPATH**, Variable Value: [your local current project root path]
4. Click [OK] and exit the **Settings Window**.

[your local current project root path]: ""

```bash
python3 main.py
```

#### 3.2.1 Schedule it to run at any time

You can reference this article: [schedule-tasks-windows-10](https://windowsreport.com/schedule-tasks-windows-10/) or [scheduled-task-windows](https://www.technipages.com/scheduled-task-windows) to create a cron task.
