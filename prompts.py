PROMPT_SMALL = """You are an expert software developer and version control specialist.
Your task is to summarizes a commit using file diffs following the instructions and example.

## Output example

The change addresses an issue where the subscription is not processed normally after a SIM is turned off and a FOTA update occurs.

Modified files:
src/DataSources/Amazon/AmazonClient.cs
* Added a check to ensure that the subscription ID of the new handle matches the provided subscription ID.


## Input
<diffs>
{diffs}
</diffs>
"""

PROMPT_MEDIUM = """You are an expert software developer and version control specialist.
Your task is to summarizes a commit using file diffs following the instructions and example.
The code diff of the file is described like (for example):
```
src/DataSources/Amazon/AmazonClient.cs (modified)
---@@ -836,7 +836,7 @@
     <dimen name="qrcode_popup_background_radius">26dp</dimen>
     <dimen name="qrcode_popup_single_line_background_radius">18dp</dimen>
     <dimen name="qrcode_popup_single_line_icon_margin">6dp</dimen>
-    <dimen name="qrcode_popup_single_line_title_text_size">12dp</dimen>
+    <dimen name="qrcode_popup_single_line_title_text_size">14dp</dimen>
     <dimen name="qrcode_popup_single_line_title_line_height">23dp</dimen>
     <dimen name="qrcode_popup_single_line_title_icon_start_margin">14dp</dimen>
     <dimen name="qrcode_popup_single_line_title_arrow_margin">10dp</dimen>
---
```

It means `Camera/src/main/res/values/dimensions.xml` was added, modified or deleted in this commit.
Then there is a specifier of the lines that were modified.
A line starting with `+` means it was added.
A line that starting with `-` means that line was deleted.
A line that starts with neither `+` nor `-` is code given for context and better understanding.


## Output example

The change addresses an issue where the subscription is not processed normally after a SIM is turned off and a FOTA update occurs.

Modified files:
src/DataSources/Amazon/AmazonClient.cs
* Added a check to ensure that the subscription ID of the new handle matches the provided subscription ID.


## Input
<diffs>
{diffs}
</diffs>
"""


PROMPT_LARGE = """You are a senior software engineer specialized in version control.
Your task is to generate a concise, informative commit message based on the provided diffs.
The code diff of the file is described like (for example):
```
src/DataSources/Amazon/AmazonClient.cs (modified)
---@@ -836,7 +836,7 @@
     <dimen name="qrcode_popup_background_radius">26dp</dimen>
     <dimen name="qrcode_popup_single_line_background_radius">18dp</dimen>
     <dimen name="qrcode_popup_single_line_icon_margin">6dp</dimen>
-    <dimen name="qrcode_popup_single_line_title_text_size">12dp</dimen>
+    <dimen name="qrcode_popup_single_line_title_text_size">14dp</dimen>
     <dimen name="qrcode_popup_single_line_title_line_height">23dp</dimen>
     <dimen name="qrcode_popup_single_line_title_icon_start_margin">14dp</dimen>
     <dimen name="qrcode_popup_single_line_title_arrow_margin">10dp</dimen>
---
```
---

# Commit Message Format

## Summary line (1st line):

- Summarize the commit in one sentence (max 72 characters).
- Use imperative tone (e.g., Fix bug, Add feature, Refactor logic).
- Do not use punctuation at the end.

## Modified Files section:

- Use the exact format below.
- List each file path on its own line (no bullets).
- Indent each change description under the file using - (asterisk + space).
- Be specific and use technical language (mention functions, methods, or logic changed).

---

## Output Format:

<summary line>

Modified files:

<file path>
* <description>
* <description>

<file path>
* <description>

---

## Example:
 
The change addresses an issue where the subscription is not processed normally after a SIM is turned off and a FOTA update occurs.

Modified files:

src/DataSources/Amazon/AmazonClient.cs
* Added a check to ensure that the subscription ID of the new handle matches the provided subscription ID.
 
 
---
 
## Input:
 
<diffs>
{diffs}
</diffs>
"""

TEMPLATE_DIFF = """
You are an expert software developer and version control specialist.
Your task is to analyze the file diff and generate a clear, concise, and meaningful commit message that summarizes the file diff.
<diff> has code diff of a file.
The code diff of the file is described like (for example):
```
src/DataSources/Amazon/AmazonClient.cs (modified)
---@@ -836,7 +836,7 @@
     <dimen name="qrcode_popup_background_radius">26dp</dimen>
     <dimen name="qrcode_popup_single_line_background_radius">18dp</dimen>
     <dimen name="qrcode_popup_single_line_icon_margin">6dp</dimen>
-    <dimen name="qrcode_popup_single_line_title_text_size">12dp</dimen>
+    <dimen name="qrcode_popup_single_line_title_text_size">14dp</dimen>
     <dimen name="qrcode_popup_single_line_title_line_height">23dp</dimen>
     <dimen name="qrcode_popup_single_line_title_icon_start_margin">14dp</dimen>
     <dimen name="qrcode_popup_single_line_title_arrow_margin">10dp</dimen>
---
```

It means `Camera/src/main/res/values/dimensions.xml` was added, modified or deleted in this commit.
Then there is a specifier of the lines that were modified.
A line starting with `+` means it was added.
A line that starting with `-` means that line was deleted.
A line that starts with neither `+` nor `-` is code given for context and better understanding.


## Follow these guidelines:
- Summarize the commit in one sentence (max 72 characters).
- Use imperative tone (e.g., Fix bug, Add feature, Refactor logic).
- Do not use punctuation at the end.


## Input
<diff>
{diff}
</diff>
"""

PROMPT_SUMMARIZE_DIFFS = """
You are an expert software developer and version control specialist.
Your task is to analyze the all summaries and generate a clear, concise, and meaningful commit message based on all summaries.

# Commit Message Format

## Summary line (1st line):

- Summarize the commit in one sentence (max 72 characters).
- Do not show any code in the commit message
- Use imperative tone (e.g., Fix bug, Add feature, Refactor logic).


## Modified Files section:

- List each file path on its own line (no bullets).
- Indent each change description under the file using - (asterisk + space).
- Be specific and use technical language (mention functions, methods, or logic changed).

---

## Output Format:

<summary line>

Modified files:

<file path>
* <description>
* <description>

<file path>
* <description>

---

## Example:
 
The change addresses an issue where the subscription is not processed normally after a SIM is turned off and a FOTA update occurs.

Modified files:

src/DataSources/Amazon/AmazonClient.cs
* Added a check to ensure that the subscription ID of the new handle matches the provided subscription ID.


## Input

{summaries}
"""
