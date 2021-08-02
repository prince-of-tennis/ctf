# Regex Problems Solutions on RegexOne
starting from here:
https://regexone.com/problem/matching_decimal_numbers

Technically, the website has their own solutions, but I'd like to keep mine here as well for comparison purposes. Of course, theirs are much more effective in covering the nuances of user input. My solutions just happen to work on these problems.

The first solution is mine, while the second one is from the website. If there is only one solution here, that means I got the same regex as the website! 

## 1. Matching a decimal numbers

 my sol: ```^-?\d+,?\d*\.?\d+e?\d+$```

website sol: ```^-?\d+(,\d+)*(\.\d+(e\d+)?)?$```

## 2. Matching Phone Numbers
```1?[\s]?\(?(\d{3})\)?[ -]?\d{3}[ -]?\d{4}```

```1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}```

## 3. Matching emails
```(\w+\.?\w+)```

```^([\w\.]*)```

## 4. Matching HTML
```<(\w+\b)```

```<(\w+)```

## 5. Matching specific filenames
```(\w+)\.(png|jpg|gif)$```

## 6. Trimming whitespace from start and end of line
```^\s+(.*)$```

``` ^\s*(.*)\s*$```

## 7. Extracting log data
My solution for this one is ridiculously specific, which is not a good thing since some things would probably change in a log file.

```E/\( 1553\):\s*at widget\.List\.(\w+)\((\w+\.\w+):(\d+)\)$```

```(\w+)\(([\w\.]+):(\d+)\)```

## 8. Parsing and extracting data from a URL
Probably my favorite challenge so far.
```(\w+)://([\w-]+\.?\w+):?(\d+)?```

```(\w+)://([\w\-\.]+)(:(\d+))?```
