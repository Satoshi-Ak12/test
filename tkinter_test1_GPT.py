import tkinter as tk
from tkinter import ttk

root = tk.Tk()

class App:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=500, height=300, bg="black")
        self.canvas.pack()

        self.segment_a = self.canvas.create_rectangle(50, 20, 150, 40, fill="gray")
        self.segment_b = self.canvas.create_rectangle(150, 40, 170, 140, fill="gray")
        self.segment_c = self.canvas.create_rectangle(150, 160, 170, 260, fill="gray")
        self.segment_d = self.canvas.create_rectangle(50, 260, 150, 280, fill="gray")
        self.segment_e = self.canvas.create_rectangle(30, 160, 50, 260, fill="gray")
        self.segment_f = self.canvas.create_rectangle(30, 40, 50, 140, fill="gray")
        self.segment_g = self.canvas.create_rectangle(50, 140, 150, 160, fill="gray")

        # self.segment_dp = self.canvas.create_oval(170, 260, 190, 280, fill="gray")

        self.segments = [
            self.segment_a, self.segment_b, self.segment_c,
            self.segment_d, self.segment_e, self.segment_f, self.segment_g
        ]

        self.button = tk.Button(root, text="CountUp", command=self.CountUp, width=8, height=2)
        self.button.pack()

        # a,b,c,d,e,f,g の順で0/1（dpは含めない）
        self.DIGIT_MAP = {
            "nothing": [0,0,0,0,0,0,0],
            0: [1,1,1,1,1,1,0],
            1: [0,1,1,0,0,0,0],
            2: [1,1,0,1,1,0,1],
            3: [1,1,1,1,0,0,1],
            4: [0,1,1,0,0,1,1],
            5: [1,0,1,1,0,1,1],
            6: [1,0,1,1,1,1,1],
            7: [1,1,1,0,0,0,0],
            8: [1,1,1,1,1,1,1],
            9: [1,1,1,1,0,1,1],
        }

    def Char_Replace(self, colors):
        # colors: ['gray','red', ...] -> [0/1,...]
        values = []
        for color in colors:
            values.append(0 if color == 'gray' else 1)
        return values

    def color_confirm(self):
        colors = []
        for seg in self.segments:
            colors.append(self.canvas.itemcget(seg, "fill"))
        return self.Char_Replace(colors) 

    def Rev_lookup(self, value_list):
        # value_list: [0/1,...] の7要素
        for k, v in self.DIGIT_MAP.items():
            if v == value_list:
                return k
        return None  # 見つからないとき

    def Display(self, number):
        # numberに対応する7要素マスクを色に変換して反映
        mask = self.DIGIT_MAP[number]
        colors = ['red' if bit else 'gray' for bit in mask]
        for seg, color in zip(self.segments, colors):
            self.canvas.itemconfig(seg, fill=color)

    def CountUp(self):
        currents = self.color_confirm()            # 今の0/1状態（7要素）
        if currents == self.DIGIT_MAP["nothing"]:  # まだ何も表示していない
            self.Display(0)
            return

        char_value = self.Rev_lookup(currents)
        if char_value is None or char_value == "nothing":
            # 想定外の状態 → 0に戻すなどのフォールバック
            self.Display(0)
            return

        n = int(char_value)
        n = (n + 1) % 10   # 0〜9でループ
        self.Display(n)

def main():
    app = App(root)
    app.CountUp()
    root.mainloop()

if __name__ == "__main__":
    main()