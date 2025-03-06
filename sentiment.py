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
        words_in_line = line.split(" ")
        for word in words_in_line:
            if word not in unique_words_arr and word != '' and word != '\t' and word != '0' and word != '1':
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
    vectorized_text = []
    labels = []


    for line in text:
        vect_line = []
        words_in_line = line.split(" ")
        
        for v_word in vocab:
            if v_word in words_in_line:
                vect_line.append(1)
            else:
                vect_line.append(0)

        # Checks last char which is the class label
        if line[len(line) - 1] == "1":
            labels.append("1")
        else:
            labels.append("0")
        vectorized_text.append(vect_line)

    return vectorized_text, labels



def create_txt_file(file_name, vector_text, vocab, labels):
    """
    Creates a text file with the vectorized text
    vector_text: vectorized text from vectorize_text
    vocab: vocab from build_vocab
    """
    file = open(file_name, "w")

    for word in vocab:
        file.write(word + ",")
    file.write("classlabel\n")

    for i in range(len(vector_text)):
        for val in vector_text[i]:
            file.write(str(val) + ",")
        print(f"c_t_x {i}: {labels[i]}")
        file.write(f"{labels[i]}\n")

    file.close()

    return 1

def full_preprocess():
    test_processed_text = process_text("testSet.txt")
    test_vocab = build_vocab(test_processed_text)
    test_vector_text, test_labels = vectorize_text(test_processed_text, test_vocab)
    create_txt_file("preprocessed_test.txt", test_vector_text, test_vocab, test_labels)

    train_processed_text = process_text("trainingSet.txt")
    train_vocab = build_vocab(train_processed_text)
    train_vector_text, train_labels = vectorize_text(train_processed_text, train_vocab)
    create_txt_file("preprocessed_train.txt", train_vector_text, train_vocab, train_labels)


def accuracy(predicted_labels, true_labels):
    """
    predicted_labels: list of 0/1s predicted by classifier
    true_labels: list of 0/1s from text file
    return the accuracy of the predictions
    """
    correct = 0
    for i in range(len(predicted_labels)):
        if predicted_labels[i] == true_labels[i]:
            correct += 1
    accuracy_score = correct / len(predicted_labels)

    return accuracy_score


def main():
    # Take in text files and outputs sentiment scores
    full_preprocess()



    return 1


if __name__ == "__main__":
    main()