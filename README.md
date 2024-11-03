# -Papertrail-archives-downloader

This Python script enables you to download Papertrail log archives for a specified date range. By setting the start and end dates, you can quickly retrieve logs from a particular timeframe, making it easy to analyze and review relevant log data as needed. Simply input the desired date range, and the script will handle the rest, fetching and organizing the logs for your convenience.


example : 

```{r, engine='bash', count_lines}
$ pip install -r requirements.txt
$ python download.py --start 2023-03-28 --end 2023-04-02 -t {yourToken} -o ./logs/
$ find logs -type f -print0 | xargs -0 grep -rE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
```
