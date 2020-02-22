# 用于练习打字
from random import choice


def make_practice(artical, signals=[';', '\'', '"', '/', ',', '.', '?',
                                    '{', '}', '[', ']', '_', '\\', '_', '-', '+', '=', '0', ')', '(', '*']):
    """
    在字符串与空格之间添加各种c语言符号，用于练习打字速度

    Parameters
    ----------
    artical : str
        可以是任意一篇文章
    signals: list
        符号想要练习的符号

    Returns
    -------
    artical_str : str   
        带有符号的文章
    """
    artical_str = ""
    artical_list = artical.split(' ')

    for word in artical_list:
        # 排除文章的逗号句号等符号
        # print(word)
        if (word == '' or word == '\t' or word == '\n'):
            pass
        elif (word[-1] in signals):
            artical_str += word
        else:
            artical_str += word+choice(signals)
        artical_str += ' '
    return artical_str


if __name__ == "__main__":
    # artical = """Mrs. Anne Sterling did not think of the risk she was taking when she ran through a forest after two men. They
    #             had rushed up to her while she was having a picnic at the edge of a forest with her children and tried to steal her
    #             handbag. In the struggle, the strap broke and, with the bag in their possession, both men started running through the trees. Mrs. Sterling got so angry that she ran after them. She was
    #             soon out of breath, but she continued to run. When she caught up with them, she saw that they had sat down and
    #             were going through the contents of the bag, so she ran straight at them. The men got such a fright that they
    #             dropped the bag and ran away. 'The strap needs mending,' said Mrs. Sterling later, 'but they did not steal anything."""
    artical = """The whole village soon learnt that a large sum of money had been lost. Sam Benton, the local butcher, had
lost his wallet while taking his savings to the post office. Sam was sure that the wallet must have been found by
one of the villagers, but it was not returned to him. Three months passed, and then one morning, Sam found his
wallet outside his front door. It had been wrapped up in newspaper and it contained half the money he had lost,
together with a note which said: 'A thief, yes, but only 50 per cent a thief!' Two months later, some more money
was sent to Sam with another note: 'Only 25 per cent a thief now!' In time, all Sam's money was paid back in this way. The last note
said: 'I am 100 per cent honest now!'
    """
    artical_str = make_practice(artical)
    print(artical_str)
