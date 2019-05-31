import random  # 임의의 음운 선택
import hgtk  # 한글 자모 조합


class RandName:
    # 랜덤 글자 생성 함수
    @classmethod
    def character(cls):

        # 자모음 리스트
        consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅎ']  # 자음
        vowel = ['ㅏ', 'ㅐ', 'ㅖ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅜ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ']  # 모음
        vowel2 = ['ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅡ', 'ㅣ']  # 받침이 있을 때의 모음
        final_consonant = ['ㄱ', 'ㄴ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅇ']  # 받침

        # 자모음 리스트에서 한 음운씩 선택
        a = random.sample(consonant, 1)[0]
        b = random.sample(vowel, 1)[0]
        c = random.sample(final_consonant, 1)[0]
        d = random.sample(vowel2, 1)[0]

        # 랜덤으로 받침 여부를 결정 후 글자 만들기
        bat = random.choice([True, False])  # 받침 여부
        if bat:
            result = hgtk.letter.compose(a, b)
        else:
            result = hgtk.letter.compose(a, d, c)
        return result

    # 이름 생성 함수
    @classmethod
    def make_name(cls, input_num):
        if input_num > 7 or input_num < 1:
            name = '그 정도 길이의 이름은 예쁘지 않아요. 더 짧게 만들어 보아요!'
        else:
            make_list = [cls.character() for _ in range(int(input_num))]
            name = ''.join(make_list)
        return name

