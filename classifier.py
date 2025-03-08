# This file implements a Naive Bayes Classifier
import math

class BayesClassifier():
    """
    Naive Bayes Classifier
    file length: file length of training file
    sections: sections for incremental training
    """
    def __init__(self):
        self.postive_word_counts = {}
        self.negative_word_counts = {}
        self.positive_sentence_count = 0
        self.negative_sentence_count = 0
        self.percent_positive_sentences = 0
        self.percent_negative_sentences = 0
        self.file_length = 499
        self.file_sections = [self.file_length // 4, self.file_length // 3, self.file_length // 2, self.file_length]


    def train(self, train_data, train_labels, vocab):
        """
        This function builds the word counts and sentence percentages used for classify_text
        train_data: vectorized text
        train_labels: vectorized labels
        vocab: vocab from build_vocab
        """
        self.set_counts(vocab)

        for label in train_labels:
            if label == 1:
                self.positive_sentence_count += 1
            else:
                self.negative_sentence_count += 1
        self.percent_positive_sentences = self.positive_sentence_count / len(train_labels)
        self.percent_negative_sentences = self.negative_sentence_count / len(train_labels)

        for i in range(len(train_data)):
            for j in range(len(vocab)):
                if train_data[i][j] == 1:
                    if train_labels[i] == 1:
                        self.postive_word_counts[vocab[j]] += 1
                    else:
                        self.negative_word_counts[vocab[j]] += 1

        return


    def classify_text(self, vectors, vocab):
        """
        vectors: [vector1, vector2, ...]
        predictions: [0, 1, ...]
        """
        predictions = []

        for vector in vectors:
            pos_prob = math.log(self.percent_positive_sentences)
            neg_prob = math.log(self.percent_negative_sentences)
            for i in range(len(vector)):
                if vector[i] == 1:
                    pos_prob += math.log(self.postive_word_counts[vocab[i]] / self.positive_sentence_count)
                    neg_prob += math.log(self.negative_word_counts[vocab[i]] / self.negative_sentence_count)
            predictions.append(1 if pos_prob > neg_prob else 0)

        return predictions
    

    def set_counts(self, vocab):
        """
        This function resets the counts for the classifier
        """
        self.postive_word_counts = {}
        self.negative_word_counts = {}
        for word in vocab:
            self.postive_word_counts[word] = 1
            self.negative_word_counts[word] = 1

        self.positive_sentence_count = 2 # Number of possibilites for labels
        self.negative_sentence_count = 2
        self.percent_positive_sentences = .5
        self.percent_negative_sentences = .5
        
        return