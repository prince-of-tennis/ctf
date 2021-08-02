# Regex Problems Solutions on RegexOne
starting from here:
https://regexone.com/problem/matching_decimal_numbers

Technically, the website has their own solutions, but I'd like to keep mine here as well for comparison purposes. Of course, the website solutions are much more effective in covering the nuances of user input.

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
