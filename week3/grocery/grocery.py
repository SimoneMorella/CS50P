def main():
    g_dict = {}
    while True:
        try:
            item = input().upper()
            if item in g_dict:
                g_dict[item] += 1
            else:
                g_dict.update({item : 1})
        except EOFError:
            create_g_list(g_dict)
            break


def create_g_list(dict):
    g_list = list(dict)
    g_list.sort()
    for item in g_list:
        print(f"{dict[item]} {item}")

main()