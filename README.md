# UCS420 — Cognitive Computing

Assignment solutions.

Name: **Vishu Verma**  ·  Roll number: **1024170242**

| Folder | Topic |
| --- | --- |
| [`assignment-2/`](assignment-2/) | Python data structures — lists, tuples, sets, dictionaries |
| [`assignment-3/`](assignment-3/) | Pandas — DataFrames, indexing, CSV files, employee dataset |
| [`assignment-4/`](assignment-4/) | A cognitive FAQ system using Pandas (Nova 2.0) |
| [`assignment-5/`](assignment-5/) | NumPy — array creation, indexing, reshape, resize |
| [`assignment-6/`](assignment-6/) | NumPy II — vectorization, axis sums, views vs copies, least squares |
| [`assignment-7/`](assignment-7/) | NLP I — preprocessing IT-support tickets with NLTK and regex |
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

## Assignment 6 — NumPy II

[`assignment-6/Assignment_6_NumPy_II.ipynb`](assignment-6/Assignment_6_NumPy_II.ipynb)

| Q | Topic |
| --- | --- |
| 1 | Sensor readings — +2°C correction, Celsius → Fahrenheit, Boolean mask for readings above 32°C, loop vs vectorized timing |
| 2 | Step counts — total, mean, max/min, `axis=0` per day, `axis=1` per user, `argmax` + `unravel_index` |
| 3 | Views vs copies — slicing, `.copy()`, `arange().reshape(3, 4)`, `flatten()` vs `ravel()`, array attributes |
| 4 | Ordinary least squares — `X.T`, `X.T @ X`, `np.linalg.inv`, β = (XᵀX)⁻¹Xᵀy, prediction for a new user |

Q1 works on the corrected readings (5 above 32°C) and also shows the raw count (4).
The OLS fit gives β ≈ [−0.16, +0.14, +10.06] for sleep, activity and stress, checked against
`np.linalg.lstsq`. The new user `[5, 40, 7]` gets a predicted score of **75.28**.

## Assignment 7 — NLP I

[`assignment-7/Assignment_7_NLP_I.ipynb`](assignment-7/Assignment_7_NLP_I.ipynb)

Built on the official starter notebook (`UCS420_LA9_Starter.ipynb`); `generate_dataset()` and
`process_ticket()` are unchanged. Roll number `1024170242` gives **14 tickets**, fingerprint
**`28B1E1DF`**, focus tickets T07 and T10. The generated tickets are saved in
`1024170242_generated_dataset.csv`.

| Q | Topic |
| --- | --- |
| 1 | Per-ticket table of sentences, tokens, punctuation, stopwords, unique and final tokens with a TOTAL row; full breakdown of T07 |
| 2 | `re.findall` for long words, numbers (95.5, 2.0.1), capitalized and vowel-initial words; `re.sub` for `<EMAIL>`, `<URL>`, `<PHONE>` |
| 3 | `my_tokenize()` — one `RegexpTokenizer` pattern for contractions, hyphens, decimals, versions, emails, URLs, phones; compared with `word_tokenize()` |
| 4 | Porter vs Lancaster vs Regexp (`ing$`) vs POS-aware WordNet lemmatizer — table of the 31 words where they differ |
| 5 | Tokens / unique / TTR for S1–S4, top-10 words, Zipf log-log plot, top-5 bigrams |
| 6 | Interpretation — TTR trend, tokenizer difference, bad stemming, lemmatization vs stemming |

---

Needs `pandas` and `numpy`; Assignment 7 also needs `nltk` and `matplotlib` (the first cell downloads the NLTK data). Run each notebook from inside its own folder so the CSV paths resolve.
