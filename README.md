# UCS420 - Cognitive Computing

My assignment solutions for UCS420.

Name: Vishu Verma

Roll number: 1024170242

| Folder | Topic |
| --- | --- |
| assignment-2 | Python data structures (lists, tuples, sets, dictionaries) |
| assignment-3 | Pandas basics, Iris dataset, employees dataset |
| assignment-4 | FAQ system using Pandas (Nova 2.0) |
| assignment-5 | NumPy intro (arrays, indexing, reshape, resize) |
| assignment-6 | NumPy II (vectorization, axis, views vs copies, least squares) |
| assignment-7 | NLP I (text preprocessing of IT support tickets with NLTK and regex) |
| assignment-8 | NLP II (BoW, TF-IDF, similarity, sentiment analysis, LSTM text generation) |
| assignment-9 | Vision based cognitive system (medicine label reader, emotion-aware assistant) |
| assignment-10 | Healthcare cognitive assistant (Heart Health Information Assistant) |

The question papers are in `assignment-papers/`.

## Notes

- Assignment 2: Q3 uses my roll number as the random seed. Q2 and Q4 take input, I used 40 and 28.
- Assignment 3: `Iris.csv` is the Kaggle iris dataset. Q6 creates `employees.csv` and saves `employees_modified.csv`.
- Assignment 4: last two digits of my roll number are 4 and 2, so my two entries are in account and general. Q4 takes input, I used `otp`. Data is saved to `1024170242_faq_data.csv`.
- Assignment 6: predicted score for the new user in Q4 is 75.28.
- Assignment 7: uses the starter notebook from Colab. My roll number gives 14 tickets with fingerprint `28B1E1DF`. The dataset is saved in `1024170242_generated_dataset.csv`.
- Assignment 8: paragraph is about cricket, reviews are for a food delivery app. The paper says Lab Assignment 10 on top but it was given as assignment 8.
- Assignment 9: medicine bottle photos are from Wikimedia Commons (`medicine_labels/`), faces are 140 images from the FER-2013 test set (`faces/`). OCR is done with EasyOCR and emotions with the FER+ ONNX model, which the notebook downloads into `models/` on first run. 9/10 medicines identified, emotion accuracy 47.86%.
- Assignment 10: my roll number is even, so it is the Heart Health Information Assistant. Corpus has 175 queries in 7 intents, classifier is TF-IDF + Logistic Regression (test accuracy 0.705, 5-fold CV 0.79). The chat cell takes input, type `exit` to stop.

## Running

Needs numpy and pandas. Assignment 7 also needs nltk and matplotlib.
Assignment 8 needs nltk, scikit-learn, textblob, wordcloud and tensorflow. Assignment 9 needs opencv-python (version 4.x) and easyocr. Assignment 10 needs nltk, scikit-learn, matplotlib and networkx.
Run each notebook from its own folder so the csv files are found.
