def get_word_count(file_content):
    words = file_content.split()
    word_count = len(words)
    return word_count

def get_num_per_character(file_content):
    dict = {}
    file_content = file_content.lower()
    for c in file_content:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict

def build_console_report(dict):
    report_list = []
    for key in dict:
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = dict[key]
        report_list.append(temp_dict)
   
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def sort_on(items):
    return items["num"]
