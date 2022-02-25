---
meta:
  author: Jon Doe
  topic: Samples
---

# A sample Markdown document

This is a sample document so you can preview the color schemes.

## Text Formatting

Markdown supports _italics_, **bold**, and _**bold italics**_ style using underscores. S Markdown supports _italics_, **bold**, and _**bold italics**_ style using asterisks.

There are also inline styles like `inline code in monospace font` and ~~strikethrough style~~.

**There may be **~~**strikethroughed text**~~** or `code text` inside bold text.**

_And There may be _~~_strikethroughed text_~~_ or `code text` inside italic text._

> **Here is some quotation**. Lorem ~~ipsum~~ dolor sit amet, consectetur\
> adipisicing elit, _sed_ do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim **ad** minim veniam, quis nostrud exercitation.
>
> `code block`

Inline key or ~~key~~ other **bold html** tags.

## Links and References

To reference something from a URL, [Named Links](https://example.com/index.html), [Inline links](https://example.com/index.html) and direct link like [https://example.com/](https://example.com) are of great help. Sometimes ![A picture](https://example.com/sample.png) is worth a thousand words.

***

This \[\[SamplePage]] is a wiki link.

## Lists

There are two types of lists, ordered and unordered.

1. Item 1 key
2. Item 2
3. Item 3
4. Item 1
5. Item 2
6. Item 3

* Item A
  * Sub list
    * Sub sub list
    * Sub sub list 2
  * Sub list 2
* Item B
* Item C

## Tables

| Col 1 | Col 2 |
| ----: | ----- |
|  what | else  |

## Code Blocks

Anything indented more than 3 characters is treated as raw code block.

```
function fibo(n) {
    fibo.mem = fibo.mem || []; // I am some comment
    return fibo.mem[n] || fibo.mem[n] = n <= 1 ? 1 : fibo(n - 1) + fibo(n - 2);
```

Fenced code blocks support syntax highlighting and are wrapped in triple backticks.

```javascript
function fibo(n) {
    fibo.mem = fibo.mem || []; // I am some comment
    return fibo.mem[n] || fibo.mem[n] = n <= 1 ? 1 : fibo(n - 1) + fibo(n - 2);
}
```

```diff
diff --git a/schemes/Preview.md b/schemes/Preview.md
index 3d4b1fe..a85a22a 100644
--- a/schemes/Preview.md
+++ b/schemes/Preview.md
@@ -89,6 +89,12 @@ function fibo(n) {
 
-## Deleted
+## Inserted
```

## CriticMarkup

This is {++ inserted ++} and {-- deleted --} or {== highlighted ==}{>> comment <<} text.

We can also {\~\~ substitute \~> something \~\~}.

## Reference Definitions

\[^1]: This is a footnote definition
