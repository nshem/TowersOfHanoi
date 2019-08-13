

def parse_total_disks_num(txt_input):
    try:
        value = int(txt_input.readline())
    except ValueError:
        raise
    else:
        return value


def parse_moves(txt_input):
    return txt_input.readlines()
