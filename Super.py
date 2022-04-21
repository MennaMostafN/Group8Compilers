from tkinter import *
import nltk
import re
import automata
from nltk.lm import counter
from automata.fa.dfa import DFA


class Super:
    def _init_(self):
        pass

    def divText(self, text):
        identifier = r"(^[^\d\W]\w*\Z)"  # for Identifier
        number = r"^[0-9]+"  # for NUM and Decimals
        symbols = r"[;\<\>\=]"
        keyword = r"repeat|until"
        symbols1 = r":=|<=|>="

        for line in text:
            tokens = nltk.wordpunct_tokenize(line)
            print(tokens)
        for i in range(0, len(tokens)):
            if re.fullmatch(keyword, tokens[i]):
                # tracetokens.append(tokens[x])
                label2 = Label(frame1, text=tokens[i] + "    is a Keyword", bg='lightblue')
                label2.pack()
                # print(x, " : KEYWORD")
            else:
                if re.fullmatch(identifier, tokens[i]):
                    # print(x, " : NUMBER")
                    # tracetokens.append(tokens[x])
                    label3 = Label(frame1, text=tokens[i] + "   is an identifier", bg='lightblue')
                    label3.pack()
                    # break
                else:
                    if re.fullmatch(symbols, tokens[i]):
                        # print(x, " : SYMBOL")

                        label4 = Label(frame1, text=tokens[i] + "   is a Symbol", bg='lightblue')
                        # tracetokens.append(tokens[x])
                        label4.pack()
                        # break
                    else:
                        if re.fullmatch(number, tokens[i]):
                            # print(x, " : IDENTIFIER")
                            label5 = Label(frame1, text=tokens[i] + "   is a Number", bg='lightblue')
                            # tracetokens.append(tokens[x])
                            label5.pack()
                            # break
                        else:
                            if re.fullmatch(symbols1, tokens[i]):
                                # print(x, " : IDEN")
                                label6 = Label(frame1, text=tokens[i] + "   is a Symbol", bg='lightblue')

                                label6.pack()
                                # tracetokens.append(tokens[x])
                                # break
                            else:
                                # print(x, " : NO MATCH")
                                label7 = Label(frame1, text=tokens[i] + "   is a NO MATCH", bg='lightblue')
                                label7.pack()
        tokenType = ["" for x in range(len(tokens))]
        for i in range(0, len(tokens)):
            if (tokens[i] == '='):
                tokenType[i] = '='
            else:
                if (tokens[i] == '>'):
                    tokenType[i] = '>'
                else:
                    if (tokens[i] == '<'):
                        tokenType[i] = '<'
                    else:
                        if (tokens[i] == ';'):
                            tokenType[i] = ';'
            if re.fullmatch(identifier, tokens[i]):
                tokenType[i] = 'id'

            if re.fullmatch(keyword, tokens[i]):
                if (tokens[i] == 'repeat'):
                    tokenType[i] = 'repeat'

            if (re.fullmatch(keyword, tokens[i])):
                if (tokens[i] == 'until'):
                    tokenType[i] = 'until'

            if re.fullmatch(number, tokens[i]):
                tokenType[i] = 'num'

            if re.fullmatch(symbols1, tokens[i]):
                if (tokens[i] == ':='):
                    tokenType[i] = ':='

            if re.fullmatch(symbols1, tokens[i]):
                if (tokens[i] == '<='):
                    tokenType[i] = '<='

            if re.fullmatch(symbols1, tokens[i]):
                if (tokens[i] == '>='):
                    tokenType[i] = '>='
        print(tokenType)
        dfa = DFA(
            states={'START', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'FINAL', 'DEAD'},
            input_symbols={'repeat', 'id', ':=', ';', 'until', '=', '>', '<', '>=', '<=', 'num'},
            transitions={
                'START': {'repeat': 's2', 'id': 'DEAD', ':=': 'DEAD', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                          '>': 'DEAD', '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                          'num': 'DEAD'},
                's2': {'repeat': 'DEAD', 'id': 's3', ':=': 'DEAD', ';': 'DEAD', 'until': 's7', '=': 'DEAD', '>': 'DEAD',
                       '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                       'num': 'DEAD'},
                's3': {':=': 's4', 'repeat': 'DEAD', 'id': 'DEAD', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                       '>': 'DEAD', '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD', 'num': 'DEAD'},
                's4': {':=': 'DEAD', 'repeat': 'DEAD', 'id': 's5', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                       '>': 'DEAD',
                       '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                       'num': 's5'},
                's5': {':=': 'DEAD', 'repeat': 'DEAD', 'id': 'DEAD', ';': 's6', 'until': 'DEAD', '=': 'DEAD',
                       '>': 'DEAD',
                       '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                       'num': 'DEAD'},
                's6': {':=': 'DEAD', 'repeat': 'DEAD', 'id': 's3', ';': 'DEAD', 'until': 's7', '=': 'DEAD', '>': 'DEAD',
                       '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                       'num': 'DEAD'},
                's7': {':=': 'DEAD', 'repeat': 'DEAD', 'id': 's8', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                       '>': 'DEAD',
                       '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                       'num': 's8'},
                's8': {':=': 'DEAD', 'repeat': 'DEAD', 'id': 'DEAD', ';': 'DEAD', 'until': 'DEAD', '=': 's9', '>': 's9',
                       '<': 's9', '>=': 's9', '<=': 's9',
                       'num': 'DEAD'},
                's9': {':=': 'DEAD', 'repeat': 'DEAD', 'id': 'FINAL', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                       '>': 'DEAD', '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                       'num': 'FINAL'},
                'FINAL': {'repeat': 'DEAD', 'id': 'DEAD', ':=': 'DEAD', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                          '>': 'DEAD', '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                          'num': 'DEAD'},
                'DEAD': {'repeat': 'DEAD', 'id': 'DEAD', ':=': 'DEAD', ';': 'DEAD', 'until': 'DEAD', '=': 'DEAD',
                         '>': 'DEAD', '<': 'DEAD', '>=': 'DEAD', '<=': 'DEAD',
                         'num': 'DEAD'}
            },
            initial_state='START',
            final_states={'FINAL'}
        )
        # x = str(dfa.read_input(tokenType))
        if dfa.accepts_input(tokenType):
            label333 = Label(frame2, text=" Input Accepted ",font = "Helvetica 12 bold ",bg='light green')
            label333.pack(pady=0)
        else:
            label336 = Label(frame2, text="ERROR , the input entered is incorrect!" ,font = "Helvetica 12 bold")
            label336.pack()
        print("Final state is " + str(dfa.read_input(tokenType)))
        states_list = (list(dfa.read_input_stepwise(tokenType)))
        print("tokens:  ", tokenType)
        print("states sequence: ", states_list)
        # label333 = Label(frame2,text="Final state : "+ str(dfa.read_input(tokenType)))
        # label333.pack()
        label334=Label(frame2,text= "Tokens : "+ str(tokenType),bg='light green',font = "Helvetica 12 italic")
        label334.pack(pady=5)
        label335 = Label(frame2, text = "Sequence of states of input is :" + str(states_list), bg='light green',font = "Helvetica 12 italic")
        label335.pack(pady=10)
    def remove_Spaces(self, program):
        scanned_Program = []
        for line in program:
            if (line.strip() != ''):
                scanned_Program.append(line.strip())
        return scanned_Program

    def exc(self, text):
        scanned_Prog = self.remove_Spaces(text)
        scanned_Program_lines = text.split('\n')
        Source_Code = []
        for line in scanned_Program_lines:
            Source_Code.append(line)
            self.divText(Source_Code)




# ---------------------------------------------------
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab
from tkinter import ttk
from automata.fa.dfa import DFA



class DFA1:
    G = nx.DiGraph()
    ax = plt.subplot()
    G.add_node(' ')
    G.add_node('  ')
    G.add_node('id')
    G.add_node('until')
    G.add_node('repeat|until|id|num|symbol')
    G.add_edges_from([(' ', 'START')])
    transition = [('START', 's2', 'repeat '), ('START', 'DEAD', 'other'), ('s2', 's3', 'id'), ('s3', 's4', ':='),
                  ('s2', 'DEAD', 'other'), ('s3', 'DEAD', 'other'), ('s4', 'DEAD', 'other'),
                  ('s5', 'DEAD', 'other'), ('s6', 'DEAD', 'other'), ('s7', 'DEAD', 'other'),
                  ('s8', 'DEAD', 'other'), ('s9', 'DEAD', 'other'), ('s6', 's7', 'until'),
                  ('s7', 's8', 'id|num'), ('s4', 's5', 'id|num'), ('s5', 's6', ';'), ('s8', 's9', '=|>|<|>=|<='),
                  ('s9', 'FINAL', 'id|num'), ('FINAL', 'DEAD', 'other')]
    for i in transition:
        G.add_edge(i[0], i[1], transition=i[2])

    positions = {'START': [-130, 0], 's2': [-75, 0], 's3': [-35, 0], 's4': [0, 0], 's5': [50, 0], 's6': [80, 0],
                 's9': [285, 0], 's7': [120, 0], 's8': [175, 0], 'FINAL': [130, -125], 'DEAD': [0, -125],
                 ' ': [-160, 30], '  ': [10, -125], 'id': [22, 38], 'until': [22, 65],
                 'repeat|until|id|num|symbol': [0, -180]}

    fixed_nodes = positions.keys()
    pos = nx.spring_layout(G, pos=positions, fixed=fixed_nodes)
    nx.draw(G, pos, with_labels=True, font_size=10, node_color='red')
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color='w',
                           nodelist=[(' '), ('id'), ('until'), ('repeat|until|id|num|symbol')])
    nx.draw_networkx_edges(G, pos, edge_color='black', connectionstyle='arc3, rad = 0.5', edgelist=[('s6', 's3')],
                           width=1,
                           arrowsize=9)
    nx.draw_networkx_edges(G, pos, edge_color='black', connectionstyle='arc3, rad = -0.5', edgelist=[('s2', 's7')],
                           width=1,
                           arrowsize=9)
    nx.draw_networkx_edges(G, pos, edge_color='black', connectionstyle='arc3, rad = -20', edgelist=[('  ', 'DEAD')],
                           width=1, arrowsize=9)
    nx.draw_networkx_edges(G, pos, edge_color='black', width=1, arrowsize=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'transition'))

    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

    def present(self):
        pylab.show()
        plt.show()

# ---------------------------------------------------
root = Tk()
root.title("Welcome to my compiler")
mynotebook = ttk.Notebook(root)
mynotebook.pack()
frame1 = Frame(mynotebook, padx=100, pady=120, bg='light blue')
frame2 = Frame(mynotebook, padx=100, pady=120, bg='light green')
frame1.pack(fill="both", expand=1, padx=20, pady=10)
frame2.pack(fill="both", expand=1, padx=20, pady=10)
mynotebook.add(frame1, text="Tokens")
mynotebook.add(frame2, text="DFA graph")
firstlabel = Label(frame1, text="Enter your repeat statement", fg='black', bg='light blue', font="Verdana 15 bold ")
firstlabel.pack(padx=10, pady=10)
firstentry = Entry(frame1, width=20, font=('Ariel', 10))
firstentry.insert(END, " ")
firstentry.pack(padx=10, pady=5)



def view_command():
    l1 = Super()
    l1.exc(firstentry.get())
    firstentry.delete(0, 'end')


def openDfa1():
    d = DFA1()
    d.present()


tokenbut = Button(frame1, text="Display Tokens", command=view_command, activebackground='red', fg='black',
                  font=("times", 15), bg='pink')
tokenbut.place(x=90, y=120)
tokenbut.pack()
ShowDfaButton = Button(frame2, text='Display DFA', command=openDfa1, activebackground='red', fg='Black',
                       font=("times", 15), bg='pink')
ShowDfaButton.pack()

root.mainloop()


