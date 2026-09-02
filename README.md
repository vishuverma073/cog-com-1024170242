# UCS420 — Cognitive Computing

Assignment solutions.

Name: **Vishu Verma**  ·  Roll number: **1024170242**

| Folder | Topic |
| --- | --- |
| [`assignment-2/`](assignment-2/) | Python data structures — lists, tuples, sets, dictionaries |
| [`assignment-3/`](assignment-3/) | Pandas — DataFrames, indexing, CSV files, employee dataset |
| [`assignment-4/`](assignment-4/) | A cognitive FAQ system using Pandas (Nova 2.0) |
| [`assignment-5/`](assignment-5/) | NumPy — array creation, indexing, reshape, resize |
| [`assignment-papers/`](assignment-papers/) | The original question papers (PDF) |

Every notebook is saved with its outputs, so the answers can be read without running anything.

---

## Assignment 2 — Python Data Structures

[`assignment-2/Cognitive_comp.ipynb`](assignment-2/Cognitive_comp.ipynb)

| Q | Topic |
| --- | --- |
| 1 | Lists — build `L` from the roll digits, append/insert/remove/pop, sort, slice, comprehension |
| 2 | Tuples — max/min, reversing, searching, immutability error, `*` unpacking |
| 3 | Random — 100 seeded numbers, odds, evens, primes, most frequent |
| 4 | Sets — union, intersection, difference, symmetric difference, subset/superset, discard |
| 5 | Dictionaries — rename key, add/update, `pop` vs `del`, iteration, merging, comprehension |

Question 3 seeds `random` with the roll number, so the same 100 numbers come out on every run.
Questions 2 and 4 ask for input; the saved run used `40` and `28`.

## Assignment 3 — Pandas

[`assignment-3/Assignment_3_Pandas.ipynb`](assignment-3/Assignment_3_Pandas.ipynb)

| Q | Topic |
| --- | --- |
| 1 | Build the Tid / Refund / Marital Status / Taxable Income / Cheat DataFrame |
| 2 | Locate rows 0, 4, 7, 8 with `loc` |
| 3 | Navigate with `loc` and `iloc` — row and column slices |
| 4 | Read `Iris.csv` and show the first five rows |
| 5 | Drop row 4 and column 3 from the Iris data |
| 6 | `employees.csv` — shape, `info`, `describe`, statistics, sorting, rating categories, missing values, rename, filtering, `Tax` column, save to CSV |

Data files: `Iris.csv` (same columns as the Kaggle `uciml/iris` download, used by Q4 and Q5),
`employees.csv` (written by Q6), `employees_modified.csv` (written by Q6l with the `Performance`
and `Tax` columns added).

## Assignment 4 — Cognitive FAQ System

[`assignment-4/Assignment_4_FAQ_System.ipynb`](assignment-4/Assignment_4_FAQ_System.ipynb)

| Q | Topic |
| --- | --- |
| 1 | 6-row knowledge base — 4 fixed entries plus 2 built from the last two roll digits |
| 2 | Scoring function — every matching entry, ranked by confidence |
| 3 | `same_category(category_name, df)` |
| 4 | Add a keyword from user input, save to `1024170242_faq_data.csv` |
| 5 | Entries per category with `groupby` |
| 6 | Scoring that prints every entry tied for the best score |

The last two digits of `1024170242` are 4 and 2, so the personalised entries land in
**account** (`4 % 3 = 1`) and **general** (`2 % 3 = 2`). The scorer drops filler words like
"how" and "my" before matching, otherwise every entry would look like a match.
Q4 asks for input; the saved run used `otp`.

## Assignment 5 — NumPy

[`assignment-5/Assignment_5_NumPy.ipynb`](assignment-5/Assignment_5_NumPy.ipynb)

| Q | Topic |
| --- | --- |
| 1 | 1-D array of 5 elements — add 2, multiply by 3, divide by 2 |
| 2 | Reverse an array; most frequent value and its indices (`y` has a tie, both are reported) |
| 3 | Access a 2-D array by row and column index |
| 4 | `vishu` — `linspace` of 25 values, array attributes, transpose via `reshape` vs `T` |
| 5 | `ucs420_vishu` — mean, median, max, min, unique, `reshape` to 4×3, `resize` to 2×3 |

---

Needs `pandas` and `numpy`. Run each notebook from inside its own folder so the CSV paths resolve.
