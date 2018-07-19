def Sudoku(file):
	if (!get_input(file)) {
        printf("Incorrect input.\n");
        sys.exit();
    }

def get_input(file):
	data = np.loadtxt(file);
	char c;
    int i = 0, j = 0;
    for(c : )
    while((c = getchar()) != EOF):
        if c == '\n' && j:
            if j > 0 && j != RANGE: 
            # premature
                printf("i:%d, j:%d\n", i, j);
                return false;
            
            
            if j == RANGE: 
            # new line
                j = 0;
                i++;

        if isdigit(c):
            grid[i][j++][VALUE] = c - '0';
        
    
    #print_grid();
    return i == RANGE && j == 0;

def preassess():
# to check if the sudoku ia valid
# input: sudoku_3.txt
# output: There is clearly no solution
# 		  There might be a solution
flag = True;
if (!isValid())
    print("There is clearly no solution.\n");
    flag = False;
else
    print("There might be a solution.\n");
    
def isValid():


def bare_tex_output():
# output the sudoku in the tex style



def forced_tex_output():
# output the sudoku that has used forced digits tech


def marked_tex_output():
# used forced digits tech and has been marked


def worked_tex_output():
# used forced digits tech and has been marked, 
# and the preemptive set tech has been applied. 


