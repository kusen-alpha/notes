def remove_all_tags_by_regex(text, sub_regex=None,sep=''):
    """
    删除html文本中的所有标签，只留文本内容
    :param text: html文本
    :param sub_regex: 附加删除正则
    :param sep: 替换后符号
    :return:
    """
    if sub_regex:
        if isinstance(sub_regex, str):
            sub_regex = [sub_regex, ]
        for regex in sub_regex:
            text = re.sub(regex, sep, text, flags=re.S | re.M)
    return re.sub(r'<.*?>', sep, text, flags=re.S | re.M).strip()


def remove_all_tags_from_content_by_regex(content, sub_regex=None, sep=''):
    """
    删除html中正文区域所有标签
    :param content:
    :param sub_regex:
    :param sep:
    :return:
    """
    content = re.sub(r'<script>.*</script>', sep, content, flags=re.S | re.M)
    content = remove_all_tags_by_regex(content, sub_regex, sep=sep)
    return content.strip()