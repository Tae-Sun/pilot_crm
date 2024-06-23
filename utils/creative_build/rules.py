class CommonRule:
    BAD_WORD = '욕설을 사용해서는 안돼'
    SEXUAL = '성적인 단어는 최대한 지양해야 해'
    HATRED = '누군가가 증오를 느낄 만한 단어와 표현을 피하자'

    @classmethod
    def get_all_rules(cls):
        return {
            k: v for cls in CopyWritingRules.__mro__
            for k, v in cls.__dict__.items()
            if not k.startswith('__')
               and 'function' not in str(v)
        }


class CopyWritingRules(CommonRule):
    MARKETER = '간결하고 번뜩이는 광고 문구를 생성해야해'