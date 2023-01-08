def _parse_symbols(self):
    # Inicijalizacija predefiniranih oznaka.
    self._init_symbols()
    
    # Prvo parsiramo deklaracije oznaka. Npr. "(LOOP)".
    self._iter_lines(self._parse_labels)

    # Na kraju parsiramo varijable i reference na oznake te ih pretvaramo u
    # konstante. Npr. "@SCREEN" pretvaramo u "@16384" ili "@END" kojemu je
    # oznaka "(END)" bila u trecoj liniji pretvaramo u "@3".
    self._n = 16
    self._iter_lines(self._parse_variables)

# Svaka oznaka mora biti sadrzana unutar oblih zagrada. Npr. "(LOOP)". Svaka
# oznaka koju procitamo treba zapamtiti broj linije u kojoj se nalazi i biti
# izbrisana iz nje. Koristimo dictionary _labels.
def _parse_labels(self, line, p, o):
    if line[0] != "(":
        return line
    else:
        label = line[1:].split(")")
        if len(label) > 2 or (label[1] != ""): 
            self._flag = False
            self._line = o
            self._errm = "Invalid label."
        elif len(label[0])==0:
            self._flag = False
            self._line = o
            self._errm = "Invalid label."
        else:
            self._labels[label[0]] = str(p)
            
    return ""

def _parse_macro(self, line, p, o):
    if line[0] != "$":
        return line
    self.macro = True
    try:
        naredba = line[1:].split("(")[0]
        argumenti = naredba[:-1]
        arg = argumenti.split(",") 
    except:
        pass
    # u B sprema A 
    if naredba == "$MV":
        return ["@" + arg[1], "D=M", "@" + arg[0], "M=D", "@" + arg[1] , "M=0"]
    
    
    # zbraja A i B i sprema u D 
    elif naredba == "$SUM":
        return ["@" + arg[0], "D=M", "@" + arg[1],"D=M+D", "@" + arg[2],"D=M "]
    
    # mjenja sadrzaj A i B 
    elif naredba == "$SWP":
        return ["@" + arg[0], "D=M", "@908", "M=D", "@" +arg[1], "D=M", "@" +arg[0],"M=D","@908", "D=M" , "@" + arg[1], "M=D"]


    # izvršava se dok RAM[A] ne postane 0 
#    elif naredba == "$WHILE":

    
    # terminira while petlju 
#    elif naredba == "$END":

    else:
        self._flag = False
        self._errm = "Invalid macro."
        return ""







# Svaki poziv na varijablu ili oznaku je oblika "@NAZIV", gdje naziv nije broj.
# Prvo provjeriti oznake ("_labels"), a potom varijable ("_vars"). Varijablama
# dodjeljujemo memorijske adrese pocevsi od 16. Ova funkcija nikad ne vraca
# prazan string!
def _parse_variables(self, line, p, o):
    if line[0] != "@":
        return line

    l = line[1:]

    if l.isdigit():
        return line

    if l in self._labels.keys():
        return "@" + self._labels[l]
    elif l in self._variables.keys():
        return "@" + self._variables[l]
    else:
        self._variables[l] = str(self._n)
        self._n += 1
        return "@" + str(self._n - 1)

# Inicijalizacija predefiniranih oznaka.
def _init_symbols(self):
    self._labels = {
        "SCREEN" : "16384",
        "KBD" : "24576",
        "SP" : "0",
        "LCL" : "1",
        "ARG" : "2",
        "THIS" : "3",
        "THAT" : "4"
    }
    
    for i in range(0, 16):
        self._labels["R" + str(i)] = str(i)
        