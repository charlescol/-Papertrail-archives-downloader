# -Papertrail-archives-downloader

This Python script, created on April 7, 2023, allows you to download Papertrail archives between two specific dates. 
With this script, you can easily retrieve logs for a specific time frame and analyze them as needed. Simply specify the start and 
end dates in the script and let it do the work for you. 
This script is a useful tool for anyone who needs to access Papertrail archives and wants to automate the retrieval process.


example : 

```{r, engine='bash', count_lines}
$ python download.py --start 2023-03-28 --end 2023-04-02 -t fQvvhjA9q4qWhzEsAS3k -o ./logs/
$ find logs -type f -print0 | xargs -0 grep -rE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
```
