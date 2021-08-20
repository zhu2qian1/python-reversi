from examples import testboard

coordination = tuple[int, int]


class ReversiGame:

    code_and_name: dict[int, str] = {
        0: "empty",
        1: "white",
        2: "black",
        3: "reserved",
        4: "reserved",
        5: "reserved",
        6: "reserved",
        7: "reserved",
        8: "reserved",
        9: "self",
    }

    initial_board: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def is_turn_of_black(self, turnnum: int) -> bool:
        return True if turnnum % 2 == 0 else False

    def __init__(self) -> None:
        self.board: list[list[int]] = self.initial_board

    def does_code_exist(self, code: int) -> bool:
        return code in self.code_and_name

    def place_stone(self, code: int, x_coord: int, y_coord: int) -> None:
        # ! imprement this
        assert self.does_code_exist(code)

        # TODO: check if the stone is placable

        self.board[y_coord][x_coord] = code

        # TODO: turn stones as needed

        raise NotImplementedError

    def count_stones(self, white_or_black: str) -> dict[str, int]:
        counters: dict[str, int] = {name: 0 for name in self.code_and_name.values()}
        # default {"empty": 0, "white" : 0, "black" : 0}
        for row in self.board:
            for cell in row:
                counters[self.code_and_name[cell]] += 1

        return counters

    def fetch_all_direction_array(
        self, x_coord: int, y_coord: int
    ) -> tuple[dict[coordination, int]]:
        # ! implement this
        raise NotImplementedError

    def fetch_direction_array(
        self, x_coord: int, y_coord: int, direction: int
    ) -> dict[coordination, int]:
        """fetch information of a row of stones along a direction.

        Args:
            x_coord (int): original x coordination of cell
            y_coord (int): origin of cell
            direction (int): 0: horizontal, 1: top-left to lower-right, 2: vertical, 3: lower-left to top-right

        Returns:
            dict[tuple[int, int], int]: position of cell and its stone stat
        """
        addresses: dict[tuple[int, int], int] = {}
        x_factor: int = 1
        y_factor: int = 0

        direction %= 4

        if direction == 1:
            x_factor, y_factor = 1, 1
        elif direction == 2:
            x_factor, y_factor = 0, 1
        else:
            x_factor, y_factor = 1, -1

        for i in range(-8, 8, 1):
            x: int = x_coord + i * x_factor
            y: int = y_coord + i * y_factor
            if i == 0:
                addresses[(x, y)] = 9
                continue
            if x < 0 or y < 0:
                continue
            cell = self.tell_what_in_cell(x, y)

            if cell != -1:
                addresses[(x, y)] = cell
        return addresses

    def draw_board(self):
        for row in self.board:
            for cell in row:

                grid = " "
                if cell == 1:
                    grid = "O"
                elif cell == 2:
                    grid = "X"

                print(f" {grid}", end="")
            print(" ")

    def tell_what_in_cell(self, x_coord: int, y_coord: int) -> int:
        try:
            return self.board[y_coord][x_coord]
        except IndexError:
            return -1


if __name__ == "__main__":
    game: ReversiGame = ReversiGame()
    game.draw_board()
    game.board = testboard
    game.draw_board()

    arrays: list[dict[coordination, int]] = []
    for i in range(0, 4):
        arrays.append(game.fetch_direction_array(4, 2, i))

    for i in arrays:
        print(i)
