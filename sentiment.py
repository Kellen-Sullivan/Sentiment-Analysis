# CS331 Sentiment Analysis Assignment 3
# This file contains the processing functions

import sys
import string


def process_text(text):
    """
    Preprocesses the text: Remove apostrophes, punctuation marks, etc.
    Returns a list of text
    """
    preprocessed_text = []
    file = open(text, 'r') # open the text file for reading
    # remove punctuation in file
    for line in file:
        line = line.strip() # remove end line characters apparently
        line = line.lower()
        line = ''.join([char for char in line if char not in string.punctuation])
        preprocessed_text.append(line)

    # test print statement
    # for line in preprocessed_text:
    #     print(line)

    return preprocessed_text


def build_vocab(preprocessed_text):
    """
    Builds the vocab from the preprocessed text
    preprocessed_text: output from process_text
    Returns unique text tokens
    """
    # vocab is an array of strings that consists of all unique words in the preprocessed_text in alphabetical order
    unique_words_arr = []
    for line in preprocessed_text:
        words_in_line = line.split(" ");
        for word in words_in_line:
            if word not in unique_words_arr and word != '' and word != '\t':
                unique_words_arr.append(word)
                
    vocab = sorted(unique_words_arr)

    # test print
    # print(vocab)

    return vocab


def vectorize_text(text, vocab):
    """
    Converts the text into vectors
    text: preprocess_text from process_text
    vocab: vocab from build_vocab
    Returns the vectorized text and the labels
    """
    

    return vectorized_text, labels


def accuracy(predicted_labels, true_labels):
    """
    predicted_labels: list of 0/1s predicted by classifier
    true_labels: list of 0/1s from text file
    return the accuracy of the predictions
    """

    return accuracy_score


def main():
    # Take in text files and outputs sentiment scores
    build_vocab(process_text(sys.argv[1]))

    return 1


if __name__ == "__main__":
    main()