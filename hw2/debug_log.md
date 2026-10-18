# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
File "/Users/won23/hcde310 GitHub/hcde.310/hw2/part4.py", line 16, in works_by
    print(works_by("Claude Monet", artworks))
[Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded

### 2. What I thought it meant
that it was looping infinitely?

### 3. What it actually meant
the function called itself too many times

### 4. The fix
I looked back on terminal and saw that error later, so I'm not sure 
where the fix was exactly, but i believe with fixing the if statement 

## Entry 2

### 1. Error message
*copy it exactly*
 titles.append(artwork.get("title"))   
    ^^^^^^
IndentationError: expected an indented block after 'if' statement on line 18

### 2. What I thought it meant
indentation error, there must be somewhere I accidentally indented

### 3. What it actually meant
identation error

### 4. The fix
I fixed the indentation on line 18. Easy fix