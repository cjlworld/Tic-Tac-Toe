from flask import Flask, render_template, request, session
import tictactoe
import json

app = Flask(__name__)
app.secret_key = 'fefenlwafmekjsfewfojflkwanfkrjefnjkrea'

# 游戏模式
class Mode():
    """
    游戏模式
        link: 相对根地址的链接
        title: 模式的名称
    """
    def __init__(self, title, link):
        self.title = title
        self.link = link

Modes = [Mode("Tic-Tac-Toe", "tic-tac-toe")]

# 主页面
@app.route("/")
def index():
    """
    渲染模式按钮
    """
    return render_template("index.html", modes=Modes)

# tic-tac-toe
@app.route("/tic-tac-toe", methods=["GET", "POST"])
def TicTacToe():
    session["board"] = tictactoe.initial_state()
    return render_template("tictactoe.html")

@app.route("/tic-tac-toe/action", methods=["POST"])
def tictactoe_action():
    """
    receive the actions from the frontend
    """
    json_data = request.json
    row = int(json_data["row"])
    col = int(json_data["col"])

    # 验证数据的合法性
    board = session["board"]
    if row < 0 or row > 2 or col < 0 or col > 2:
        return json.dumps({"board": board, "signal": "failure"})
    elif tictactoe.player(board) != tictactoe.X:
        return json.dumps({"board": board, "signal": "failure"})
    # 结束了
    elif tictactoe.terminal(board):
        winner = tictactoe.winner(board)
        if winner == None:
            return json.dumps({"board": board, "signal": "Tie"})
        else:
            return json.dumps({"board": board, "signal": winner})

    # Take action
    board = tictactoe.result(board, (row, col))
    board = tictactoe.result(board, tictactoe.minimax(board))
    session["board"] = board
    return json.dumps({"board": board, "signal": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)