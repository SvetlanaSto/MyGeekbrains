from soap_check_text import check_text


def test_step1(correct_word, incorrect_word):
    assert correct_word in check_text(incorrect_word), 'Test1 FAILED'

