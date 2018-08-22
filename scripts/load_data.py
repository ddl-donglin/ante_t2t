# coding=utf-8
import pickle as pickle

if __name__ == '__main__':
    ROOT_DATA_PATH = '../data_manager/'
    with open('{}self_antecedent_generate_sentences.pkl'.format(ROOT_DATA_PATH), 'rb') as f:
        # get all the sentences for antecedent identification
        _sentences = pickle.load(f)

    for _sent in _sentences:
        # sum pooling, FloatTensor, Size: 400
        _sent.input_vec_sum
        # sum pooling with feature, FloatTensor, Size: 468
        _sent.input_vec_sum_feature
        # GRU, FloatTensor, Size: 6100
        _sent.input_vec_hidden
        # GRU with feature, FloatTensor, Size: 6168
        _sent.input_vec_hidden_feature
        # AttentionGRU, FloatTensor, Size: 1600
        _sent.input_vec_attention
        # AttentionGRU with feature, FloatTensor, Size: 1668
        _sent.input_vec_attention_feature
        # tag(1 for positive case, and 0 for negative case), Int, Size: 1
        _sent.antecedent_label
        # tag(1 for positive case, and 0 for negative case), Int, Size: 1
        _sent.trigger_label
        # trigger word for the error analysis, Str
        _sent.trigger
        # trigger word auxiliary type for the experiment, Str
        _sent.aux_type
        # the original sentence for the error analysis, Str
        _sent.sen

        print(_sent.input_vec_sum)