#Program No.12 default parameter value passing
#(Value inside Formal will act as Actual parameter)
def citizen(country = "American"):
    print("I'm from " + country)

def studentnames(fname):
    fname = input("Enter the name")
    return fname
citizen()
citizen("VietNam")
citizen("India")
