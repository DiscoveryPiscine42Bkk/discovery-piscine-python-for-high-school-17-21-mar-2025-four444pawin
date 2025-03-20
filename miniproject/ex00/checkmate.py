def chess_position_to_index(pos):
    col_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    col, row = pos[0].upper(), int(pos[1])
    return (8 - row, col_map[col] - 1)

def is_checkmate(king_pos, piece, piece_pos):
    k_row, k_col = chess_position_to_index(king_pos)
    p_row, p_col = chess_position_to_index(piece_pos)
    
    moves = []
    if piece == 'Q':  # Queen moves like Rook + Bishop
        moves += [(k_row + i, k_col + i) for i in range(-7, 8)]  # Diagonals
        moves += [(k_row + i, k_col - i) for i in range(-7, 8)]
        moves += [(k_row, k_col + i) for i in range(-7, 8)]  # Straight
        moves += [(k_row + i, k_col) for i in range(-7, 8)]
    elif piece == 'R':  # Rook moves straight
        moves += [(k_row, k_col + i) for i in range(-7, 8)]
        moves += [(k_row + i, k_col) for i in range(-7, 8)]
    elif piece == 'B':  # Bishop moves diagonally
        moves += [(k_row + i, k_col + i) for i in range(-7, 8)]
        moves += [(k_row + i, k_col - i) for i in range(-7, 8)]
    elif piece == 'N':  # Knight moves in L-shape
        moves = [(k_row + x, k_col + y) for x, y in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]]
    elif piece == 'P':  # Pawn moves forward one step, captures diagonally
        moves = [(k_row - 1, k_col - 1), (k_row - 1, k_col + 1)]
    elif piece == 'K':  # King moves one square in any direction
        moves = [(k_row + i, k_col + j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
    
    # Remove out-of-bounds moves
    moves = {(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8}
    
    # Check if the piece is attacking the king
    if (p_row, p_col) in moves:
        return "Checkmate!"
    return "Not checkmate."

if __name__ == "__main__":
    king_pos = input("Enter the King position (Ex. A1): ")
    piece = input("Enter the chess piece (K, Q, R, N, B, P): ")
    piece_pos = input("Enter the piece position (Ex. A2): ")
    print(is_checkmate(king_pos, piece, piece_pos))
