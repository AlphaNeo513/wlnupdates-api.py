<!-- Source: https://github.com/MattIPv4/template/blob/master/README.md -->

<!-- Title -->
<h1 align="center" id="wlupdatesapipy">
    wlnupdates-api.py
</h1>

<!-- Tag line --> 
<h3 align="center">A simple API wrapper for wlnupdates to get json data based on ID.</h3>


----

<!-- Content -->
## Installation

Install via pip (recommended)

```Shell
pip install wlnupdates
```
## Wrapper
All Wrapper functions only accepts ID as param
Wrapper param | Value | Description
------------ | ------------- | -------------
ID | String **(optional)** | ID for the novel/series you're requesting


```Python
from wlnupdates import Wrapper

data = Wrapper()

print(data.get_series_data('3')

```
## Search
title_search param | Value | Description
------------ | ------------- | -------------
name | String **(required)** | Name for the novel/series you're requesting
similarityNum | Float **(optional)** | This param will output any lists with a value above the number you entered.
fullList | Boolean **(optional)** | If true, will output clean list with match(similarity num, name) and sid(series ID)

### Usage for Search
```Python
from wlnupdates import Search

data = Search()

print(data.title_search(name, similarityNum=0, fullList=False))
```


## Contributing

Contributions are always welcome!\
Take a look at any existing issues on this repository for starting places to help contribute towards, or simply create your own new contribution to the project.

When you are ready, simply create a pull request for your contribution and we will review it whenever we can!


* If you have an issue, please create a GitHub issue here to report it, include as much detail as you can.
