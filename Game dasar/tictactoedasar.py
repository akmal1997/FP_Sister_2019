import random
try:
    raw_input()
except NameError:
    raw_input = input

WIN_COMBINATIONS = [(1, 2, 3),
                    (4, 5, 6),
                    (7, 8, 9),
                    (1, 4, 7),
                    (2, 5, 8),
                    (3, 6, 9),
                    (1, 5, 9),
                    (3, 5, 7)]

def display_board(board):
    print('''   |   |  
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {} 
   |   |
-----------
   |   |
 {} | {} | {}
   |   |'''.format(*board[1:10]))

def player_input():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Pemain 1, Pilih O atau X untuk bermain').upper()
    if marker == 'X':
        return {'Pemain 1': 'X', 'Pemain 2': 'O'}
    else:
        return {'Pemain 2': 'X', 'Pemain 1': 'O'}

def win_check (board):
    return any(board[a] != ' ' and board[a] == board[b] == board[c] for a, b, c in WIN_COMBINATIONS)

def choose_first(players):
    random_player = 'Pemain {}'.format(random.randint(1, 2))
    return random_player, players[random_player]

def full_check (board):
    return all(b != ' ' for b in board)

def player_choice(board):
    while True:
        try:
            position = int(raw_input('Silahkan masukkan angka 1-9 '))
            if position in range(1, 10) and board[position] == ' ':
                return position
        except ValueError:
            pass

def replay():
    return raw_input('Maukah anda bermain lagi? Ketik Ya atau Tidak: ').lower().startswith('y')

def ttt():
    board = [' ' for _ in range(10)]
    players = player_input()
    name, player_marker = choose_first(players)
    print('{} dengan tanda {} akan bermain pertama.'.format(name, player_marker))
    while True:
        position = player_choice(board)
        board[position] = player_marker
        display_board(board)
        if win_check(board):
            print('Selamat {}! Anda telah memenangkan permainan ini!'.format(name))
            break

        if full_check(board):
            print('Selamat {} dan {}! Anda telah menang seri!'.format(players.keys()))
            break

        name = 'Pemain 1' if name == 'Pemain 2' else 'Pemain 2'
        player_marker = players[name]
        print(name, player_marker)

if __name__ == '__main__':
    print('Selamat Datang di permainan Tic Tac Toe!')
    print('Aturan permainan: ')
    print('Isi angka 1-9 di kolom input. Angka tersebut akan memposisikan dimana posisi simbol X atau O yang anda inginkan')
    print('Jika sudah terisi ketiganya secara horizontal/vertikal/diagonal, anda menang\n')
    print('Untuk format barisan dan kolom adalah seperti ini:')
    print('(1 2 3)')
    print('(4 5 6)')
    print('(7 8 9)\n')
    print('Simpel kan? Selamat mencobaaaa')
    while True:
        ttt()
        if not replay():
            break
