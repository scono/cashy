import path
import simulate_key
import pillow
import tesseract
import webrequest
import simulate_websearch
import show
import telegram_code
import ranking
import time

fragen_nr = 0

#telegram_code.send_hello()

while True:

    #simulate_key.take_screenshot()
    picture_path = path.get_path()
    q_path, a1_path, a2_path, a3_path, nr_path = pillow.get_sub_pics(picture_path)

    q_str, a1_str, a2_str, a3_str, nr_str = tesseract.get_pic_text(q_path, a1_path, a2_path, a3_path, nr_path)
    path.hist_file(picture_path, nr_str, True)

    if fragen_nr != nr_str:
        fragen_nr = nr_str
            
        simulate_websearch.search_visual(q_str)

        answer_tuples, a_ans = ranking.search_ranking(q_str, a1_str, a2_str, a3_str, nr_str)
        
        telegram_code.send_result(q_str, answer_tuples, a_ans)
        show.show_result(q_str, answer_tuples, a_ans)  