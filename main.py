from examples import testboard


class ReversiGame:
    code_and_name: dict[int, str] = {
        0: "empty",
        1: "white",
        2: "black",
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
    ) -> tuple[dict[tuple, int]]:
        raise NotImplementedError

    def fetch_direcion_array(
        self, x_coord: int, y_coord: int, direction: int
    ) -> dict[tuple, int]:
        addresses: dict[tuple, int] = {}
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
            if i == 0:
                continue
            x = x_coord + i * x_factor
            y = y_coord + i * y_factor
            cell = self.tell_what_in_cell(x, y)

            if cell != -1:
                addresses[(x, y)] = cell
        return addresses

    def is_adjacent_cells_filled(self, x_coord: int, y_coord: int) -> bool:
        # ? delete needed?
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.tell_what_in_cell(x_coord + j, y_coord + i) == -1:
                    continue
                if self.tell_what_in_cell(x_coord + j, y_coord + i):
                    return True
        return False

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
