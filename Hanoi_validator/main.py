import sys
import utils


class Game:
    def __init__(self, total_disks_num, moves):
        self.total_disks_num = total_disks_num
        self.total_rods_num = 3
        self.rods = self.initialize_rods()
        self.moves = moves
        self.isValid = self.move()

    def initialize_rods(self):
        rods = [Rod() for item in range(self.total_rods_num)]
        rods[0].disks = self.initialize_disks()
        return rods

    def initialize_disks(self):
        disks = list(range(self.total_disks_num, 0, -1))
        return disks

    def move_is_legal(self, current_move, from_rod, to_rod):
        if len(from_rod.disks) > 0:
            disk = from_rod.disks.pop()
            if not to_rod.disks or disk < to_rod.disks[-1]:
                to_rod.disks.append(disk)
                return True
        return False

    def move(self):
        if self.moves:
            current_move = self.moves.pop(0)
            from_rod = self.rods[int(current_move[0])-1]
            to_rod = self.rods[int(current_move[1])-1]

            if self.move_is_legal(current_move, from_rod, to_rod):
                return self.move()

        return self.win()

    def win(self):
        for rod in self.rods[1:]:
            if len(rod.disks) == self.total_disks_num:
                print('YES')
                return True
        print('NO')
        return False


class Rod:
    def __init__(self):
        self.disks = []


def validate_solution():
    if len(sys.argv) == 1:
        print('Error: no files where given')
        quit()

    for file in sys.argv[1:]:
        try:
            with open(file, 'r') as txt_input:
                total_disks_num = utils.parse_total_disks_num(txt_input)
                moves = utils.parse_moves(txt_input)
                current_game = Game(total_disks_num, moves)
        except FileNotFoundError:
            print(f'Error: no such file in the directory ({file})')
        except ValueError:
            print(f'Error: Empty or invalid file ({file})')
        except:
            print(f'Error: unknown error ({file})')


if __name__ == "__main__":
    validate_solution()
