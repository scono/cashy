
def show_result(q_str, answer_tuples, a_ans):
    print('_____________________________________________________________________________')
    print(q_str.encode("utf-8"))
    print('\n')
    for ans in answer_tuples:
        if ans[0] == a_ans:
            print(ans[1])
    print('_____________________________________________________________________________')

if __name__ == "__main__":
    pass