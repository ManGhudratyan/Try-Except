def read_data(fname):
    try:
        with open(fname, "r") as f:
            return f.readlines()
    except FileNotFoundError as err:
        print(err)
        exit()

def get_sum(content):
    msum = 0
    for el in content:
        try:
            msum += int(el.strip())
        except ValueError:
            print("A non  int is detected", el)
    return msum

def main():
    fname = "data.txt"
    content = read_data(fname)
    print(get_sum(content)) 
   
main()
