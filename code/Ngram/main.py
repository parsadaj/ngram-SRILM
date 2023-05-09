import os


HW_path = '/Users/parsa/Daneshgah/Arshad/2/NLP/Homeworks/HW1'
lexicon_path = os.path.join(HW_path, 'results/lexicon.txt')
train_corpus_path = os.path.join(HW_path, 'data/final_train.txt')
test_corpus_path = os.path.join(HW_path, 'data/final_test.txt')

count_file_path = os.path.join(HW_path, 'results/n{order}_{smoothing_name}.count')
lm_path = os.path.join(HW_path, 'results/n{order}_{smoothing_name}.lm')
ppl_path = os.path.join(HW_path, 'results/n{order}_{smoothing_name}.ppl')

SRILM_path = '/Users/parsa/Daneshgah/Arshad/2/NLP/SRILM/bin/macosx/'

# Step 1: lexicon, train_corpus -> ngram-count => count_file
def create_count_file(lexicon_path, train_path, out_file, order):
    command = SRILM_path + 'ngram-count -vocab {vocab} -text {train} -order {order} -write {out_file} -unk'.format(
        vocab=lexicon_path, train=train_path, out_file=out_file, order=order
    )

    os.system(command)
    
    return command

# Step 2: lexicon, count_file -> ngram-count => language_model
def create_lm(lexicon_path, count_file, out_file, order, smoothing_command):
    command = SRILM_path + 'ngram-count -vocab {vocab} -read {count_file} -order {order} -lm {out_file}'.format(
        vocab=lexicon_path, count_file=count_file, out_file=out_file, order=order
    ) + smoothing_command

    os.system(command)

    return command

# Step 3: language_model, test_corpus -> ngram => perplexity
def get_ppl(test_file, lm, out_file, order):
    command = SRILM_path + 'ngram -ppl {test_file} -order {order} -lm {lm} > {out_file}'.format(
        vocab=lexicon_path, test_file=test_file, out_file=out_file, lm=lm, order=order
    )

    os.system(command)

    return command 

smoothing = dict(
    laplace=' -addsmooth 1',
    wittenbell=' -wbdiscount1 -wbdiscount2 -wbdiscount3',
    absolute=' -cdiscount1 0.5 -cdiscount2 0.5 -cdiscount3 0.5'
)


for order in range(1,4):
    for smoothing_name, smoothing_command in smoothing.items():
        current_count_file =  count_file_path.format(order=order, smoothing_name=smoothing_name)
        current_lm =  lm_path.format(order=order, smoothing_name=smoothing_name)
        current_ppl =  ppl_path.format(order=order, smoothing_name=smoothing_name)
        create_count_file(lexicon_path, train_corpus_path, current_count_file, order)
        create_lm(lexicon_path, current_count_file, current_lm, order, smoothing_command)
        get_ppl(test_corpus_path, current_lm, current_ppl, order)