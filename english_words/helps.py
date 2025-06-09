
def _exit(**kwargs):
    exit()
    
    return False


def _answer(**kwargs):
    print(str(kwargs["custom"]) +'({})_answer : {}{} \033[0m'.format(kwargs["word"][0],'\033[35m',kwargs["word"][2]))

    return False


def _pass(**kwargs):
    
    return True

def _search(**kwargs):

    
    return False
    



features = {"_answer":_answer,"_exit":_exit,"_pass":_pass,"_search":_search}


def ask(word:list,custom="") -> int:

    color = "\033[34m"
    miss = 0
    while True:
        answer = input(str(custom) +'({}) {}{} : \033[0m'.format(word[0],color,word[1]))

        if answer == word[2]:
            break
        elif answer in list(features.keys()):

            if (features[answer.split(" ")[0]](word=word,
                                                custom=custom,
                                                color=color,
                                                command=answer.split("\n")[1::]
                                                )):
                break
            
        miss += 1
        color = '\033[31m'

    return miss


