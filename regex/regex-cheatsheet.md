# Regex Cheatsheat
by prince_of_tennis

## Intro
Regex or regular expressions is a format for creating patterns to match text. This has a lot of applications in multiple CTF-type problems and in CS problems as well.

I'm basing this off of what I learn from: https://regexone.com/.

Practice problems here: https://regexone.com/problem/matching_decimal_numbers

A cool link for learning and testing regex is: https://regexr.com/

## General rules
* characters usually can match anywhere in string - BE AS SPECIFIC AS POSSIBLE
* regex is case-sensitive

## Cheatsheet

### misc

```[abc]``` match either an a, b, or c in the space of one character 

```[^abc]``` match any single character except a, b, or c

```[a-z]``` dashes represent character ranges 

```a{m}``` m repetitions of ```a``` 
* can be used with any character, for example ```[abc]{3}```

```a{m,n}``` m-n repetitions of ```a```

```a*``` zero or more ```a```

```a+``` one or more ```a```

```a?``` optional character
* for example, ```an?t``` matches ```ant``` and ```at``` since ```n``` is optional

```^randomtext$``` specify beginning and end of text to match
* different from ```[^a]``` which exists only with square brackets

### special

```.``` is wildcard (matches every character)

```\``` to escape (escape character)
* ```\.``` to match a period
* ```\?``` for a question mark

```\d``` for 0-9

```\D``` for non-digits

```\w``` for alphanumeric characters, equivalent to ```[A-Za-z0-9]```

```\W``` for any non-alphanumeric character

```\b``` for empty string at beginning or end of word
* usually for capturing whole words like ```\w+\b```
* for example, take the sentence: ```The cat scattered his food.``` The regex ```\bcat\b``` will match the word ```cat``` but not the ```cat``` in ```scattered```.

```\B``` for empty strings not at beginning or end of word

### whitespace

``` ``` literally a space

```\t``` tab

```\n``` newline

```\r``` carriage return

```\s``` any whitespace

```\S``` any non-whitespace

### capture text

```(text)``` capture group within parantheses
* for example, ```^(IMG\d+\.png)$``` to get filenames with .png extension, ```^(IMG\d+)\.png$``` to get it without
* another example, to get numbers from ```2400x1600```, we can do ```(\d+)x(\d+)```

```(a(bc))``` capture nested groups
* for example, to get two groups like ```May 1968``` and ```1968``` from ```May 1968```, we could do ```([A-Z][a-z]+ (\d{4}))```

```(.*)``` capture all

```(cat|dog)``` matches ```cat``` or ```dog```

### back referencing - depends on implementation
The idea is to reference your captured groups.

```\0``` full matched text

```\1``` your first group

```\2``` your second group

... and so on

## More References
https://stackoverflow.com/questions/6664151/difference-between-b-and-b-in-regex
https://regexone.com/lesson/misc_meta_characters?



