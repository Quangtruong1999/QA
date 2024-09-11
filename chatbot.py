# Use a pipeline as a high-level helper
from transformers import pipeline

generate = pipeline("text-generation", model="Quangtruong61/qa_model", device=0)

# prompt = """다음은 작업을 설명하는 명령입니다. 요청을 적절하게 완료하는 응답을 작성하세요.

# ### 지침:
# {}

# ### 응답:
# {}"""

prompt = """Đây là lệnh giải thích hoạt động: Vui lòng viết phản hồi hoàn thành yêu cầu một cách thích hợp.

### hướng dẫn:
{}

### phản ứng:
{}"""

def _exe_answer(answers):
    list_answer = answer.split("\nanswer")
    if list_answer:
        # print(list_answer)
        if len(list_answer) <= 1:
            return list_answer[0].strip()
        elif list_answer[0].strip() == list_answer[1].strip():
            return list_answer[0]
        return "\n".join([list_answer[0], list_answer[1]])
    return "Sorry, I don't understand your question"

def _exe_answer_ver2(answers):
    list_answer = answer.split("\nanswer")
    if list_answer:
        return list_answer[0].strip
    return "Sorry, I don't understand your question"

while True:
    question = str(input("Hãy đặt câu hỏi: ")).strip()
    if question:
        messages = [
            {"role": "user", "content": prompt.format(question, "")},
        ]
        output = generate(messages, max_new_tokens=512)
        if output:
            generated_text = output[0]['generated_text']
            if generated_text:
                answer = generated_text[-1]['content']
                print(_exe_answer(answer))
        choice = input("Bạn có muốn tiếp tục không?\n Tiếp tục hãy nhấn Y\n Thoát chương trình ấn phím bất kỳ\n")
        try:
            if choice and choice.lower() == 'y':
                continue
            else:
                break
        except:
            break
    else:
        break
# Tôi cần biết mức thuế thu nhập cá nhân hiện tại là bao nhiêu?
# Tiền lương tôi 10.000.000 VNĐ thì phải đóng thuế bao nhiêu?
# messages = [
#     {"role": "user", "content": "Tiền lương tôi 10.000.000 VNĐ thì phải đóng thuế bao nhiêu?"},
# ]
# print(pipe(messages, max_new_tokens=512))
