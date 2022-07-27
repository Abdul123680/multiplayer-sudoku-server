import flask
import html_utils

server = flask.Flask(__name__)

board = [[''] * 9,
         [''] * 9,
         [''] * 9,
         [''] * 9,
         [''] * 9,
         [''] * 9,
         [''] * 9,
         [''] * 9,
         [''] * 9]
board[3][2] = 1


@server.route("/show-board")
def show_board():
    display = '<table id="grid">'
    for line in board:
        display += '<tr>'
        cell_number = 0
        for number in line:
            if number != '':
                display += '<td><input id="cell-' + str(cell_number) + '" type="text" value="' + str(number) + '" disabled></td>'
            else:
                display += '<td><input id="cell-' + str(cell_number) + '" type="text"></td>'
            cell_number += 1
        display += '</tr>'
    display += '</table>'
    return html_utils.wrap_board_style(display)


if __name__ == '__main__':
    server.run(debug=True, host='localhost')