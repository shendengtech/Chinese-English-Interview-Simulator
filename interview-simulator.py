import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import json
import os

QUESTION_FILE = "questions.json"  # 题库保存的文件名

class InterviewSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("面试模拟器 - 英语/中文 (macOS系统say朗读)")
        self.process = None
        self.saying = False

        # 初始化题库
        self.questions = self.load_questions()
        if not self.questions:
            self.questions = [
                {"question": "Python 中的列表和元组有什么区别？", "answer": "列表是可变的，元组是不可变的。"},
                {"question": "What is the difference between list and tuple in Python?", "answer": "List is mutable, tuple is immutable."}
            ]
        self.q_index = 0

        # 推荐voice
        self.voice_options = {
            "中文": ["Tingting", "Tingting (Enhanced)", "Shanshan (Enhanced)", "Meijia", "Meijia (Premium)", "Sinji"],
            "英语": ["Moira", "Samantha", "Daniel", "Karen", "Tessa", "Fred", "Moira"]
        }
        self.selected_voice = tk.StringVar()

        # 语言选择
        self.lang_var = tk.StringVar(value="中文")
        lang_frame = tk.Frame(master)
        lang_frame.pack(pady=5)
        tk.Label(lang_frame, text="朗读语言:").pack(side="left")
        for lang in ["中文", "英语"]:
            tk.Radiobutton(lang_frame, text=lang, variable=self.lang_var, value=lang, command=self.update_voice_menu).pack(side="left")

        # voice下拉菜单
        voice_frame = tk.Frame(master)
        voice_frame.pack(pady=5)
        tk.Label(voice_frame, text="选择朗读人声:").pack(side="left")
        self.voice_menu = tk.OptionMenu(voice_frame, self.selected_voice, *self.voice_options["中文"])
        self.voice_menu.pack(side="left")
        self.update_voice_menu()

        self.question_label = tk.Label(master, text="", font=('Arial', 14), wraplength=420, justify="left")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Text(master, height=4, width=55, font=('Arial', 12))
        self.answer_entry.pack(pady=5)

        self.std_answer_label = tk.Label(master, text="", font=('Arial', 12), fg='green', wraplength=420, justify="left")
        self.std_answer_label.pack(pady=3)

        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="显示标准答案", command=self.show_answer).pack(side="left", padx=3)
        self.speak_q_btn = tk.Button(btn_frame, text="朗读题目", command=lambda: self.start_say("question"))
        self.speak_q_btn.pack(side="left", padx=3)
        self.speak_a_btn = tk.Button(btn_frame, text="朗读标准答案", command=lambda: self.start_say("answer"))
        self.speak_a_btn.pack(side="left", padx=3)
        tk.Button(btn_frame, text="下一题", command=self.next_question).pack(side="left", padx=3)
        tk.Button(btn_frame, text="删除当前题目", command=self.delete_question, fg='red').pack(side="left", padx=3)

        # 控制按钮
        control_frame = tk.Frame(master)
        control_frame.pack(pady=5)
        self.stop_btn = tk.Button(control_frame, text="■ 停止", command=self.stop_say, state="disabled")
        self.stop_btn.pack(side="left", padx=3)

        add_frame = tk.LabelFrame(master, text="添加新考题", padx=5, pady=5)
        add_frame.pack(pady=10, fill="x", expand=True)
        tk.Label(add_frame, text="考题：").grid(row=0, column=0, sticky="e")
        self.new_q_entry = tk.Entry(add_frame, width=60)
        self.new_q_entry.grid(row=0, column=1, padx=4, pady=2)
        tk.Label(add_frame, text="标准答案：").grid(row=1, column=0, sticky="e")
        self.new_a_entry = tk.Entry(add_frame, width=60)
        self.new_a_entry.grid(row=1, column=1, padx=4, pady=2)
        tk.Button(add_frame, text="添加到题库", command=self.add_question).grid(row=2, column=1, sticky="e", pady=3)

        self.load_question()

        # 绑定窗口关闭事件，实现自动保存
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_questions(self):
        if os.path.exists(QUESTION_FILE):
            try:
                with open(QUESTION_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_questions(self):
        try:
            with open(QUESTION_FILE, "w", encoding="utf-8") as f:
                json.dump(self.questions, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showwarning("保存失败", f"题库保存失败：{e}")

    def update_voice_menu(self):
        lang = self.lang_var.get()
        menu = self.voice_menu["menu"]
        menu.delete(0, "end")
        for v in self.voice_options[lang]:
            menu.add_command(label=v, command=lambda vname=v: self.selected_voice.set(vname))
        if self.voice_options[lang]:
            self.selected_voice.set(self.voice_options[lang][0])

    def load_question(self):
        if self.questions and 0 <= self.q_index < len(self.questions):
            q = self.questions[self.q_index]["question"]
            self.question_label.config(text=f"问题{self.q_index+1}：{q}")
            self.answer_entry.delete(1.0, tk.END)
            self.std_answer_label.config(text="")
        elif not self.questions:
            self.question_label.config(text="题库为空，请添加新题目！")
            self.answer_entry.delete(1.0, tk.END)
            self.std_answer_label.config(text="")
            self.q_index = 0
        else:
            messagebox.showinfo("结束", "题目已全部完成！")
            self.q_index = 0
            self.load_question()

    def show_answer(self):
        if self.questions and self.q_index < len(self.questions):
            answer = self.questions[self.q_index]["answer"]
            self.std_answer_label.config(text=f"标准答案：{answer}")

    def start_say(self, mode):
        if self.saying:
            return
        if self.questions and self.q_index < len(self.questions):
            text = self.questions[self.q_index]["question"] if mode == "question" else self.questions[self.q_index]["answer"]
            voice = self.selected_voice.get()
            self.saying = True
            self.update_audio_control_buttons()
            self.saying_thread = threading.Thread(target=self.say, args=(text, voice))
            self.saying_thread.daemon = True
            self.saying_thread.start()

    def say(self, text, voice):
        try:
            # -r 170 为语速
            self.process = subprocess.Popen(["say", "-v", voice, "-r", "170", text])
            self.process.communicate()
        except Exception as e:
            messagebox.showwarning("系统朗读出错", f"调用 say 命令失败：{e}")
        self.saying = False
        self.update_audio_control_buttons()

    def stop_say(self):
        if self.saying and self.process:
            try:
                self.process.terminate()
            except Exception:
                pass
            self.saying = False
            self.update_audio_control_buttons()

    def update_audio_control_buttons(self):
        state = "normal" if not self.saying else "disabled"
        self.speak_q_btn.config(state=state)
        self.speak_a_btn.config(state=state)
        self.stop_btn.config(state="normal" if self.saying else "disabled")

    def next_question(self):
        self.stop_say()
        if self.questions:
            self.q_index = (self.q_index + 1) % len(self.questions)
            self.load_question()

    def add_question(self):
        q = self.new_q_entry.get().strip()
        a = self.new_a_entry.get().strip()
        if not q or not a:
            messagebox.showwarning("输入不完整", "请填写考题和标准答案！")
            return
        self.questions.append({"question": q, "answer": a})
        messagebox.showinfo("添加成功", "新题目已加入题库！")
        self.new_q_entry.delete(0, tk.END)
        self.new_a_entry.delete(0, tk.END)
        if len(self.questions) == 1:
            self.q_index = 0
            self.load_question()
        self.save_questions()  # 实时保存

    def delete_question(self):
        self.stop_say()
        if not self.questions:
            messagebox.showwarning("题库为空", "没有题目可删除！")
            return
        confirm = messagebox.askyesno("确认删除", "确定要删除当前题目吗？")
        if confirm:
            del self.questions[self.q_index]
            if self.q_index >= len(self.questions):
                self.q_index = max(0, len(self.questions) - 1)
            self.load_question()
            messagebox.showinfo("删除成功", "题目已删除！")
            self.save_questions()  # 实时保存

    def on_close(self):
        self.save_questions()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterviewSimulator(root)
    root.mainloop()
