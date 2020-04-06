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
    # artical = """The whole village soon learnt that a large sum of money had been lost. Sam Benton, the local butcher, had
    # lost his wallet while taking his savings to the post office. Sam was sure that the wallet must have been found by
    # one of the villagers, but it was not returned to him. Three months passed, and then one morning, Sam found his
    # wallet outside his front door. It had been wrapped up in newspaper and it contained half the money he had lost,
    # together with a note which said: 'A thief, yes, but only 50 per cent a thief!' Two months later, some more money
    # was sent to Sam with another note: 'Only 25 per cent a thief now!' In time, all Sam's money was paid back in this way. The last note
    # said: 'I am 100 per cent honest now!'
    #     """
    # artical2 = """
    #     When a plane from London arrived at Sydney airport, workers began to unload a number of wooden boxes
    # which contained clothing. No one could account for the fact that one of the boxes was extremely heavy. It
    # suddenly occurred to one of the workers to open up the box. He was astonished at what he found. A man was lying
    # in the box on top of a pile of wooden goods. He was so surprised at being discovered that he did not even try to
    # run away. After he was arrested, the man admitted hiding in the box before the plane left London. He had had a
    # long and uncomfortable trip, for he had been confined to the wooden box for over eighteen hours. The man was
    # ordered to pay $3,500 for the cost of the trip. The normal price of a ticket is $2,000!
    # """
    #     artical3 = """
    #     A public house which was recently bought by Mr. Ian Thompson is up for sale. Mr.Thompson is going to sell
    # it because it is haunted. He told me that he could not go to sleep one night because he heard a strange noise
    # coming from the bar. The next morning, he found that the doors had been blocked by chairs and the furniture had
    # been moved. Though Mr.Thompson had turned the lights off before he went to bed, they were on in the morning.
    # He also said that he had found five empty whisky bottles which the ghost must have drunk the night before. When
    # I suggested that some villagers must have come in for a free drink, Mr.Thompson shook his head. The villagers
    # have told him that they will not accept the pub even if he gives it away
    # """
    # artical = """
    #     Dentists always ask questions when it is impossible for you to answer. My dentist had just pulled out one of
    # my teeth and had told me to rest for a while. I tried to say something, but my mouth was full of cotton wool. He
    # knew I collected match boxes and asked me whether my collection was growing. He then asked me how my
    # brother was and whether I liked my new job in London. In answer to these questions I either nodded or made
    # strange noises. Meanwhile, my tongue was busy searching out the hole where the tooth had been. I suddenly felt
    # very worried, but could not say anything. When the dentist at last removed the cotton wool from my mouth, I was
    # able to tell him that he had pulled out the wrong tooth.
    # """

    artical = """
At last firemen have put out a big forest fire in California. Since then, they have been trying to find out how
the fire began. Forest fires are often caused by broken glass or by cigarette ends which people carelessly throw
away. Yesterday the firemen examined the ground carefully, but were not able to find any broken glass. They were
also quite sure that a cigarette end did not start the fire. This morning, however, a firemen accidentally discovered
the cause. He noticed the remains of a snake which was wound round the electric wires of a 16,000-volt power
line. In this way, he was able to solve the mystery. The explanation was simple but very unusual. A bird had
snatched up the snake from the ground and then dropped it on to the wires. The snake then wound itself round the
wires. When it did so, it sent sparks down to the ground and these immediately started a fire
    """

    artical_str = make_practice(artical)
    print(artical_str)

