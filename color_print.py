class ColorPrint:
    black_back = ["\033[31m\033[40m", "\033[32m\033[40m", "\033[33m\033[40m",
                  "\033[34m\033[40m", "\033[35m\033[40m", "\033[37m\033[40m"]
    red_back = ["\033[30m\033[41m", "\033[32m\033[41m", "\033[33m\033[41m",
                "\033[34m\033[41m", "\033[35m\033[41m", "\033[37m\033[41m"]
    green_back = ["\033[30m\033[42m", "\033[31m\033[42m", "\033[33m\033[42m",
                  "\033[34m\033[42m", "\033[35m\033[42m", "\033[37m\033[42m"]
    yellow_back = ["\033[30m\033[43m", "\033[31m\033[43m", "\033[32m\033[43m",
                   "\033[34m\033[43m", "\033[35m\033[43m", "\033[37m\033[43m"]
    blue_back = ["\033[30m\033[44m", "\033[31m\033[44m", "\033[32m\033[44m",
                 "\033[33m\033[44m", "\033[35m\033[44m", "\033[37m\033[44m"]
    purple_back = ["\033[30m\033[45m", "\033[31m\033[45m", "\033[32m\033[45m",
                   "\033[33m\033[45m", "\033[34m\033[45m", "\033[37m\033[45m"]
    white_back = ["\033[30m\033[47m", "\033[31m\033[47m", "\033[32m\033[47m",
                  "\033[33m\033[47m", "\033[34m\033[47m", "\033[35m\033[47m"]
    default_back = ["\033[30m", "\033[31m", "\033[32m",
                    "\033[33m", "\033[34m", "\033[35m"]
    red_bla , gre_bla, yel_bla, blu_bla, pur_bla, whi_bla = black_back
    bla_red, gre_red, yel_red, blu_red, pur_red, whi_red = red_back
    bla_gre, red_gre, yel_gre, blu_gre, pur_gre, whi_gre = green_back
    bla_yel, red_yel, gre_yel, blu_yel, pur_yel, whi_yel = yellow_back
    bla_blu, red_blu, gre_blu, yel_blu, pur_blu, whi_blu = blue_back
    bla_pur, red_pur, gre_pur, yel_pur, blu_pur, whi_pur = purple_back
    bla_whi, red_whi, gre_whi, yel_whi, blu_whi, pur_whi = white_back
    black, red, green, yellow, blue, purple = default_back
    default = "\033[0m\033[0m"

    @staticmethod
    def ctext(text, scheme):
        return f'{scheme}{text}{ColorPrint.default}'

    @staticmethod
    def cprint(text, scheme):
        print(ColorPrint.ctext(text, scheme))

    @staticmethod
    def rtext(text, scheme_list):
        return_text = ''
        count = 0
        for letter in text:
            return_text += f'{scheme_list[count]}{letter}{ColorPrint.default}'
            count += 1
            if count >= len(scheme_list):
                count = 0
        return return_text

    @staticmethod
    def rprint(text, scheme_list):
        print(ColorPrint.rtext(text, scheme_list))


def main():
    ColorPrint.rprint('color_print.py v1.0', ColorPrint.default_back)
    print('by ' + ColorPrint.ctext('Shuwiku', ColorPrint.green))


if __name__ == '__main__':
    main()
