import re
import random

source = 'English.txt'

with open(source,encoding='utf-8') as f:
    data = f.read()

english_words = re.findall('[a-z]+',data)
ja = re.findall('\s.*\n',data)

meanings = []
for word in ja:
    m = re.sub('\t|\n','',word)
    meanings.append(m)

words_dict = dict(zip(english_words,meanings))

n_tests = 50
n_questions = 50
for test_num in range(n_tests):
    with open('英単語テスト_{:02d}.txt'.format(test_num + 1),'w') as f:

        f.write('出席番号:\n'
                '名前:\n\n'
                '第{}回英単語テスト\n\n'.format(test_num +1 ))

        for question_num in range(n_questions):
            question_word = random.choice(english_words)
            correct_answer = words_dict[question_word]
            meanings_copy = meanings.copy()
            meanings_copy.remove(correct_answer)
            wrong_answers = random.sample(meanings_copy, 3)

            ansewer_options = [correct_answer] + wrong_answers

            random.shuffle(ansewer_options)

            f.write('問{}.{}\n\n'.format(question_num + 1, question_word))

            for i in range(4):
                f.write('{}. {}\n'.format(i + 1, ansewer_options[i]))
            f.write('\n')

            f.write('答え：' + correct_answer + '\n\n\n')
